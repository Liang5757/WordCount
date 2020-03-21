from utils.count import *


# 输出字符数
def print_char_num(text):
    print(FileProperties(text).count_char_num())


# 输出单词数
def print_word_num(text):
    print(FileProperties(text).count_word_num())


# 输出行数
def print_line_num(text):
    print(FileProperties(text).count_line_num())


# 命令集
orders = {
    '-c': print_char_num,

    '-w': print_word_num,

    "-l": print_line_num,

    '-s': print("递归调用"),

    "-a": print("代码行/空行/注释行"),

    "-x": print("图像界面")
}
