import argparse
import logging
import os
import datetime

from dotenv import load_dotenv
from instabot import Bot

logger = logging.getLogger()


def create_parser():
    parser = argparse.ArgumentParser(description='Amplifier')
    parser.add_argument('--account_name', help='account_name', default='cocacolarus', type=str)

    return parser


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    logger.setLevel(logging.INFO)

    parser = create_parser()
    args = parser.parse_args()

    load_dotenv()
    inst_login = os.getenv("INST_LOGIN")
    inst_password = os.getenv("INST_PASSWORD")

    bot = Bot()
    bot.login(username=inst_login, password=inst_password)

    user_id = bot.get_user_id_from_username(args.account_name)
    total_user_medias = bot.get_total_user_medias(user_id)
    for media in total_user_medias:
        comment = bot.get_media_comments_all(media)[0]
        comment_text = comment['text']
        timestamp = comment['created_at_utc']
        comment_date = datetime.datetime.utcfromtimestamp(timestamp)


if __name__ == '__main__':
    main()