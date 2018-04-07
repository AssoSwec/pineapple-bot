import markovify

class TextGenerator:
    def __init__(self, reddit, sub):
        self.comment_data = ''
        subreddit = reddit.subreddit(sub)
        for submission in subreddit.top(limit=100):
            for comment in submission.comments:
                try:
                    # strip out any links
                    clean = ' '.join(item for item in comment.body.split(' ') if not item.endswith('.com'))
                    self.comment_data += clean + ' '
                except AttributeError as e:
                    continue
        self.text_model = markovify.Text(self.comment_data)

    def make_sentence(self):
        return self.text_model.make_sentence()