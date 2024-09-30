# Import packages
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

 #set the size of our plots as they are a little small by default.
plt.rcParams["figure.figsize"] = (20,5)

#import dataset
df = pd.read_csv(r'/home/user/Data Science Projects/Taxi/Predicting-car-insurance-cost-throughcollision-risk-through-machine-learning-/LBD_New_York_collisions_and_weather_data.csv')
df.head()
display(df.head())

