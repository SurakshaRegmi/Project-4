# Logistic Regression Model Analysis

This section provides a comprehensive analysis of the Logistic Regression model's performance in detecting fraudulent transactions.  
The evaluation is based on the provided confusion matrix, classification report, accuracy, and key features.

## Confusion Matrix

The confusion matrix summarizes the model's predictions:

|               | Predicted Non-Fraud (0) | Predicted Fraud (1) |
|---------------|------------------------|---------------------|
| Actual Non-Fraud (0) | 475217                 | 77228                 |
| Actual Fraud (1)     | 314                  | 1320                |

## Classification Report

The classification report presents precision, recall, and F1-score for each class:

|     | Precision | Recall | F1-Score | Support |
|-----|-----------|--------|----------|---------|
| 0   | 0.999     | 0.860  | 0.925    | 552445  |
| 1   | 0.017     | 0.808  | 0.033    | 1634    |
|     |           |        |          |         |
| Accuracy | 0.860     |        |          | 554079  |
| Macro Avg| 0.508     | 0.834  | 0.479    | 554079  |
| Weighted Avg| 0.996  | 0.860  | 0.922    | 554079  |

## Accuracy

The accuracy of the model is 0.860, indicating that approximately 86.0% of instances are correctly predicted.  

## Key Features

The model's performance relies on the following features:

- 'step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFlaggedFraud', 'hour', 'day', 'week', 'trans_weight', 'bal_change_per', 'large_transaction', 'type_CASH_OUT', 'type_TRANSFER', 'Destination'

## Conclusion

- The model excels in accurately identifying non-fraudulent transactions (class 0) with high precision.  
- Precision for fraudulent transactions (class 1) is notably low, leading to a relatively low F1-score for this class.  
- The model's recall for fraudulent transactions is relatively better, indicating successful detection of a substantial portion of actual fraudulent cases.  
- The model's accuracy may be influenced by class imbalance, favoring the majority class.    
- Further exploration of feature engineering, model tuning, and techniques for handling imbalanced data could potentially enhance the model's ability to detect fraudulent transactions.  
