import praw
from email_functionality import SendEmail

import sys
sys.path.insert(0, r'D:\app')
from account_info import account

keywords = ['fresh']
artists = ['drake', 'kendrick', 'lamar', 'kanye', 'west', 'frank', 'ocean', 'joey', 'bada$$']


def main():
    reddit = praw.Reddit(client_id=account['personal_key'],
                         client_secret=account['secret_key'],
                         password=account['reddit_password'],
                         user_agent="RedditAPI/0.1",
                         username=account['username'])

    subreddit = reddit.subreddit('hiphopheads')
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    normalized_title = submission.title.lower()

    for keyword in keywords:
        if check_fresh(normalized_title):
            if check_artist(normalized_title):
                email = SendEmail(normalized_title, normalized_title)
                break


def check_fresh(title):
    for keyword in keywords:
        if keyword in title:
            return True


def check_artist(title):
    for artist in artists:
        if artist in title:
            return True


if __name__ == '__main__':
    main()