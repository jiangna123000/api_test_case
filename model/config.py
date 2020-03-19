import configparser
import os


config = configparser.ConfigParser()
# path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini 也可以用这个方法
#config.read(r'C:\Users\Administrator\PycharmProjects\SCRM_API_TEST\model\config.ini', encoding="utf-8")   # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
'''
secs = config.sections()
# 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
options = config.options("db")  # 获取某个section名为db所对应的键
items = config.items("db")  # 获取section名为db所对应的全部键值对
host = config.get("db", "token")  # 获取[db]token
'''
# 获取当前脚本所在文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))
# # 获取yaml文件路径
yamlpath = os.path.join(curpath, "config.ini")
config.read(yamlpath)


def readconfig(key):  # 获取token的值
    tk = config.get("db", key)
    return tk


def fixconfig(key, value):  # 修改token的值
    config.set("db", key, value)
    with open(yamlpath, 'w') as op:
        config.write(op)


if __name__ == "__main__":
    fixconfig("token", '123')
    fixconfig("company_id", '111')

