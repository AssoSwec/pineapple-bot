import markovify
import praw

reddit = praw.Reddit(client_id='jM7OgXvUxGNG_A',
                     client_secret='hSa0af4LMNHc_WIS909oxu9NMsM',
                     user_agent='pineapple-bot-discord v0.0.1')
reddit.read_only = True

user_name = "@nickypy#8619"
comment_data = ""



def build_corpus():
    global text_model, comment_data
    subreddit = reddit.subreddit('roastme')
    for submission in subreddit.top(limit=100):
        for comment in submission.comments:
            try:
                comment_data += comment.body + ' '
            except AttributeError as e:
                continue
    text_model = markovify.Text(comment_data)

build_corpus()

roast_str = user_name + ': ' + text_model.make_sentence()
print(roast_str)
roast_str = user_name + ': ' + text_model.make_sentence()
print(roast_str)
roast_str = user_name + ': ' + text_model.make_sentence()
print(roast_str)
roast_str = user_name + ': ' + text_model.make_sentence()
print(roast_str)
roast_str = user_name + ': ' + text_model.make_sentence()
print(roast_str)
roast_str = user_name + ': ' + text_model.make_sentence()
print(roast_str)
roast_str = user_name + ': ' + text_model.make_sentence()
print(roast_str)
