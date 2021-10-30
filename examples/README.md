# Publish-Subscribe Examples

## Basic example

### Overview

Runs a publisher along with two subscribers: a producer that publishes data and a consumer that subscribes to it.

### Usage

Run the following commands from the root directory, each as its own process:

```shell
pipenv run python run_publisher.py -c examples/basic/publisher.yml
```

```shell
pipenv run python run_subscriber.py -c examples/basic/producer.yml
```

```shell
pipenv run python run_subscriber.py -c examples/basic/consumer.yml
```
