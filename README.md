# Chicken-Disesase-Classifier

## Introduction

Welcome to the Chicken Disease Classifier project! This is an end-to-end deep learning project using MLOps DVC pipeline, showcasing deployments on AWS platforms. The project aims to classify images of chickens based on various diseases they might have, thereby enabling early detection and effective disease management.

### Project Overview

The Chicken Disease Classifier project covers the following key components:

1. Data Ingestion: Loading and preparing the dataset for training and validation.
2. Data Validation: Ensuring the integrity and quality of the dataset.
3. Model Training: Training a deep learning model using the prepared dataset.
4. Model Evaluation: Evaluating the trained model's performance and accuracy.
5. Web Application: Creating a Flask-based web application for image classification.
6. Deployment: Deploying the trained model on Azure and AWS platforms.

- Throughout the project, we'll emphasize modular coding, configuration management, and the use of MLOps tools like DVC for efficient pipeline execution and version control.

# Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- TensorFlow (version 2.x)
- Keras (version 2.x)
- Flask (version 2.x)
- DVC (Data Version Control)
- Docker (for AWS deployment)
- AWS Account (for AWS deployment)

# Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the Configuration Manager in src/config
6. Update the Components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/entbappy/Chicken-Disease-Classification--Project
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up you local host and port
```

### DVC cmd

```
1. dvc init
2. dvc repro
3. dvc dag
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

### with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws

### Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

### Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
