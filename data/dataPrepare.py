import numpy as np
import pandas as pd

df1 = pd.read_csv('data_CAL.csv')

#print(df1.loc[:,'Local_sg_time'])
#
# for i in range(df1.size):
#     print(df1.loc[i,'Local_sg_time'])

new1 = df1.groupby(['User_id']).size()
df2 = pd.DataFrame(new1) #记录了每个用户的访问poi数
df2.rename(columns={0:'counts'},inplace=True)

count_list = df2['counts'].tolist()


if df2.loc[:,'counts'] < 10:
    df2.drop('')
print(df2)