import json
import requests

from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from cloudify.exceptions import NonRecoverableError, OperationRetry

slack_token = inputs['slack_token']
slack_channel = inputs['channel_id']
message_ts = ctx.target.instance.runtime_properties['response']['message']['ts']
BREAK_MSG = 'Waiting for Slack approval'

def get_latest_message():
    return requests.get('https://slack.com/api/conversations.history',
        headers={'Authorization': 'Bearer {0}'.format(slack_token)},
        params={
        'channel': slack_channel,
        "latest": message_ts,
        "limit": 1,
         "inclusive": True
    }).json()

updated_message = get_latest_message()['messages'][0]['blocks'][3]

if 'fields' not in updated_message:
    raise OperationRetry(BREAK_MSG)

if 'Rejected!' in updated_message['fields'][0]['text']:
    raise NonRecoverableError('Rejected')
elif 'Approved!' in updated_message['fields'][0]['text']:
    ctx.logger.info('Got Slack approval')
