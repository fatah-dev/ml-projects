import pandas as pd
import numpy as np
df=pd.read_csv('./diabetes.csv')
x=df.drop('Outcome',axis=1)
y=df['Outcome']
x=np.array(x)
y=np.array(y)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x=scaler.fit_transform(x)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.neural_network import MLPClassifier
model=MLPClassifier(hidden_layer_sizes=100,max_iter=400)
model.fit(x_train,y_train)
y_pred_train=model.predict(x_train)
y_pred_test=model.predict(x_test)

from sklearn.metrics import accuracy_score,precision_score,recall_score
acc=accuracy_score(y_train, y_pred_train)
acc1=accuracy_score(y_test, y_pred_test)
pre=precision_score(y_train, y_pred_train)
pre1=precision_score(y_test, y_pred_test)
rec=recall_score(y_train, y_pred_train)
rec1=recall_score(y_test, y_pred_test)


print(acc,acc1,pre,pre1,rec,rec1)