import pandas as pd

# 由于不能直接读取用户上传的Excel文件，我们将模拟一个具有类似结构的DataFrame
# 模拟的DataFrame结构基于用户提供的图片
data = {
    ('Pos1', 'x1'): [0, 1],
    ('Pos1', 'x2'): [1, 0],
    ('Pos1', 'x3'): [0, 0],
    ('Pos2', 'x1'): [0, 1],
    ('Pos2', 'x2'): [1, 0],
    ('Pos2', 'x3'): [0, 0]
}

# 多级索引的模拟
index = pd.MultiIndex.from_tuples([('type1',), ('type2',)], names=['type'])

# 创建DataFrame
df_wide = pd.DataFrame(data, index=index)

# 重设索引，使得'type'也成为一个列
df_wide = df_wide.reset_index()

# 转换列名：合并多级列索引为单级索引
df_wide.columns = ['type'] + ['{}_{}'.format(pos, x) for pos, x in df_wide.columns[1:]]

# 使用pandas的melt函数将宽格式转换为长格式
df_long = pd.melt(df_wide, id_vars=['type'], var_name='Pos_x', value_name='value')

# 分割'Pos_x'列为'Pos'和'x'列
df_long[['Pos', 'x']] = df_long['Pos_x'].str.split('_', expand=True)

# 只保留'value'为1的行
df_long = df_long[df_long['value'] == 1]

# 丢弃'Pos_x'列，并调整列的顺序
df_long = df_long[['type', 'Pos', 'x', 'value']].reset_index(drop=True)

df_long


# 创建一个示例DataFrame
df = pd.DataFrame({
    'ID': [1, 2],
    'Day': ['Mon', 'Tue'],
    'Apple': [1, 2],
    'Banana': [3, 4],
    'Cherry': [5, 6]
})

# 指定id_vars
id_vars = ['ID', 'Day']

# 其他变量的列名
value_vars = [col for col in df.columns if col not in id_vars]

# 初始化一个空的DataFrame来存储结果
melted_df = pd.DataFrame()

# 遍历每一行
for i, row in df.iterrows():
    # 对当前行进行melt操作
    melted_row = pd.melt(df.loc[df.index == i], id_vars=id_vars, value_vars=value_vars,
                         var_name='Fruit', value_name='Value')
    # 将melt后的当前行追加到结果DataFrame中
    melted_df = pd.concat([melted_df, melted_row], ignore_index=True)

print(melted_df)










import pandas as pd

file_path = 'path/to/your/file.txt'  # 将此路径替换为您的文件路径

# 使用open函数打开文件
with open(file_path, 'r') as file:
    lines = file.readlines()

# 获取列名（假设第一行是列名）
column_names = lines[0].strip().split(',')

# 初始化一个空列表来存储非重复的数据行
data_rows = []

# 遍历每一行，除了第一行以外
for line in lines[1:]:
    # 如果当前行不是重复的列名行，则添加到data_rows列表中
    if line.strip() != ','.join(column_names):
        data_rows.append(line.strip().split(','))

# 使用列名和数据行创建DataFrame
df = pd.DataFrame(data_rows, columns=column_names)

print(df)













