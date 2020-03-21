import re


class FileProperties(object):

    def __init__(self, file_text):
        self.file_text = file_text
        # 字符数
        self.char_num = 0
        # 单词数
        self.word_num = 0
        # 行数
        self.line_num = 0
        # 代码行
        self.code_line_num = 0
        # 空行
        self.null_line_num = 0
        # 注释行数
        self.annotation_line_num = 0

    # 计算字符数
    def count_char_num(self):
        for line in self.file_text:
            self.char_num += len(line.strip())

        return self.char_num

    # 计算单词数
    def count_word_num(self):
        word_num = 0
        for line in self.file_text:
            # 正则匹配一行中的所有单词，并计算单词数
            word_num += len(re.findall(r'[a-zA-Z]+[\-\']?[a-zA-Z]*', line))

        return word_num

    # 计算行数
    def count_line_num(self):
        self.line_num = len(self.file_text)

        return self.line_num
