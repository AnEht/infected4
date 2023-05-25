import os

def is_multilevel_path(path):
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            # 如果有子目录，说明是多级路径
            return True
    # 如果没有子目录，说明只有一级路径
    return False

if __name__ == '__main__':
    while True:
        path = input('请输入路径：')
        if path == 'exit':
            # 如果用户输入 exit，退出循环
            break
        if is_multilevel_path(path):
            print('这是一个多级路径')
        else:
            print('这是一个只有一级的路径')
