from utils.count import FileProperties


# 输出字符数
def print_char_num(text):
    print("字符数：" + str(FileProperties(text).count_char_num()))


# 输出单词数
def print_word_num(text):
    print("词数：" + str(FileProperties(text).count_word_num()))


# 输出行数
def print_line_num(text):
    print("行数：" + str(FileProperties(text).count_line_num()))


# 输出代码行/空行/注释行
def print_code_property(text):
    file_properties = FileProperties(text)

    print("空行：" + str(file_properties.count_null_line_num()))
    print("注释行：" + str(file_properties.count_annotation_line_num()))
    print("代码行：" + str(file_properties.count_code_line_num()))


# 调出图形界面
def draw_view():
    import tkinter as tk
    from views.main_view import MainView

    root = MainView(tk.Tk())


def print_error():
    print("指令输入错误")


# 单指令命令集
orders = {
    '-c': print_char_num,

    '-w': print_word_num,

    "-l": print_line_num,

    "-a": print_code_property,

    "-s": print_error,

    "-x": draw_view
}
