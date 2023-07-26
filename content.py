from connection import getHeaders
import requests

def getContent():
    Info = getHeaders()

    url = Info[0][0]
    payload = ""
    headers = {
        "Accept": f"{Info[2][0]}",
        "Accept-Encoding": f"{Info[4][0]}",
        "Accept-Language": f"{Info[6][0]}",
        "Connection": f"{Info[8][0]}",
        "Cookie": f"{Info[10][0]}",
        "Host": f"{Info[12][0]}",
        "Referer": f"{Info[14][0]}",
        "Sec-Fetch-Dest": f"{Info[16][0]}",
        "Sec-Fetch-Mode": f"{Info[18][0]}",
        "Sec-Fetch-Site": f"{Info[20][0]}",
        "User-Agent": f"{Info[22][0]}",
        "X-LIVEAGENT-AFFINITY": f"{Info[24][0]}",
        "X-LIVEAGENT-API-VERSION": f"{Info[26][0]}",
        "X-LIVEAGENT-SESSION-KEY": f"{Info[28][0]}"
        }


    response = requests.request("GET", url, headers=headers)

    return response.text
