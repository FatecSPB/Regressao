import pandas as pd

d = {'y': [6,10,20,40], 'x1': [8,6,14,20], 'x2': [0,1,2,1]}
con = pd.DataFrame(data=d)

cormat = con.corr()
print(cormat)