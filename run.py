from BeautifulReport import BeautifulReport
import unittest
import os,sys
import time

env = os.path.dirname(__file__)
sys.path.append(env)
current_path = os.getcwd()
report_path = os.path.join(current_path, "reports")   # 获取报告路径
Case_path = os.getcwd()+'\Test_case'  # 也可以写成Case_path = "./Test_case" 获取用例路径
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
# 报告地址和名称
report_title = "SCRM_API_TEST自动化测试报告"
# 报告描述
desc = '本次报告只针对线上scrm测试'

if __name__ == '__main__':
    import sys

    # sys.path.append(r'C:\Users\Administrator\PycharmProjects\SCRM_API_TEST\model\excel.py')
    # sys.path.append(r'C:\Users\Administrator\PycharmProjects\SCRM_API_TEST\model\config.py')
    # sys.path.append(r'C:\Users\Administrator\PycharmProjects\SCRM_API_TEST\model\readYaml.py')
    testsuit = unittest.defaultTestLoader.discover(".", pattern="test*.py", top_level_dir=None)
    run = BeautifulReport(testsuit)
    run.report(description=desc, filename=report_title, log_path=report_path)
    print(sys.path)