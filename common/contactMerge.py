import requests
from model import read_yaml


def contactmerge(url, a, b, header):

    data = {'contacts_id': a,
            'merge_contacts_id': b
             }
    r = requests.post(url=url, data=data, headers=header)
    result = r.json()
    return result
