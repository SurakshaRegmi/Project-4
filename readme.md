![Alt text](<4. Output/4.1 Data Analysis/Title.jpg>)

# Financial Fraud Analysis using Machine Learning
This project explores multiple machine learning methods to detect fraud.  
After creating a final modal (random forest)- this project builds an app which can be used to detect fraud at the transaction level .  
Whilst the focus is using the random-forest model, the App provides a process to use various models. 
  
This project uses the following: 
- Tableau for data and model visualisation
- Pandas , Matplotlib and Scikit-learn
- Flask App to visualise data prediction

### Team Members
- Jeremy Oliver
- Micah Raquena-Pequeno
- Suraksha Regmi
- Tattwamasi Ray
----------------------
## Project Folder Overview
- 1. Data Fetch  
- 2. Model Training
- 3. Application
- 4. Output - Model Analysis and Visualisations
- 5. Resources - data csv
----------------------
## Summary of Findings
### Fraud Data Summary [tableau link](https://public.tableau.com/app/profile/micah.raquena.pequeno/viz/FraudDataSummary/FraudDataSummary?publish=yes).   
Original data had over 6 million transactions over one month for a foreign nation.  
The data showed the total fraud transactions to be 8,213 with a total amount of $12b. The average fraud transaction is $1.47 million of the currencty. 
Of all transactions < 1% were fraud .  
Only Cash Out and Transfer were relevant transactions in the data set in predicting fraud.   
We identified that splitting by transaction type could drop non-relevant transactions.  
`Class Imbalance` Due to the imbalance of the classes - we used random undersampling of the model.

![Alt text](<4. Output/4.1 Data Analysis/data_summary.jpg>)

### Final Model Evaluation [tableau link](https://public.tableau.com/app/profile/micah.raquena.pequeno/viz/FraudDataSummary/ModelSummary?publish=yes).    
Our final model had a 97.5% accuracy rate - whilst the confusion matrix had a high false positive (outweighs true positive) - we found that this was in line with a financial institutions risk appetite.
Our priority in the model was to reduce the number of False Negatives - which in this case we reduced to 0.01%.
Of transactions Non-flagged for fraud - 0.01% was true fraud.  
Of transactions Flagged for fraud 10.2% were true frad wheras 89.8% were false positives.   
The model can prevent up to 95.6% of all fraudulent transactions- which is estimated to be up to $691 B over a year. 

 
![Alt text](<4. Output/4.2 Model Analysis/Model Evaluation.jpg>)

### Random Forest - Confusion Matrix:

|                | Predicted Non-Fraud (0) | Predicted Fraud (1) |
|----------------|------------------------|---------------------|
| Actual Non-Fraud (0) | 538743                 | 13702               |
| Actual Fraud (1)     | 72                     | 1562                |

### - Classification Report:

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
The overall accuracy of the model is around 97.51%, which might be misleading due to the imbalanced nature of the dataset. 
The macro and weighted average metrics provide a more balanced perspective.  

### Conclusion
The overall model decided for this project is the Random Forest model.
The classification model demonstrates a promising ability to identify non-fraudulent transactions with high accuracy and precision.  
However, it faces challenges in accurately detecting fraudulent transactions (class 1), with a relatively low precision and F1-score for that class.  
This suggests that the model might benefit from additional fine-tuning, feature engineering, or alternative algorithms to improve its performance on detecting fraudulent transactions.  


----------------------
## Instructions - Building the model App
----------------------
- 1. Data fetch.  

    Clone repository to local device and run virtual environment. 
    Run pip install - command in gitbash for the following:
    imblearn, jupyter , sklearn, pickle

    Download data csv from [kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1)  and save under `5.Resources` as csv name.  From folder 1. run jupyter notebook "1.1 fraud_data_fetch.ipynb".  
    Readomg from the data csv this model cleans the data by: removing transactions with 0 amount; only includes transaction types which may include fruad, uses random undersampling to address the class imbalance issue in the data set- as < 1% of data is fraud.
    The data should print csv `fraud_det_dig_df.csv` into 5.Resources folder.
    

- 2. Model training.

    3 files are created to use random undersampling for our data set and run various models including K-NN , Logistic Regression and Random forest. 
    Run each file to get an overview of each model.  
    This project uses Random Forest training and file `2.3 mod_random_forest.ipynb` creates a model named model.pkl and saves under `3. Application folder` .

- 3. App - flask App
    Ensure the model is saved under folder `3. App` . 
    Use git command flask run.  
    The app will prompt used to key in data 
 
- 4. Output
    4.1 Visualises data from initial model to undertand distribution 
    4.2 Model analysis evaluates each of the models trained. 

## Demonstartion of Flask App 
![Alt text](<4. Output/4.2 Model Analysis/Flask App.jpg>)