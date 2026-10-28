# #بیش بردازش و اماده سازی دیتاست دیابت
# import pandas as pd
# import numpy as np
# df=pd.read_csv('./diabetes.csv')
# x=df.drop('Outcome',axis=1)
# y=df['Outcome']
# x=np.array(x)
# y=np.array(y)
# from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# x=scaler.fit_transform(x)
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# #مدل knn
# from sklearn.neighbors import KNeighborsClassifier
# knn=KNeighborsClassifier(n_neighbors=5)
# #اموزش مدل
# knn.fit(x_train, y_train)
# #ازمون مدل
# y_pred_train=knn.predict(x_train)
# y_pred_test=knn.predict(x_test)
# #ارزشیابی دقت مدل
# from sklearn.metrics import accuracy_score
# acc_train=accuracy_score(y_train, y_pred_train)
# acc_test=accuracy_score(y_test, y_pred_test)
# print(f'{int(round(acc_train,2)*100)}%\n{int(round(acc_test,2)*100)}%')
# from sklearn.metrics import recall_score,precision_score
# p= precision_score(y_test, y_pred_test)
# r,p=recall_score(y_test, y_pred_test), precision_score(y_test, y_pred_test)
# print(r,p)

c=12
print(ord(c))