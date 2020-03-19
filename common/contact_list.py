import requests
from model import  Log

contact_list = [
        'uncontact_start',  # 未联系时间
        'uncontact_end',  # 未联系截止时间
        'uncontact_time',  # 未联系时间段
        'system_grade_level',  # 系统评级
        'tag_ids',  # 标签
        'state_id',  # 国家
        'is_worktime',  # 是否工作时间，1是，2否
        'saleman',  # 跟进人
        'keywords',  # 关键词查询
        'sort_system_grade_level',  # 按系统评级排序。 desc降序，asc升序
        'sort_recent_action_time',  # 按最近动态时间排序 desc降序，asc升序
        'sort_recent_contact_time',  # 按最近联系时间排序 desc降序，asc升序
        'life_cycle',  # 生命周期 1 新建客户 2潜在客户 3新成交客户 4返单客户 5衰退客户
        'first_letter',  # 首字母排序 desc降序，asc升序
        'type',  # 1表示 我 的 2表示共享给我的 3表示我共享的 4表示xx的联系人
        'group_id',  # 跟进人分组
        'search_source'  # 来源
    ]


# 获取联系人列表
def contact_required(_url, _token):

    data = {
        '_gouuse_token': _token,
        'page_size': '50',
        }
    r = requests.post(url=_url, data=data)
    result = r.json()
    # 打印日志到logs
    log = Log()
    log.debug('联系人筛选返回信息：%s' % result)
    return result


# 获取联系人筛选结果
def contact_other(_url, _token, key, value, listresult):

    data = {
        '_gouuse_token': _token,
        'page_size': '50',
        key: value
    }
    r = requests.post(url=_url, data=data)
    result = r.json()
    # 为了保障返回条数与返回统计数一致,n为接口返回的条数
    n = 0
    for d in result['data']:
        n = n + 1
    # 为了保障返回的统计数据与真实列表中符合的条数一致，t是真实列表符合的条数
    t = 0
    for level in listresult['data']:
        if key == 'tag_ids':
            l1 = level[key].split(',')
            if str(value) in l1:
                t = t + 1
        elif level[key] == value:
            t = t + 1

    try:
        assert(t == n)
    except AssertionError:
        print(t, n)
    return result, t


# 列表排序
def contact_sort(_url, _token, key, value):
    data = {
        '_gouuse_token': _token,
        'page_size': '50',
        key: value
    }
    r = requests.post(url=_url, data=data)
    result = r.json()
    return result


# 搜索列表内容
def contact_search(_url, _token, key, value, listresult, cod, price):

    data = {
        '_gouuse_token': _token,
        'page_size': '50',
        key: value
    }
    r = requests.post(url=_url, data=data)
    result = r.json()
    # 为了保障返回条数与返回统计数一致,n为接口返回的条数
    n = 0
    for d in result['data']:
        n = n + 1
    # 为了保障返回的统计数据与真实列表中符合的条数一致，t是真实列表符合的条数
    t = 0
    for level in listresult['data']:
        if key == 'tag_ids':
            l1 = level[cod].split(',')
            if str(price) in l1:
                t = t + 1
        elif level[cod] == price:
            t = t + 1

    assert(t == n)
    return result, t



