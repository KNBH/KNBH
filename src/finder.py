"person downloader"


import re
import requests

from src import const
from src import person
from http.client import responses


def get(block, room):

    "Get request to kn.vutbr.cz and retrieve person's data"


    URL = 'http://kn.vutbr.cz/search/index.html?str='+str(block)+'-'+str(room)

    get_request = requests.get(URL)

    if get_request.status_code is not 200:
        print("ERROR:\tStatus code of HTTP GET request is", get_request.status_code, "-", responses[get_request.status_code])
        print("\tURL:", URL)
        return None
    elif "Data nenalezena" in get_request.text:
        return None

    matches = re.finditer(r"<\/font>\s(.*)\s(.*)<\/th>", get_request.text)

    names = list()

    for match in matches:
        p_name = str(match.group(1))
        p_surname = str(match.group(2))
        p_gender = const.FEMALE if p_surname.endswith(('á', 'Á')) else const.MALE

        names.append(person.Person(p_name, p_surname, p_gender))

    return names
