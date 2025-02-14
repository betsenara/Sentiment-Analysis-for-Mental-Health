# Machine Learning Life Cycle: Sentiment Analysis for Mental Health Detection

## 1. Problem Statement
Mental health issues are increasing, and early detection can significantly impact intervention efforts. This project aims to classify user-written text into different mental health categories to assist in identifying mental health conditions using machine learning models.

## 2. Data Collection and Preprocessing
### **Datasets Used**
- **Dataset 1 (~50k rows)**: Professionally labeled mental health data.
- **Dataset 2 (~600k rows)**: Labels derived from subreddit discussions.

### **Preprocessing Steps**
- Data Cleaning (removal of noise, special characters, unnecessary spaces, removal of rows with non-English texts)
- Tokenization and Lemmatization
- Stopword Removal
- Feature Engineering (TF-IDF, Word2Vec, BERT embeddings)

## 3. Exploratory Data Analysis (EDA)
- **Label Distribution Analysis**: Visualizing class imbalance
- **Word Clouds**: Identifying common words for each category
- **Text Length Analysis**: Understanding word count distributions per class
- Cosine similarity analysis with Word2Vec

## 4. Model Selection and Training


### **Baseline Machine Learning Models**
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- Stacking Classifier (combining Logistic Regression, Linear SVC, Naive Bayes, Random Forest, and XGBoost)

**Hardware Used:** CPU with 24 cores

### **Deep Learning Model**
* Fine-tuned BERT model trained separately on both datasets
  
**Hardware Used:** NVIDIA RTX GPU 4070 



### **Evaluation Metrics**
- Accuracy, Precision, Recall, F1-score
- Confusion Matrix for error analysis

### Model Performance Comparison

| Model                | Accuracy | Precision | Recall | F1-Score |
|----------------------|----------|-----------|--------|----------|
| Logistic Regression  | 0.74     | 0.75      | 0.74   | 0.74     |
| Linear SVC           | 0.74     | 0.75      | 0.74   | 0.74     |
| XGBoost              | 0.76     | 0.76      | 0.76   | 0.76     |
| Random Forest        | 0.73     | 0.73      | 0.73   | 0.73     |
| Stacking Classifier  | 0.77     | 0.77      | 0.77   | 0.77     |
| Fine-Tuned BERT      | 0.83     | 0.83      | 0.83   | 0.83     |

## 5. Model Deployment
### **Containerization with Docker**
- **FastAPI container**: Handles ML model inference
- **Django container**: Frontend for user interaction

### **Local Deployment**
- **Generate local images**:
```
docker-compose build --no-cache
```
- **Run locally**: 
```
docker-compose up
```

### **Cloud Deployment on AWS**
- **ECS (Fargate)** for scalable inference
- **AWS RDS** for storing user input and diagnosis feedback
- **Application Load Balancer (ALB)** for external access

## 6. User Interaction & Feedback Collection
- **User submits text input** through the Django-based web interface
- **FastAPI processes input** and predicts a mental health category
- **Django displays results** to the user
- **User diagnosis feedback** is stored in AWS RDS to improve future models

### **Live Demo**
[Visit Mental Health Detection App](http://my-ALB-1071292174.us-east-2.elb.amazonaws.com/predict)

## 7. Future Improvements
- **Further optimize BERT fine-tuning** for better accuracy
- **Enhance model explainability** with SHAP/LIME analysis
- **Expand dataset** with additional labeled sources
- **Implement real-time feedback loops** to improve model generalization

## Conclusion
This document outlines the complete **Machine Learning Life Cycle** for mental health text classification, covering **problem definition, data preparation, modeling, deployment, and future improvements**.

