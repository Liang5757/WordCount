from utils.utils import *
from utils.orders import *
from utils.count import *

if __name__ == '__main__':
    command = input("请输入命令(wc.exe [parameter] {file_name}):\n")
    [order, file_list] = parse_command(command)

    text = read_files(file_list)

    orders.get(order)(text)
