# customer-churn-prediction-ml
End-to-end customer churn analysis and prediction project built using Python. Covers data cleaning, exploratory analysis, feature engineering, machine learning model training, and deployment through a Streamlit web application to support data-driven retention decisions.

### overview
This project simulates how a business analyst collaborates with data science workflows to translate customer data into actionable retention insights.

#### Why this project exists
Customer churn is not just a modeling problem.
It’s a business problem.
Instead of starting with algorithms, this project starts with a question:
Why are customers leaving, and how can data help prevent that?
This repository documents my end-to-end thinking process, from raw data to insights, predictions, and finally a simple web application that makes the results usable.
#### How I approached the problem
I treated this project the way a business analyst or data analyst would in a real organization.
Not jumping straight into machine learning, but moving step by step:
Understand the data and the business context
Clean and prepare the data so it can be trusted
Explore patterns and ask better questions
Engineer features that reflect real customer behavior
Train and compare machine learning models
Package the results in a form others can actually use

Each step builds on the previous one.

### Project workflow
### 1. Data Understanding
Before writing complex code, I focused on:
What each column represents
How customer behavior is recorded
What “churn” actually means in this dataset
This step shaped every decision that followed.
### 2. Data Cleaning
Clean data is not about perfection, it’s about reliability.
Here I handled:
Missing values
Inconsistent formats
Irrelevant or redundant columns
The goal was to create a dataset that reflects reality without introducing assumptions.
### 3. Exploratory Data Analysis
EDA was used to think, not just to plot charts.

### I explored
How churn varies across customer segments
Relationships between tenure, services, and churn
Early signals that separate churned vs retained customers
This step helped me move from “data” to “insights”.
### 4. Feature Engineering
Instead of blindly using all columns, I focused on:
Transforming raw fields into meaningful signals
Encoding customer behavior in a way models can learn from
Keeping features interpretable from a business perspective
Every feature has a reason to exist.
### 5. Machine Learning Models
Models were used as decision-support tools, not black boxes.
I:
Trained multiple models
Compared performance logically
Focused on interpretability and stability over complexity
The emphasis was on understanding why predictions are made, not just accuracy scores.
### 6. Streamlit Web Application
Insights are only useful if others can access them.
I built a simple Streamlit web app to:
Interact with the churn prediction model
Make results easy to explore
Simulate how analytics can be shared with non-technical users
This step turns analysis into something actionable.
### What this project demonstrates
  Structured, step-by-step analytical thinking
  Ability to translate business questions into data workflows
  Comfort working across the full data lifecycle
  Clear separation between analysis, modeling, and delivery
  This project reflects how I would approach real-world analytics work, not just an academic exercise.

### Tools used
Python (Pandas, NumPy)
Data visualization libraries
Machine learning models
Jupyter Notebook (VS Code)
Streamlit for deployment
