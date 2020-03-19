import requests


def get_shares_contacts(url, contacts_id, header):
    data = {
        'contacts_id': contacts_id,
        'type': 0
    }
    r = requests.post(url=url, data=data, headers=header)
    result = r.json()
    return result


def contactShare(url, contacts_id, member_id, header):
    data = {
        "contacts_id": "["+str(contacts_id)+"]",
        "data": "[{\"member_id\":"+member_id+",\"read_permission\":1,\"write_permission\":0}]"
    }

    r = requests.post(url=url, data=data, headers=header)
    result = r.json()
    return result

