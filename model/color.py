# coding=utf-8


def coloring():
    """输出终端时给字体着色
       显示格式: \033[显示方式;前景色;背景色m
       只写一个字段表示前景色,背景色默认
    """
    color_dict = {
        'RED': '\033[31m',  # 红色
        'GREEN': '\033[32m',  # 绿色
        'YELLOW': '\033[33m',  # 黄色
        'BLUE': '\033[34m',  # 蓝色
        'FUCHSIA': '\033[35m', # 紫红色
        'CYAN': '\033[36m',  # 青蓝色
        'WHITE': '\033[37m',  # 白色
        'RESET': '\033[0m',  # 终端默认颜色
    }
    return color_dict