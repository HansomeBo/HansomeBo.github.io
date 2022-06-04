import random
import time


start_time=(2017, 1, 1, 0, 0, 0, 0, 0, 0)
end_time=(2021, 12, 30, 23, 59, 59, 0, 0, 0)
start = time.mktime(start_time)  # 生成开始时间戳
end = time.mktime(end_time)  # 生成结束时间戳
t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
date_touple = time.localtime(t)  # 将时间戳生成时间元组
date = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串
print(date)