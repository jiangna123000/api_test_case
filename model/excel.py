import openpyxl, time
import os


def change_excel():
    # 获取当前脚本所在文件夹路径
    curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+r'\file'
    #  获取yaml文件路径
    file_home = os.path.join(curpath, "contact.xlsx")
    workbook = openpyxl.load_workbook(filename=file_home)

    # 修改客户名称+网站
    sheet_name1 = workbook['客户']
    sheet_name1['A3'] = '自动化导入客户%s' % time.strftime('%Y.%m.%d', time.localtime(time.time()))
    cname = sheet_name1['A3'].value
    sheet_name1['B3'] = 'www.%s.com' % time.strftime('%Y.%m.%d', time.localtime(time.time()))
    cwebsite = sheet_name1['B3'].value

    # 修改联系人名称+座机号
    sheet_name2 = workbook['联系人']
    sheet_name2['A3'] = '自动化导入联系人%s' % time.strftime('%Y.%m.%d', time.localtime(time.time()))
    sname = sheet_name2['A3'].value
    snum = int(sheet_name2['M3'].value)+1
    sheet_name2['M3'] = str(snum)
    snub = sheet_name2['M3'].value

    # 保存修改
    workbook.save(file_home)
    workbook.close()
    return cname, cwebsite, sname, snub


if __name__ == '__main__':
    print(change_excel())
