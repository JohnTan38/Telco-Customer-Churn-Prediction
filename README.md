# Telco Customer Churn Prediction
<div align="center">

  <img src="https://github.com/JohnTan38/Zomato/blob/main/assets/logo.png" alt="logo" width="230" height="auto" />
  <h1>Awesome Machine Learning Project</h1>
  </div>
  <div align='center'>
  
<a href='https://github.com/chroline/well_app/releases'>
  
<img src='https://img.shields.io/github/v/release/chroline/well_app?color=%23FDD835&label=version&style=for-the-badge'>
  
</a>
  
<a href='https://github.com/chroline/well_app/blob/main/LICENSE'>

<img src='https://img.shields.io/github/license/chroline/well_app?style=for-the-badge'>
  
</a>
  
<a href='https://github.com/chroline/well_app/blob/main/LICENSE'>

<img src='https://img.shields.io/badge/-MIT-blue?style=for-the-badge'>
</a>
  
</div>
  
 # Table of Contents 🥳 🚀

- [About the Project](#star2-about-the-project)
  * [Project Objectives](#space_invader-tech-stack)
  * [Tech Stack](#dart-features)
  * [Exploratory Data Analysis](#key EDA)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Feature Engineering](#gear-installation)
  * [Streamlit](#running-run-locally)
- [Strategies to Counter Churn](#eyes-usage)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
  * [Code of Conduct](#scroll-code-of-conduct)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

# 🧐 Project Philosophy
The telco industry has an annual churn of 15-20%. Customer churn is a critical metric as it is more cost effective to retain existing customers than to acquire new ones.
## Objectives:
- Analyse the data in terms of various features responsible for customer Churn
- Develop an accurate machine learning model for correct classification of Churn and non churn customers.

# 👨‍💻 Tech stack
<h3 align="left">Libraries and Tools:</h3>
<p align="left"> <a href="https://azure.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a> </p>

# 🌟 EDA
### Tenure and Churn
> ![Tenure and Churn](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/Tenure%20and%20churn.PNG?raw=true)
<br>
> New customers are more likely to churn.<br>


### Distribution of Monthly Charges
> ![Monthly Charges](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/Charges%20distribution.PNG?raw=true)
> 
> ![Total Charges](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/Total%20charges.PNG)
> <br>
> Customers with higher Monthly Charges are also more likely to churn.<br>
> 
> ![Total Recurring Churn](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/TotalRecurChurn.PNG)
> <br>
> 
>   
> Customers with shorter tenure more likely to churn.<br>


### Pearson Ranking of Features
> ![Pearson Coefficient](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/Pearson.PNG?raw=true)<br>
> Monthly Revenue and Monthly Minutes are highly correlated. One of the variables could be dropped

### Feature Importances
> ![Feature Importances](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/Feature_Importances.PNG?raw=true)
> Monthly Revenue is an important feature

### Validation Curves
> ![Validation Curves](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/Validation_curve.PNG?raw=true)<br>
> CV Scores improve with greater depth of trees

### Intercluster Distances
> ![Intercluster Distances](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/Intercluster.PNG?raw=true)



## 	:toolbox: Getting Started
The solution is developed using Python 3.11 and Visual Studio Code with Python extensions
### :bangbang: Prerequisites

Install Libraries and dependencies

```bash
 pip install -r requirements.txt
```
### :gear: Installation

Feature Engineering and Dimensionality Reduction with PCA

```bash
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
```
## :eyes: Prediction
```bash
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)
```

## ✅&nbsp; Strategies to Counter Churn

* Engage customers before tenure reaches 24 months
* Customer Segmentation for targeted and effective customer retention marketing campaigns
* Match segments to comprehensive suite of mobile plans with various price plans


### K Means Clustering - Customer Segmentation
> ![Kmeans](https://github.com/JohnTan38/Python-Data-Analysis-/blob/main/images/Kmeans.PNG?raw=true)

# 🚀&nbsp; Streamlit - Interactive Machine Learning



> ![alt text](churndemo.gif "demo")
> 

### 🏃: Run Locally
```bash
pip install streamlit
streamlit run Stream_app.py

```
[![John's GitHub stats](https://github-readme-stats.vercel.app/api?username=johntan38&theme=dracula&show_icons=true)](https://github.com/johntan38/github-readme-stats)

# Contributors ✨
# Contributing

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

<h3 align="left">Support:</h3>
<p><a href="https://www.buymeacoffee.com/vieming8"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="buymeacoffeeJohnTan" /></a></p><br><br>


<br>
<a href="https://www.buymeacoffee.com/vieming8" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="50" width="210"></a>

