# Sentiment Analysis for Mental Health

## Overview

This project classifies user-written texts into different mental health categories using machine learning and deep learning models. Two datasets were used:

* Small dataset (~50k rows) labeled by professionals.

* Large dataset (~600k rows) labeled based on subreddit categories.

Multiple models were developed, including classical machine learning models (Logistic Regression, XGBoost, Stacking) and a fine-tuned BERT model. The fine-tuned BERT model was deployed using Docker and AWS ECS (Fargate) with a Django + FastAPI web interface. User input and diagnosis data are stored in an AWS RDS database for future improvements.

## Project Structure
```
├── Data              # Datasets and descriptions
├── Deployment        # Docker and AWS deployment files
├── Notebooks         # Jupyter notebooks for data analysis and model training
├── django_proj       # Django and FastAPI web application, trained ML models
```

## Web Interface

* Frontend: Django-based UI

* Backend API: FastAPI

* Workflow:

    &nbsp;&nbsp;&nbsp;&nbsp;1. **User enters text** → Django sends it to FastAPI for classification.\
    &nbsp;&nbsp;&nbsp;&nbsp;2. **FastAPI predicts mental health category** and sends response back to Django.\
    &nbsp;&nbsp;&nbsp;&nbsp;3. **Django displays the result** to the user.\
    &nbsp;&nbsp;&nbsp;&nbsp;4. **User diagnosis** is collected and stored in AWS RDS.\

### Access the Web Application

The app can be reached from the following link:

[Visit Mental Health Detection App](http://my-ALB-1071292174.us-east-2.elb.amazonaws.com/predict)

## Future Improvements
*  Implement real-time feedback loops for continuous model improvement

## Author

Betul Senay Aras 

