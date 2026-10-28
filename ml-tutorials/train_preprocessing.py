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
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(x_train,y_train)
y_pred_train=model.predict(x_train)
y_pred_test=model.predict(x_test)
from sklearn.metrics import accuracy_score, precision_score,recall_score
acc_train=accuracy_score(y_train,y_pred_train)
acc_test=accuracy_score(y_true=y_test, y_pred=y_pred_test)
print(f'{int(round(acc_test,2)*100)}%')
print(f'{int(round(acc_train,2)*100)}%')
p=precision_score(y_test, y_pred_test)
print(f'{int(round(p,2)*100)}%')
r= recall_score(y_test, y_pred_test)
print(f'{int(round(r,2)*100)}%')
from sklearn.metrics import confusion_matrix
c=confusion_matrix(y_test ,y_pred_test)
print(c)