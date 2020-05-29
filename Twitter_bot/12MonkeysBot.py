import tweepy
import time
import random
import logging
from monkeys_creds import api
from monkeys_episodes import monkeys12

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api,keyword,since_id):
    logger.info("Checking Mentions..")
    new_since_id = since_id
    for mention in tweepy.Cursor(api.mentions_timeline,
        since_id = since_id).items():
        new_since_id = max(mention.id,new_since_id)
        if mention.in_reply_to_status_id is not None:
            continue
        if keyword in mention.text.lower():
            logger.info(f'Responding to {mention.user.screen_name}...')

            api.update_status(status = f'@{mention.user.screen_name} - '
            f'{random.choice(list(monkeys12.values()))}',
            in_reply_to_status_id=mention.id)

    return new_since_id


def main():
    since_id = 1 
    while True:
        since_id = check_mentions(api,'initiate splinter sequence',since_id)
        logger.info("Waiting..")
        time.sleep(60)

if __name__ == '__main__':
    main()