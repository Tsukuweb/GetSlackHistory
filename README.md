# GetSlackHistory

Get Slack conversation data as json files and download files in your workspace with Python and Slack API.

## config.yaml

Write `config.yaml` like `sampleConfig.yaml`.

`config.yaml` needs three informations: `workspace`, `saveDir` and `TOKEN`.

```yaml
// config.yaml

config:
  workspace: YourWorkspace
  saveDir: save
  TOKEN: Your Slack API token
```

## How to use

1. Make `config.yaml`.

2. If `pyyaml` isn't in your environment, install with `pip install pyyaml`.

3. Run `python main.py` in terminal.