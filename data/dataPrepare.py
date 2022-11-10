import numpy as np
import pandas as pd

'''
    操作1：
    找到check-in大于10的用户序列
    建立一个新的表格
'''
# df1 = pd.read_csv('data_CAL.csv')
#
# new1 = df1.groupby(['User_id']).size()
# df2 = pd.DataFrame(new1) #记录了每个用户的访问poi数
# df2.rename(columns={0:'counts'},inplace=True)
# print(df2.count())
#
# #查找check-in数大于10的用户序列
# userGbycounts = df2[df2.counts>10].copy()
# user_list = []  #用来记录check-in条数大于10的用户id
# tmp = []
# for k, v in userGbycounts.iterrows():
#     for row in df1.itertuples():
#         if k == row.User_id:
#             if k not in user_list:
#                 user_list.append(k)
#
# print(user_list)
# new_data = []
# for i in user_list:
#     for index ,row in df1.iterrows():
#         if i == row.User_id:
#             new_data.append(row)
#
# new_data = np.array(new_data)
# print(new_data)
#
# #['Location_id', 'POI_id', 'POI_Type', 'Org_id', 'User_id', 'TimeStamp', 'Zone', 'Latitude', 'Longitude', 'Subcategory', 'yelp_id', 'stars', 'Local_sg_time'])
# new_CAL_data = pd.DataFrame(data=new_data, columns=['Location_id', 'POI_id', 'POI_Type', 'Org_id', 'User_id', 'TimeStamp', 'Zone', 'Latitude', 'Longitude', 'Subcategory', 'yelp_id', 'stars', 'Local_sg_time'])
#
# new_CAL_data.to_csv("new_CAL_data.csv", index= False, header=df1.columns)

'''
    操作2：
    增加字段：
    Time：具体的时间信息 hh:mm:ss
    weekend：是否是周末 1是 0否
    Date：日期 yyyymmdd
    new_time：几点钟 hh
'''
# df3 = pd.read_csv("new_CAL_data.csv")
#
# Time = []
# weekend = []
# for t in df3['TimeStamp']:
#     Time.append(t[11:19])
#     if t[0:3] == 'Sun' or t[0:3] == 'Sat':
#         weekend.append(1)
#     else:
#         weekend.append(0)
# df3['Time'] = Time
# df3['weekend'] = weekend
#
# Date = []
# new_time = []
# for t in df3['Local_sg_time']:
#     t = t.split('/')
#     Date.append(t[2][0:4]+t[1]+t[0])
#     t[2] = t[2].split()
#     t[2][1] = t[2][1].split(':')
#     new_time.append(t[2][1][0])
# df3['Date'] = Date
# df3['new_time'] = new_time
#
# df3 = df3.drop(columns='week') #记得用df3接住你的操作
# df3.to_csv("new_CAL_data.csv", index = False)

'''
    操作3：
    增加字段： cluster 简化org_id位置信息，将其分为不同区域
    修改column名： POI_id -> Item_id
    修改POI_type： Independent：0， combine：1
    增加字段POI ： Independent ， combine
    统计总共访问的次数，记录为counts
'''
df = pd.read_csv("new_CAL_data.csv")

cluster = []
org_id = {}
POI_type = []
index = 0
for k, v in df.iterrows():
    if v.Org_id not in org_id:
        org_id[v.Org_id] = index
        index += 1
    if v.POI_Type == 'Independent':
        POI_type.append(0)
    else:
        POI_type.append(1)

for o in df['Org_id']:
    cluster.append(org_id[o])

df.rename(columns={'POI_id':'Item_id', 'POI_Type' : 'POI'}, inplace=False)

df['cluster'] = cluster
df['POI_Type'] = POI_type

user = []
time =[]
for k, v in df.iterrows():
    if v.POI_id == 54:
        user.append(v.User_id)
        time.append(v.Local_sg_time)
test54 = pd.DataFrame()
test54['user'] = user
test54['time'] = time
print(test54)
