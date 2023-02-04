import os
import os.path as osp
import requests

from .load_config import DotDict, load_config


def download_file(fileurl, filename, channel, config):

    channel_name = channel.name

    headers = {
        'Authorization': 'Bearer '+ str(config.TOKEN),
    }

    data = requests.get(fileurl, headers=headers).content

    os.makedirs(osp.join(config.saveDir,config.workspace,channel_name,"files"), exist_ok=True)

    with open(osp.join(config.saveDir,config.workspace,channel_name,"files",filename), mode='wb') as f:
        f.write(data)


def get_files(message, channel, config):

    # print(type(message))

    for file in message.files:
        
        file = DotDict(file)

        if file.mode != "tombstone":
            if "url_private_download" in file:
                fileurl = file.url_private_download
            else:
                fileurl = file.url_private
        else:
            continue

        filename = "{}-{}-{}".format(file.id, file.user, file.name)

        download_file(fileurl, filename, channel, config)


if __name__=="__main__":

    config_path = "config.yaml"
    config = load_config(config_path)

    