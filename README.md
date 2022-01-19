# slack-bolt-approval

this is a simple bolt-app , to handle approval request based on simple structure
it will run on port 8000

You will need to enable Interactivity inside your application and provide the following Request URL

http://<server_ip>:8000/slack/events

# Python 3.6+ required
```
python3 -m venv .venv
source .venv/bin/activate

pip install -U pip
pip install slack_bolt
```

before running the app , you need to export 2 environment variables that matches your slack workspace

```
# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
```

inside blueprint is a simple blueprint that creates the message on a specific channel to ask for user approval

5 secrets need to be configured on Cloudify to run it

```
slack_token
slack_channel
slack_channel_id
aws_access_key_id
aws_secret_access_key
```
