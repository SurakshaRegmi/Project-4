# Fraud Detection Model Performance Report

## Introduction

In this report, we evaluate the performance of a fraud detection classification model designed to predict fraudulent transactions in a financial dataset. 
The dataset consists of various transaction features, and the objective of the model is to accurately classify transactions as either fraudulent (class 1) or non-fraudulent (class 0).   
We'll analyze key metrics, including the confusion matrix and classification report, to assess the model's effectiveness in detecting fraud.  

## Data Overview

The dataset encompasses diverse features related to transactions, including transaction type, amount, time of day, balances before and after transactions, and more. The data is imbalanced, with a significantly larger number of non-fraudulent transactions compared to fraudulent ones.  

## Model Evaluation

## Model Features and Importance

The model utilizes a set of features to make predictions. The following features have been identified as important contributors to the model's decision-making process, along with their respective importance scores:  

- `newbalanceDest`: Importance - 0.177
- `trans_weight`: Importance - 0.169
- `oldbalanceDest`: Importance - 0.163
- `hour`: Importance - 0.100
- `oldbalanceOrg`: Importance - 0.098
- `step`: Importance - 0.079
- `day`: Importance - 0.065
- `amount`: Importance - 0.063
- `type_CASH_OUT`: Importance - 0.032
- `Destination`: Importance - 0.029

These features play a crucial role in the model's decision-making process when classifying transactions as fraudulent or non-fraudulent.  


### Confusion Matrix:

|                | Predicted Non-Fraud (0) | Predicted Fraud (1) |
|----------------|------------------------|---------------------|
| Actual Non-Fraud (0) | 538743                 | 13702               |
| Actual Fraud (1)     | 72                     | 1562                |

### Classification Report:

|                | Precision  | Recall     | F1-Score   | Support    |
|----------------|------------|------------|------------|------------|
| Non-Fraud (0)  | 0.999866   | 0.975198   | 0.987378   | 552445     |
| Fraud (1)      | 0.102332   | 0.955936   | 0.184874   | 1634       |
| Accuracy       | 0.975141   | 0.975141   | 0.975141   | 554079     |
| Macro Avg      | 0.551099   | 0.965567   | 0.586126   | 554079     |
| Weighted Avg   | 0.997220   | 0.975141   | 0.985011   | 554079     |

## Discussion

The confusion matrix reveals that the model has correctly identified a substantial number of non-fraudulent transactions (True Negatives: 538743) and a considerable number of fraudulent transactions (True Positives: 1562).  
However, it has also predicted some non-fraudulent transactions as fraudulent (False Positives: 13702) and some fraudulent transactions as non-fraudulent (False Negatives: 72).  

In terms of precision and recall, the model has a high precision for non-fraudulent transactions (99.99%) but a relatively low precision for detecting fraudulent transactions (10.23%). 
This indicates that while the model effectively identifies non-fraudulent transactions, it struggles with accurately detecting fraudulent transactions.  

The F1-score, which balances precision and recall, is higher for non-fraudulent transactions (0.987) compared to fraudulent transactions (0.185).  
The overall accuracy of the model is around 97.51%, which might be misleading due to the imbalanced nature of the dataset. The macro and weighted average metrics provide a more balanced perspective.  

## Conclusion

The classification model demonstrates a promising ability to identify non-fraudulent transactions with high accuracy and precision.  
However, it faces challenges in accurately detecting fraudulent transactions (class 1), with a relatively low precision and F1-score for that class. 
This suggests that the model might benefit from additional fine-tuning, feature engineering, or alternative algorithms to improve its performance on detecting fraudulent transactions.  

