import requests

from .load_config import DotDict


def get_replies(channel_id, message, config):

    URL = "https://slack.com/api/conversations.replies"
    ts = message.ts

    params = {
        "channel": channel_id,
        "ts": ts
    }
    headers = {
    'Authorization': 'Bearer '+ str(config.TOKEN),
    }  

    response = requests.get(URL, headers=headers, params=params)
    resdata = DotDict(response.json())

    if not resdata.ok:
        print("Error: {}. Cannot get reply data.".format(resdata.error))

    replies = [DotDict(msg) for msg in resdata.messages]
    
    ### TimeStampによるPaginationは未実装
    ### とりあえず今はPaginationなしで実装

    return replies