# -*- coding: utf-8 -*-
"""Screen Time Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G4KVHLgTn_DRqtZZQkxcL9_r0XSDjYD9

# Screen Time Analysis using Python

Let’s start the task of screen time analysis by importing the necessary Python libraries and the dataset:
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("/content/Screentime-App-Details.csv")
print(data.head())

"""Now let’s have a look if the dataset has any null values or not:"""

data.isnull().sum()

"""The dataset doesn’t have any null values. Now let’s have a look at the descriptive statistics of the data:"""

print(data.describe())

"""Now let’s start with analyzing the screen time of the user. I will first look at the amount of usage of the apps:"""

figure = px.bar(data_frame=data,
                x = "Date",
                y = "Usage",
                color="App",
                title="Usage")
figure.show()

"""Now let’s have a look at the number of notifications from the apps:"""

figure = px.bar(data_frame=data,
                x = "Date",
                y = "Notifications",
                color="App",
                title="Notifications")
figure.show()

"""Now let’s have a look at the number of times the apps opened:"""

figure = px.bar(data_frame=data,
                x = "Date",
                y = "Times opened",
                color="App",
                title="Times Opened")
figure.show()

"""We generally use our smartphones when we get notified by any app. So let’s have a look at the relationship between the number of notifications and the amount of usage:"""

figure = px.scatter(data_frame = data,
                    x="Notifications",
                    y="Usage",
                    size="Notifications",
                    trendline="ols",
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()

"""There’s a linear relationship between the number of notifications and the amount of usage. It means that more notifications result in more use of smartphones.

# ***Summary***

So this is how we can analyze the screen time of a user using the Python programming language. Screen Time Analysis is the task of analyzing and creating a report on which applications and websites are used by the user for how much time.
"""