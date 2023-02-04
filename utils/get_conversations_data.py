import os
import os.path as osp
import json
import requests

from load_config import DotDict, load_config
from get_channels_list import get_channels_list


def conversations_request(channel_id, TOKEN, prev_data=None):

    URL = "https://slack.com/api/conversations.history"

    if prev_data is not None:
        if "response_metadata" in prev_data:
            cursor = prev_data["response_metadata"]["next_cursor"]
        else:
            cursor = None
    else:
        cursor = None

    params = {
        "channel": channel_id,
        "cursor": cursor
    }
    headers = {
    'Authorization': 'Bearer '+ str(TOKEN),
    }

    response = requests.get(URL, headers=headers, params=params)
    resdata = response.json()

    if not resdata["ok"]:
        print("Error: {}. Cannot get chennel list.".format(resdata["error"]))

    return resdata


def get_conversations_data(channel, config, save=True):

    channel_name = channel.name
    channel_id = channel.id

    first_resdata = conversations_request(channel_id, config.TOKEN, prev_data=None)

    all_resdata = [first_resdata]

    if "response_metadata" in first_resdata:
        more_data = True
        resdata = first_resdata
        while more_data:
            resdata = conversations_request(channel_id, config.TOKEN, prev_data=resdata)
            all_resdata.append(resdata)
            more_data = "response_metadata" in resdata
    
    messages = [DotDict(msg) for res in all_resdata for msg in res["messages"]]

    if save:
        os.makedirs(osp.join(config.saveDir,config.workspace,channel_name), exist_ok=True)
        with open(osp.join(config.saveDir,config.workspace,channel_name,"messages.json"), "w", encoding="utf8") as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)
    
    return messages


if __name__=="__main__":

    config_path = "config.yaml"
    config = load_config(config_path)

    data = get_channels_list(config)
    messages = get_conversations_data(data[0], config)

    print(messages[0].text)