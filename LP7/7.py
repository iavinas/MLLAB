import numpy as np
import pandas as pd

from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('heart.csv')
heartDisease = heartDisease.replace('?', np.nan)



print('Few examples from the dataset are given below')
print(heartDisease.head())
print('\nAttributes and datatypes')
print(heartDisease.dtypes)
# Model Bayesian Network
model = BayesianModel([ ('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'),
('sex', 'trestbps'), ('exang', 'trestbps'), ('trestbps', 'heartdisease'),
('fbs', 'heartdisease'), ('heartdisease', 'restecg'), ('heartdisease', 'thalach'),
('heartdisease', 'chol')])
# Learning CPDs using Maximum Likelihood Estimators

print('\nLearning CPDs using Maximum Likelihood Estimators...')
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
# Deducing with Bayesian Network
print('\nInferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)
print('\n1.Probability of HeartDisease given Age=20')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 40})
print(q)
print('\n2. Probability of HeartDisease given chol (Cholestoral) =250')

q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'sex': 0, 'chol': 250})
print(q)