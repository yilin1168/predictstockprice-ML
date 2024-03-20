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
