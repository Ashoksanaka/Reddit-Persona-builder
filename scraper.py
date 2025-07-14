import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

def fetch_user_data(username, limit=50):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts = []
    comments = []

    for submission in user.submissions.new(limit=limit):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "subreddit": submission.subreddit.display_name,
            "url": submission.url,
            "permalink": f"https://reddit.com{submission.permalink}"
        })

    for comment in user.comments.new(limit=limit):
        comments.append({
            "body": comment.body,
            "subreddit": comment.subreddit.display_name,
            "permalink": f"https://reddit.com{comment.permalink}"
        })

    return {"posts": posts, "comments": comments}
