import pandas as pd
import wps

import os
# 获取当前目录
current_directory = os.getcwd()
# 构建文件名
filename = "1234.xlsx"
# 构建完整的文件路径
file_path = os.path.join(current_directory, filename)
# 检查文件是否存在
if os.path.isfile(file_path):
    print(f"文件 {filename} 存在.")

else:
    print(f"文件 {filename} 不存在.")
