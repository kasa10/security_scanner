#%%
import winapps
import pandas as pd
#%%
df=pd.read_csv('test.csv',";")
#df2=pd.read_excel('test2.xlsx', index_col=0) #

#%%
apps = []
for app in winapps.list_installed():
    apps.append([app.name, app.version])

#%%
#x=[]
for i in range(0,len(df['ID'])):
    for n in range(0,len(apps)):
        if df['Name'][i]==apps[n][0]:

            if df['Желательное'][i]==0:
                print(df['Name'][i],'|| Является нежелательным ПО || Рекомендация: ', df['Рекомендация'][i])
                print('Уровень опасности: ', df['Уровень опасности'][i])
                continue

            if df['Версия ПО'][i]!=apps[n][1]:
                print(df['Name'][i], '|| Версия ПО уязвима || Рекомендация: ', df['Рекомендация'][i])
                print('Уровень опасности: ', df['Уровень опасности'][i])
                continue
