<p align="center">
  <img src="https://user-images.githubusercontent.com/6595222/115258675-1bf98300-a129-11eb-8ea1-24cdc67d81e8.png" width="480" height="240">
</p>

# Nimbo: Machine Learning on AWS with a single command

[Nimbo](https://nimbo.sh) is a dead-simple command-line tool that allows you to run code on AWS as if you were running it locally. It abstracts away the complexity of AWS, allowing you to build, iterate, and deliver machine learning models faster than ever.

### Example - ```nimbo run "python -u train.py --lr=3e-4```
<a href="https://asciinema.org/a/408353" target="_blank"><img src="https://asciinema.org/a/408353.svg" height=300 width=300/></a>

### The fastest way to prototype on AWS

Nimbo drastically simplifies your AWS workflow by taking care of instance, environment, data, and IAM management - no changes to your codebase needed. Whether you're just getting started with AWS or are a seasoned veteran, Nimbo takes the pain out of doing Machine Learning in the cloud, allowing you to focus on what matters - building great models for your team and clients.

### Powerful commands

Nimbo provides many useful commands to supercharge your productivity when working with AWS, such as easily launching notebooks, checking prices, logging onto an instance, or syncing data. Some examples include :
- `nimbo ls-spot-prices`
- `nimbo ssh <instance-id>`
- `nimbo push datasets`
- `nimbo pull logs`
- `nimbo rm-all-instances`

## Key Features
- **Your Infrastructure:**
Code runs on your EC2 instances and data is stored in your S3 buckets. This means that you can easily use the resulting models and data from anywhere within your AWS organization, and use your existing permissions and credentials.
- **User Experience:**
Nimbo gives you the command line tools to make working with AWS as easy as working with local resources. No more complicated SDKs and never-ending documentation.
- **Customizable:**
Want to use a custom AMI? Just change the image ID in the Nimbo config file. Want to use a specific conda package? Just add it to your environment file. Nimbo is built with customization in mind, so you can use any setup you want.
- **Seamless Spot Instances**
With Nimbo, using spot instances is as simples as changing a single value on the config file. Enjoy the 70-90% savings with AWS spot instances with no changes to your workflow.
- **Managed Images**
We provide managed AMIs with the latest drivers, with unified naming across all regions. We will also release AMIs that come preloaded with ImageNet and other large datasets, so that you can simply spin up an instance and start training.

You can find more information at [nimbo.sh](https://nimbo.sh), or read the docs at [docs.nimbo.sh](https://docs.nimbo.sh).

## Getting started
Please visit the [Getting started](https://docs.nimbo.sh/getting-started) page in the docs.

## Examples
Sample projects can be found at our examples repo, [nimbo-examples](https://github.com/nimbo-sh/nimbo-examples).
Current examples include:
- [Finetuning an object segmentation network with Detectron2](https://github.com/nimbo-sh/nimbo-examples/tree/main/detectron)
- [Training a neural network on MNIST with Pytorch](https://github.com/nimbo-sh/nimbo-examples/tree/main/pytorch-mnist)
- [Training a neural network on MNIST with Tensorflow, on a spot instance](https://github.com/nimbo-sh/nimbo-examples/tree/main/tensorflow-mnist)

## Product roadmap
- **GCP support:** Use the same commands to run jobs on AWS or GCP.
- **Deployment:** Deploy ML models to AWS/GCP with a single command. Automatically create an API endpoint for providing video/audio/text and getting results from your model back.
- **Add Docker support:** Right now we assume you are using a conda environment, but many people use docker to run jobs. This feature would allow you to run a command such as `nimbo run "docker-compose up"`, where the docker image would be fetched from DockerHub (or equivalent repository) through a `docker_image` parameter on the `nimbo-config.yml` file.
- **Add AMIs with preloaded large datasets:** Downloading and storing large datasets like ImageNet is a time consuming process. We will make available AMIs that come with an extra EBS volume mounted on `/datasets`, so that you can use large datasets without worrying about storing them or waiting for them to be fetched from your S3 bucket. Get in touch if you have datasets you would like to see preloaded with the instances. 

## Developing

If you want to make changes to the codebase, you can clone this repo and
1. `pip install -e .` to install nimbo locally. As you make code changes, your local
nimbo installation will automatically update.
2. `pip install -r requirements/dev.txt` for installing all dependencies for development.

### Running Tests

Create two instance keys, one for `eu-west-1` and one for `us-east-2`. The keys should
begin with the zone name, e.g. `eu-west-1-dave.pem`. Do not forget to `chmod 400` the
created keys. Place these keys in `src/nimbo/tests/aws/assets`. 

Create a `nimbo-config.yml` file in `src/nimbo/tests/assets` with only the `aws_profile`,
`security_group`, and `cloud_provider: AWS`  fields set.

Make sure that the `security_group` that you put in test `nimbo-config.yml` allows
your IP for all regions, otherwise, the tests will fail.

Use `pytest` to run the tests
```bash
NIMBO_ENV=test pytest -x
```
