#!/bin/bash

trap 'echo "Job failed."; do_cleanup; exit 1' ERR
trap 'echo "Received signal to stop."; do_cleanup; exit 1' SIGINT

do_cleanup () { 
    echo "Backing up nimbo logs..."
    $AWS s3 cp --quiet $LOCAL_LOG $S3_LOG_PATH

    PERSIST="$(grep 'persist:' $CONFIG | awk '{print $2}')"
    if [ "$PERSIST" = "no" ]; then
        echo "Deleting instance $INSTANCE_ID."
        sudo shutdown now >/tmp/nimbo-system-logs
    fi
}

PYTHONUNBUFFERED=1

INSTANCE_ID=$1
JOB_CMD=$2

AWS=/usr/local/bin/aws
PROJ_DIR=/home/ubuntu/project
CONDA_PATH=/home/ubuntu/miniconda3
CONDASH=$CONDA_PATH/etc/profile.d/conda.sh

cd $PROJ_DIR

CONFIG=nimbo-config.yml
source ./nimbo_vars

if [ -z "${ENCRYPTION}" ]; then
    S3CP="$AWS s3 cp"
    S3SYNC="$AWS s3 sync"
else
    S3CP="$AWS s3 cp --sse $ENCRYPTION"
    S3SYNC="$AWS s3 sync --sse $ENCRYPTION"
fi

ENV_FILE=local_env.yml
ENV_NAME="$(grep 'name:' $ENV_FILE | awk '{print $2}')"

S3_LOG_NAME=$(date +%Y-%m-%d_%H-%M-%S).txt
S3_LOG_PATH=$S3_RESULTS_PATH/nimbo-logs/$S3_LOG_NAME
LOCAL_LOG=/home/ubuntu/nimbo-log.txt
echo "Will save logs to $S3_LOG_PATH"

mkdir -p $LOCAL_DATASETS_PATH
mkdir -p $LOCAL_RESULTS_PATH
mkdir -p $CONDA_PATH


# ERROR: This currently doesn't allow for a new unseen env to be passed. Fix this.
if [ -f "$CONDASH" ]; then
    echo ""
    echo "Conda installation found."
else
    echo "Conda installation not found. Installing..."
    wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -bfp /home/ubuntu/miniconda3
    rm Miniconda3-latest-Linux-x86_64.sh
    echo "source $CONDASH" >> .bashrc
fi

source $CONDASH

echo "Creating conda environment: $ENV_NAME"
conda env create -q --file $ENV_FILE
conda activate $ENV_NAME

echo "Done."

# Import datasets and results from the bucket
echo ""
echo "Importing datasets from $S3_DATASETS_PATH to $LOCAL_DATASETS_PATH..."
$S3CP --recursive $S3_DATASETS_PATH $LOCAL_DATASETS_PATH >/tmp/nimbo-s3-logs
echo "Importing results from $S3_RESULTS_PATH to $LOCAL_RESULTS_PATH..."
$S3CP --recursive $S3_RESULTS_PATH $LOCAL_RESULTS_PATH >/tmp/nimbo-s3-logs

echo ""
echo "================================================="
echo ""

nohup bash -c "while true;  
do $S3CP --quiet $LOCAL_LOG $S3_LOG_PATH >>/tmp/nimbo-s3-logs 2>&1;
$S3SYNC --quiet $LOCAL_RESULTS_PATH $S3_RESULTS_PATH >>/tmp/nimbo-s3-logs 2>&1;
sleep 10; done" >/dev/null 2>&1 &

if [ "$JOB_CMD" = "_nimbo_launch_and_setup" ]; then
    echo "Setup complete. You can now use 'nimbo ssh $1' to ssh into this instance."
    exit 0
elif [ "$JOB_CMD" = "_nimbo_notebook" ]; then
    if ! conda env export | grep -q jupyterlab; then
        echo "Jupyterlab installation not found. Installing..."
        conda install -q -y jupyterlab -c conda-forge >/dev/null
    fi
    nohup jupyter lab --no-browser --port 57467 --autoreload --ServerApp.token="" >/tmp/nimbo-notebook-logs 2>&1 &
    echo "Notebook running at http://localhost:57467/lab"
    exit 0
else
    echo "Running job: ${@:2}"
    eval ${@:2}
fi

echo ""
echo "Saving results to S3..."
$S3SYNC $LOCAL_RESULTS_PATH $S3_RESULTS_PATH

conda deactivate
echo ""
echo "Job finished."

do_cleanup; exit 0

