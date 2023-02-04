import os
import os.path as osp
import json
import requests

from .load_config import DotDict


def get_channels_list(config, save=True):

    URL = "https://slack.com/api/conversations.list"
    TOKEN = config.TOKEN

    headers = {
        'Authorization': 'Bearer '+ str(TOKEN),
    }

    response = requests.get(URL, headers=headers)
    resdata = response.json()

    if not resdata["ok"]:
        print("Error: {}. Cannot get chennel list.".format(resdata["error"]))
    
    if save:
        os.makedirs(osp.join(config.saveDir,config.workspace), exist_ok=True)
        with open(osp.join(config.saveDir,config.workspace,"channels.json"), "w", encoding="utf8") as f:
            json.dump(resdata, f, indent=2, ensure_ascii=False)

    return [DotDict(c) for c in resdata["channels"]]