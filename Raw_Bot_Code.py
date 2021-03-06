"""To obtain the CREDENTIALS referenced in 23, you must get a reddit developers account (will take about a minute), 
then they will be on the page for you to see. The user agent name must be filled in, and can not be empty, but it has no effect.




import praw
import pdb
import re
import os
import sys

if len(sys.argv) >= 3:
    args = sys.argv[1:]
    subreddit = args[0]
    reply = " ".join(args[1:])
if len(sys.argv) == 2:
    subreddit = sys.argv[2]
    reply = "Yo"
if len(sys.argv) == 1:
    subreddit = 'mildlyinteresting'
    reply = "Yo"


# Create the Reddit instance and log in
reddit = praw.Reddit(client_id='ENTER YOUR OWN CREDENTIALS',
                     client_secret='ENTER YOUR OWN CREDENTIALS',
                     password='ENTER YOUR OWN CREDENTIALS',
                     username='ENTER YOUR OWN CREDENTIALS',
                     user_agent = 'ENTER YOUR OWN CREDENTIALS: can be anything, just not empty')

# Create a list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# Or load the list of posts we have replied to
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Pull the hottest 10 entries from a subreddit of your choosing
subreddit = reddit.subreddit(subreddit)

for submission in subreddit.hot(limit=10):
    print(submission.title)

    # Make sure you didn't already reply to this post
    if submission.id not in posts_replied_to:
        
        # Not case sensitive
        if re.search("", submission.title, re.IGNORECASE):
            if not (re.search("looking for users", submission.title, re.IGNORECASE)):
                
                submission.reply(reply)
                print("Bot replying to : ", submission.title)
                print('reply was:' + reply)
                # Store id in list
                posts_replied_to.append(submission.id)

# Write updated list to file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
