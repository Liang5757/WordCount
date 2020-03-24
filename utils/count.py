import re


class FileProperties(object):

    def __init__(self, file_text):
        self.file_text = file_text
        # 字符数
        self.char_num = 0
        # 单词数
        self.word_num = 0
        # 行数
        self.line_num = len(file_text)
        # 空行
        self.null_line_num = 0
        # 代码行
        self.code_line_num = 0
        # 注释行数
        self.annotation_line_num = 0

    # 计算字符数
    def count_char_num(self):
        for line in self.file_text:
            self.char_num += len(line.strip())

        return self.char_num

    # 计算单词数
    def count_word_num(self):
        for line in self.file_text:
            # 正则匹配一行中的所有单词，并计算单词数
            self.word_num += len(re.findall(r'[a-zA-Z0-9]+[\-\']?[a-zA-Z]*', line))

        return self.word_num

    # 计算行数
    def count_line_num(self):

        return self.line_num

    # 计算空行数
    def count_null_line_num(self):
        for line in self.file_text:
            # 只有不超过一个可显示的字符
            if len(re.findall(r'\S', line)) <= 1:
                self.null_line_num += 1

        return self.null_line_num

    # 计算代码行
    def count_code_line_num(self):
        return self.line_num - self.null_line_num - self.annotation_line_num

    # 计算注释行
    def count_annotation_line_num(self):
        flag = 0
        for line in self.file_text:
            line = line.strip()
            # 匹配不是代码行且有//
            if re.match(r'^\S?\s*?\/\/', line):
                self.annotation_line_num += 1
            # 匹配不是代码行且有/*
            elif re.match(r'^\S?\s*?\/\*', line):
                flag = 1
                self.annotation_line_num += 1
                if line.endswith('*/'):
                    flag = 0
            elif flag == 1:
                self.annotation_line_num += 1
            elif "*/" in line:
                self.annotation_line_num += 1
                flag = 0

        return self.annotation_line_num
