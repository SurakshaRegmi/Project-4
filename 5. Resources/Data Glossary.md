## Glossary

"Synthetic Financial Datasets For Fraud Detection"
[Kaggle Data Source](https://www.kaggle.com/datasets/ealaxi/paysim1)

### y Class
- isFraud: Indicates whether the transaction is associated with fraudulent behavior. In this dataset, fraudulent transactions involve agents attempting to take control of customer accounts and siphon funds through transfers and cash-outs.

### Independent Variables

- Step: A unit of time in the real world. In this simulation, each step represents one hour. The total number of steps is 744, equivalent to 30 days.

- Type: Denotes the type of transaction, which could be one of the following: CASH-IN, CASH-OUT, DEBIT, PAYMENT, and TRANSFER.

- Amount: The value of the transaction in the local currency.

- nameOrig: The customer who initiated the transaction.

- oldbalanceOrg: The initial balance of the originator's account before the transaction.

- newbalanceOrig: The new balance of the originator's account after the transaction.

- nameDest: The recipient of the transaction.

- oldbalanceDest: The initial balance of the recipient's account before the transaction. Not applicable to accounts starting with 'M' (Merchants).

- newbalanceDest: The new balance of the recipient's account after the transaction. Not applicable to accounts starting with 'M' (Merchants).

- isFlaggedFraud: Part of the business model aimed at identifying suspicious transactions. Transactions are flagged as fraudulent attempts if they involve transferring more than 200,000 in a single transaction.
