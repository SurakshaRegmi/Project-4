## Financial Fraud Analysis using Machine Learning
Detect fraudulent online transactions using different Machine Learning models, compare performances and come up with the best model that the investors(Banks) can invest on in order to predict fraudulent transactions and maintain the client's transaction secured and confidential.

In this project, we aim to explore three Machine Learning models training the dataset on 80% and testing on 20% to detect fraudulent transactions comparing three models performance and results. 

Please note that this approach can be transferred to other detection analysis in alternative domains. The feature extraction process remains similar and can be replicated on many other detection issues.

### Team Members
- Jeremy Oliver
- Micah Raquena
- Suraksha Regmi
- Tattwamasi Ray
----------------------
## Project Overview
- Customers Transaction Datasets Collection and Business Understanding
- Data Processing
- Exploratory Data Analysis
- Model Selection and Training
- Prior to modelling, we found the dataset available is unbalanced meaning that the fraudulent transactions were minimal compared to the non-fraudulent transactions. Thereby, to balance the dataset, we applied random undersampling that involved randomly selecting examples from the majority class to delete from the training dataset.
----------------------
## Summary of Findings
Three machine learning algorithms were used to train and test the dataset and were evaluated using different metrics for best performance. The best performance is achieved using random undersampling technique since the available dataset is unbalanced.
### MODEL 1 - Logistic Regression
- Method - Findings - Summary
### MODEL 2 - K-Nearest Neighbors
- Method - Findings - Summary
### MODEL 3 - Random Forest
- Method - Findings - Summary
### Conclusion
Upon training and evaluating our classification model, we found that the Random Forest model performed the best.

----------------------
## Project Files
### - Main Folder
- File: Description
### - Resources
- File: Description
### - Output Data
- [Fraud Data Summary](https://public.tableau.com/app/profile/micah.raquena.pequeno/viz/FraudDataSummary/FraudDataSummary?publish=yes)
----------------------
## Instructions - final APP
----------------------
Navigate to the repository for this project called Project4-Team6-Financial-Fraud-Analysis-using-Machine-Learning.

Connect the remote and local repositories through cloning .

Pull the particular project by running the “git pull” command.

Download the original dataset from https://www.kaggle.com/datasets/ealaxi/paysim1. 

Run the data fetch from jupyter notebook file. 

Run the files under Model to get the Machine Learning Models trained and tested.

Please note: 
- For Random undersampling - install imblearn library
- For the Visualisation, please check  [Fraud Data Summary](https://public.tableau.com/app/profile/micah.raquena.pequeno/viz/FraudDataSummary/FraudDataSummary?publish=yes)
