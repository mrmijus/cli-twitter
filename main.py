import os
import argparse
import sys

import tweepy


def tweet(message: str) -> None:
    twitter_auth_keys = {
        "consumer_key": os.getenv('CONSUMER_KEY'),
        "consumer_secret": os.getenv('CONSUMER_SECRET'),
        "access_token": os.getenv('ACCESS_TOKEN'),
        "access_token_secret": os.getenv('ACCESS_TOKEN_SECRET'),
    }
    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)

    try:
        api.update_status(status=message)
    except Exception as e:
        raise RuntimeError(f'Could not Tweet. Error: {e}')


def main():
    parser = argparse.ArgumentParser(description='Process CLI Twitter Args.')
    parser.add_argument('-t', '--tweet', type=str)
    args = parser.parse_args()
    tweet(message=args.tweet)


if __name__ == '__main__':
    main()
