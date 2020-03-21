

# description：parse command
# param：order input
# return：[order, [file_list]] / FALSE
def parse_command(command):
    command = command.strip().split(" ")
    [header, order, file_list] = command

    # 待填充错误检查

    return [order, file_list]


# description：read files
# param：file_list
# return：[file content, ...]
def read_files(file_list):
    with open(file_list, 'r') as f:
        return f.readlines()
