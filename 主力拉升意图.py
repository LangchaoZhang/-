import tushare as ts
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
mpl.use('TKAgg')
import numpy as np
import pandas as pd
import csv
import datetime
import pymysql
ts.set_token("1f64f4e4ed9c693072f02f20f56ea73323c6e0891f714d7ddef8bacf")
pro = ts.pro_api()
df = pro.daily(ts_code='002229.SZ', start_date='20230721', end_date='20230807')
print(df)
print(df.trade_date,df.close)
# 需要参数可以打点调用
sns.set(font="Arial Unicode MS",rc={'figure.figsize':(5,3)})
( (df.close).iloc[0]/df.close).plot()
plt.show()
# 第零阶段：吸筹阶段
# 第一阶段：第一波上涨容易被忽略

# 第二阶段：第一次调整时间较长，让人以为随时新低
# 第三阶段：第二波上涨，突破后加速
# 第四阶段：第二波洗盘，时间段，幅度深
# 第五阶段：快速拉升，吸引注意，边拉边出货
