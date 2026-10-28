import numpy as np
import matplotlib.pyplot as plt
#from sklearn.tree import DesisionTreeRegressor
years_of_experience=np.array([0,1,2,3,4,6,8,10]).reshape(-1,1)
salaries= np.array([30000,40000,55000,60000,70000,80000,85000,87000])

plt.clf()
plt.plot(years_of_experience,salaries,'*')
plt.show()

# model=DesisionTreeRegressor(max_depth=2)
# model.fit(years_of_experience,salaries)
# y_predict=model.predict(years_of_experience)
# plt.plot(years_of_experience,y_predict)
# plt.show()