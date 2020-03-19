import os
import yaml


def read_yaml():
    # 获取当前脚本所在文件夹路径
    curpath = os.path.dirname(os.path.realpath(__file__))
    # # 获取yaml文件路径
    yamlpath = os.path.join(curpath, "data.yaml")
    # open方法打开直接读出来
    with open(yamlpath, 'r', encoding='utf-8') as f:
        cfg = f.read()
        d = yaml.load(cfg)  # 用load方法转字典
    return d



if __name__ == "__main__":
    baseurl = read_yaml()[0]['baseurl']
    url = read_yaml()[1]['url']
    curpath = os.path.dirname(os.path.realpath(__file__))
    print(curpath)