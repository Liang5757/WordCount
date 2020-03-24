from utils.utils import *
from utils.count import *

if __name__ == '__main__':
    command = input("请输入命令(wc.exe [parameter] {file_name}):\n")

    parse_command(command)
