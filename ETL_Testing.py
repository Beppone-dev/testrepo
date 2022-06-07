import pandas as pd
import numpy as np
import datetime

var = "01234567"
print(var[::2])
print(var[::1])
print(var[::3])

Name="ABCDE"
print(Name.find("B"))

a=np.array([0,1,0,1,0])
b=np.array([1,0,1,0,1])
print(a*b)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "pippo": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

y = df[["calories","duration"]]

print(y)

a=np.array([1,1,1,1,1])
print(a+10)