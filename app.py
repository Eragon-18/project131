import pandas as pd 
import csv 

df = pd.read_csv('final.csv')

m = []
for i in df['Mass']:
    a = i * 1
    b = float(a)
    m.append(b * 1.989e+30)

r = []
for j in df['Radius']:
    c = j * 1
    d = float(c)
    r.append(d * 6.957e+8)

df['Mass'] = m
df['Radius'] = r

g = []
for i in range(1,97):
    gval = float(df['Mass'][i - 1]) * 6.674e-11 / (float(df['Radius'][i - 1])**2)
    g.append(gval)

df['Gravity'] = g

# create a new csv from df
df.to_csv('131final.csv', index=False)