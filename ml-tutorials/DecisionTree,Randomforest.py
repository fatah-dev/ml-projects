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

# DecisionTree
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(max_depth=8, min_samples_split=4, min_samples_leaf=2)
model=dt.fit (x_train,y_train)

#RandomForest
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=100, max_depth=8)
rf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix
y_pred_train_dt=dt.predict(x_train)
y_pred_train_rf=rf.predict(x_train)
acc_train_dt=accuracy_score(y_train, y_pred_train_dt)
acc_train_rf=accuracy_score(y_train,y_pred_train_rf)
print(acc_train_dt:.2f)#,acc_train_rf)
y_pred_test_dt=dt.predict(x_test)
y_pred_test_rf=rf.predict(x_test)
acc_test_dt=accuracy_score(y_test, y_pred_test_dt)
acc_test_rf=accuracy_score(y_test,y_pred_test_rf)
print(acc_test_dt,acc_test_rf)
