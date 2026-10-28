import pandas as pd

df=pd.DataFrame({'name':['ali','babak','zahra','hasan','reza'],
      'age':[12,15,14,28,83],
      'birthday':[2000,2010,1990,1980,1920]})



df['family']=['fatah','hasani','rezai'
              ,'mamadi','sorani']
df.loc[len(df)]={'name':'maryam',
                 'age':38,'birthday':2003}
a=df.to_csv('newdata.csv')

df=df.drop('name',axis=1)

print(df)

