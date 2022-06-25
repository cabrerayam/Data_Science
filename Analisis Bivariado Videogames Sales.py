# -*- coding: utf-8 -*-
"""Ejemplo 2 - Análisis Bivariado de Datos (CoderHouse).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14HRkElmbwELL0FNEYjW-fWvwyOd8WAp9
"""

#Importamos las librerias
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import pandas_profiling

#Importemos el archivo
vg_df = pd.read_csv('C:/Users/Layla/Desktop/Docencia/Coder House/Materiales complementarios/Mod 4 - Data Science/4. Análisis Bivariado/Datos/Video_Games_Sales_as_at_22_Dec_2016.csv')

#Head del df
vg_df.head()

#Veamos el shape
vg_df.shape

#Totalidad de registros por columnas
vg_df.count()

#Tipo de dato de cada columna
vg_df.dtypes

#Principales medidas estadisticas
vg_df.describe().T

#Data Profiling
profile = pandas_profiling.ProfileReport(vg_df)
profile

#Correlaciones
plt.figure(figsize=(12, 8))

vg_corr = vg_df.corr()
sns.heatmap(vg_corr, 
            xticklabels = vg_corr.columns.values,
            yticklabels = vg_corr.columns.values,
            annot = True);

#Ejemplo: Categórica vs. categórica
pd.crosstab(vg_df.Genre, vg_df.Rating)

pd.crosstab(vg_df.Genre, vg_df.Rating, normalize=True) #Agregamos los valores en relativo

#Análisis de numérica vs. categórica
vg_df.groupby('Genre')['Global_Sales'].mean()

vg_df.groupby('Genre')['Critic_Score'].mean()

vg_df.groupby('Genre')['EU_Sales'].mean()

vg_df.groupby('Genre')['EU_Sales'].mean().sort_values(ascending=False) #Ordenamiento descendiente

vg_df.groupby('Genre')['Critic_Score'].describe()

#Boxplot
plt.figure(figsize=(20,20)) #defino el tamaño del grafico
sns.boxplot(y = 'Critic_Score', x = 'Genre', data = vg_df)
plt.show()