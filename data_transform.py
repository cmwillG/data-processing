''' 使用方法
==============
1. 1500测试数据的批量处理，可以将csv数据中的冗余部分清除，只保留表头和相关数据
2. 使用前请先在本机上安装python (https://www.python.org/downloads/ 或者 Anaconda)
2.1 如在python官网下载安装包，请在安装时勾选将python添加至PATH
3. 处理后的数据名与原始数据相同
4. 将csv文件放在同一文件夹下，保证该文件夹只有csv文件。更改原始数据地址与新数据存放地址后，点击运行即可
5. 推荐使用pycharm或vscode(需要插件)
6. 如有
'''

import csv
import os

def csv_import(new_file, import_file):
    with open(new_file, 'w') as newfile:
        writer = csv.writer(newfile)
        with open(import_file, encoding='UTF-8') as importfile:
            reader = csv.reader(importfile)
            for row in reader:
                if row[0]=='DataValue' or row[0]=='DataName':
                    row.pop(0)
                    writer.writerow(row)

# 单引号中添加原始数据的地址，windows系统需要将分隔符\更改为/
file_path = 'E:/GCM/data/20230803/idvg/'

data_list = os.listdir(file_path)

# 单引号中添加新数据的存放地址
for data_name in data_list:
    data = csv_import('E:/GCM/data/20230803/idvg-better/'+data_name, file_path+data_name)