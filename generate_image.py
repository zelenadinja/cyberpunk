import praw

reddit_read_only = praw.Reddit(
        client_id="1PJvIf_ASxARMDLWKQ-ODg",
        client_secret="tXBCDW6MxKrFFV-abnPgQoZtamIHeQ",
        user_agent="alita-scraping",

        )

subreddit = reddit_read_only.subreddit("cyberpunk")
print(subreddit.display_name)
print(subreddit.title)
print(subreddit.description)

