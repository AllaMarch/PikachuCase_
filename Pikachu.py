import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('Pikachu.csv', sep=';', header = 0)
data.describe()
data.info()
data.Person = data.Person.astype('category')
data.Pockemon = data.Pockemon.astype('category')
data.info()

data.sample()
