from utils.get_files import get_files
from utils.load_config import load_config
from utils.get_channels_list import get_channels_list
from utils.get_conversations_data import get_conversations_data


def main():

    config_path = "config.yaml"
    config = load_config(config_path)

    channels = get_channels_list(config)

    for channel in channels:

        print("download from channel '{}'...".format(channel.name))

        messages = get_conversations_data(channel, config)

        for thread in messages:
            for msg in thread:
                if "files" in msg:
                    get_files(msg, channel, config)
    
    print("Done!")


if __name__=="__main__":
    main()