# -*- coding = utf-8 -*-
# Time: 2022/4/18 23:28
# Author: Mr Wu
# File: 3.traceback模块.py
# Software: PyCharm

# 使用traceback模块打印异常信息
import traceback
try:
    print('------------------')
    print(10/0)
except:
    traceback.print_exc()