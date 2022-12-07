Problem Statement and Business Problem Overview

In the telecom industry, customers are able to choose from multiple service providers and actively switch from one operator to another. In this highly competitive market, the telecommunications industry experiences an average of 15-25% annual churn rate. Given the fact that it costs 5-10 times more to acquire a new customer than to retain an existing one, customer retention has now become even more important than customer acquisition.

For many incumbent operators, retaining high profitable customers is the number one business goal.

To reduce customer churn, telecom companies need to predict which customers are at high risk of churn.

In this project, we analyse customer-level data of a leading telecom firm, build predictive models to identify customers at high risk of churn and identify the main indicators of churn.

Understanding and Defining Churn
There are two main models of payment in the telecom industry - postpaid (customers pay a monthly/annual bill after using the services) and prepaid (customers pay/recharge with a certain amount in advance and then use the services).

In the postpaid model, when customers want to switch to another operator, they usually inform the existing operator to terminate the services, and you directly know that this is an instance of churn.

However, in the prepaid model, customers who want to switch to another network can simply stop using the services without any notice, and it is hard to know whether someone has actually churned or is simply not using the services temporarily (e.g. someone may be on a trip abroad for a month or two and then intend to resume using the services again).

Thus, churn prediction is usually more critical (and non-trivial) for prepaid customers, and the term ‘churn’ should be defined carefully. Also, prepaid is the most common model in India and southeast Asia, while postpaid is more common in Europe in North America.


High-value Churn
In global telco markets, approximately 80% of revenue comes from the top 20% customers (called high-value customers). Thus, if we can reduce churn of the high-value customers, we will be able to reduce significant revenue leakage.

Understanding the Business Objective and the Data

The business objective is to predict the churn using Logistic Regression and RandomForest Classifier. To do this task well, understanding the typical customer behaviour during churn will be helpful.

Understanding Customer Behaviour During Churn
Customers usually do not decide to switch to another competitor instantly, but rather over a period of time (this is especially applicable to high-value customers). In churn prediction, we assume that there are three phases of customer lifecycle :

The ‘good’ phase: In this phase, the customer is happy with the service and behaves as usual.
The ‘action’ phase: The customer gets a compelling offer from a competitor, faces unjust charges, becomes unhappy with service quality etc. In this phase, the customer usually shows different behaviour than the ‘good’ months. Also, it is crucial to identify high-churn-risk customers in this phase, since some corrective actions can be taken at this point (such as matching the competitor’s offer/improving the service quality etc.)
The ‘churn’ phase: The customer is said to have churned. It is important to note that at the time of prediction, this data is not available to you for prediction. Thus, after tagging churn as 1/0 based on this phase, you discard all data corresponding to this phase.

Dataset and Data Dictionary
The dataset and Data Dictionary are included.

Solution
From the above problem statement, it's clear that this is a Binary Classification problem.

The solution is developed using Python 3.11 on VS Code with Python extensions and Jupyter Notebook.

The solution code is divided into the following sections:

Data understanding

Preprocessing

EDA

Handle missing and outliers values

Feature Engineering

Customer Churn Prediction

Feature Selection and Dimensionality Reduction using PCA
Baseline Model building
K-Fold Cross validation
Hyperparameter tuning
Model Evaluation
Model Selection with best parameters

Identifying Strong Predictors of churn (Important features)

Feature Selection with Feature Importances
Model building
Hyperparameter tuning with Cross Validation
Model Evaluation with accuracy, AUC, ROC scores, Precision and Recall

Strategy recommendation to manage customer churn
