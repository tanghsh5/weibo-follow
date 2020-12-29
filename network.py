import networkx as nx
import matplotlib.pyplot as plt
import os
import pandas as pd

# 显示中文，即字体设置
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

# 文件路径
file_dir = os.path.split(os.path.realpath('__file__'))[0]
file_path = file_dir + os.sep + 'user_follow_list.csv'
# 读取文件
df = pd.read_csv(file_path, header=None)
df.columns = ['follow_id', 'follow_name', 'user_id', 'user_name']
print(df.head())

plt.figure(figsize=(20, 20))
G = nx.Graph()

for index in df.index:
    G.add_edge(df.follow_name[index], df.user_name[index])

nx.draw(G,
        node_color='b',
        edge_color='r',
        with_labels=True,
        font_size=10,
        node_size=5)
plt.savefig('network.png')
plt.show()

