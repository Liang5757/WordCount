import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from utils.utils import read_file
from utils.count import *


class MainView(object):

    def __init__(self, window):
        self.window = window
        self.window.title("这是船新的版本！")
        self.window.geometry("540x290")
        self.data_tree = ttk.Treeview(self.window, show="headings")
        self.creat_view()

    def creat_view(self):
        # 选择文件按钮
        btn = tk.Button(self.window, text="选择文件", command=self.file_choose).place(x=240, y=247)

        # 文件数据显示表格
        self.data_tree.place(x=8, y=8)
        # 定义列
        self.data_tree["columns"] = ("文件名", "字符数", "单词数", "行数", "空行数", "代码行数", "注释行数")
        # 设置列属性，列不显示
        self.data_tree.column("文件名", width=100)
        self.data_tree.column("字符数", width=70)
        self.data_tree.column("单词数", width=70)
        self.data_tree.column("行数", width=70)
        self.data_tree.column("空行数", width=70)
        self.data_tree.column("代码行数", width=70)
        self.data_tree.column("注释行数", width=70)
        # 设置表头
        self.data_tree.heading("文件名", text="文件名")
        self.data_tree.heading("字符数", text="字符数")
        self.data_tree.heading("单词数", text="单词数")
        self.data_tree.heading("行数", text="行数")
        self.data_tree.heading("空行数", text="空行数")
        self.data_tree.heading("代码行数", text="代码行数")
        self.data_tree.heading("注释行数", text="注释行数")

        self.window.mainloop()

    def file_choose(self):
        file_list = tk.filedialog.askopenfilenames()
        for index, file in enumerate(file_list):
            text = read_file(file)
            [char_num, word_num, line_num, null_line_num, code_line_num,
             annotation_line_num] = FileProperties(text).all_count()
            file = file.split("/")[-1]
            self.data_tree.insert('', index, values=(file, char_num, word_num, line_num,
                                                     null_line_num, code_line_num, annotation_line_num))
