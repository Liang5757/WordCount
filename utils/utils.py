import re
import os
from utils.orders import *


# description：parse command
# param：order input
# return：[order, [file_list]] / FALSE
def parse_command(command):
    command = command.strip().split(" ")

    # 指令若为空或者起始不为wc.exe则报错
    if command == [] or command[0] != "wc.exe":
        print("指令输入错误")

    # 打开图形界面的指令(一级指令)
    if "-x" in command:
        orders.get("-x")()
    elif len(command) > 2:
        order = command[-2]
        file_name = command[-1]
        file_list = get_file_list(file_name)

        # 递归调用的指令
        if "-s" in command:
            if file_list:
                for file_name in file_list:
                    print(file_name + ":")
                    text = read_file(file_name)
                    orders.get(order)(text)
        else:
            print(file_list[0] + ":")
            text = read_file(file_name)
            orders.get(order)(text)
    else:
        print("指令输入错误")


# 读取目录下符合条件的文件名
def get_file_list(file_name):
    # 最终构建的文件列表
    file_list = []
    # 匹配到的文件夹列表、需二次处理
    dir_list = []

    file_name = file_name.replace("?", "\\S").replace("*", "\\S+")
    file_name += "$"

    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if re.match(file_name, name):
                file_list.append(os.path.join(root, name))
        for name in dirs:
            if re.match(file_name, name):
                dir_list.append(os.path.join(os.getcwd() + os.sep, name))

    # 如果文件夹非空，则继续收集
    if dir_list:
        for item in dir_list:
            all_file = os.listdir(item)
            for file in all_file:
                # 文件的完整路径
                file_path = item + os.sep + file
                if os.path.isfile(file_path):
                    file_list.append(file_path)

    return file_list


# description：read files
# param：file_list
# return：file content
def read_file(file):
    with open(file, 'r') as f:
        return f.readlines()
