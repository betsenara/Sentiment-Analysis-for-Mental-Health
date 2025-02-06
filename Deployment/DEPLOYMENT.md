# 🚀 Deployment Guide for Sentiment Analysis
This guide explains how to **build**, **push**, and **deploy** the Docker container to AWS.

## 1️ Build the Docker Image
Run the following command to build the Docker image:

```sh
docker-compose build --no-cache
```
## 2️. Tag and Push the Docker Images to AWS ECR
```sh
docker tag fastapi-app-amd64 $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME1:amd64
docker tag django-app-amd64 $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME2:amd64
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME1:amd64
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME2:amd64
```
## 3. Create a task-definition.json file and register it
```sh
aws ecs register-task-definition --cli-input-json file://task-definition.json
```
## 4. Create an ECS Cluster
```sh
aws ecs create-cluster --cluster-name my-cluster
```
## 5. Create an ECS Service
```sh
aws ecs create-service \
  --cluster my-cluster \
  --service-name my-service \
  --task-definition my-sent-analysis-app-task \
  --desired-count 1 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[<MY_SUBNET_ID>],securityGroups=[<MY_SECURITY_GROUP_ID>],assignPublicIp=ENABLED}"
```
## 6. Running Database Migrations
```sh
aws ecs execute-command --cluster <MY-CLUSTER-NAMES> --task <TASK_ID> --container django-app --command "python manage.py migrate" --interactive
```
## 7. Redeploy After Migrations 
```sh
aws ecs update-service --cluster my-cluster --service my-service --force-new-deployment
```
## 8. Create an Application Load Balancer (ALB)
After applying application load balancer the app can be reached from the following link:

[Visit Mental Health Detection App](http://my-ALB-1071292174.us-east-2.elb.amazonaws.com/predict)







