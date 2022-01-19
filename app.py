import re
import logging

logging.basicConfig(level=logging.DEBUG)

from slack_bolt import App

app = App()


@app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()


@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    say("What's up?")


@app.event("reaction_added")
def say_something_to_reaction(say):
    say("OK!")


@app.message("test")
def test_message(logger, body):
    logger.info(body)


@app.message(re.compile("bug"))
def mention_bug(logger, body):
    logger.info(body)


@app.action("approve_req")
def handle_approve_action(ack, body, respond, logger):
    ack()
    body['message'].pop('bot_id', None)
    body['message'].pop('type', None)
    body['message'].pop('user', None)
    body['message'].pop('ts', None)
    body['message'].pop('team', None)
    body['message']['blocks'][3]={
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": ":white_check_mark: Approved!",
				}
			]
}
    respond(
        replace_original=True,
        text=body['message'],
    )

@app.action("reject_req")
def handle_reject_action(ack, body, respond, logger):
    ack()
    body['message'].pop('bot_id', None)
    body['message'].pop('type', None)
    body['message'].pop('user', None)
    body['message'].pop('ts', None)
    body['message'].pop('team', None)
    body['message']['blocks'][3]={
                        "type": "section",
                        "fields": [
                                {
                                        "type": "mrkdwn",
                                        "text": ":x: Rejected!",
                                }
                        ]
}
    respond(
        replace_original=True,
        text=body['message'],
    )

if __name__ == "__main__":
    app.start(8000)
