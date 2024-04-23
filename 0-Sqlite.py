#Kdb+ receive
.z.ps: { show "Received data: ", string x; }




## insert to update sqlite(using dataframe)
import pandas as pd
import sqlite3

# 连接数据库
conn = sqlite3.connect('example.db')

# 创建DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
df = pd.DataFrame(data)

# 插入数据到数据库
df.to_sql('users', conn, if_exists='append', index=False)

# 关闭连接
conn.close()
