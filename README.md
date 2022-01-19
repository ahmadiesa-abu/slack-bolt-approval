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
