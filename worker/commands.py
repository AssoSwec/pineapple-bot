import json
import random
import requests

def get_food_pic(sub, reddit):
    subreddit = reddit.subreddit(sub)
    hot = [x for x in subreddit.hot(limit=100)]
    return random.choice(hot).url


def random_fact(reddit):
    subreddit = reddit.subreddit('TodayILearned')
    hot = [x for x in subreddit.hot(limit=100)]
    fact = random.choice(hot)

    # remove leading TIL in title
    title = ' '.join(fact.title.split()[1:])
    return 'Bet you didn\'t know ' + title + '\n' + 'Source: ' + fact.url


def gif(search_term, giphy_key):
    if search_term.strip() == "":
        search_term = 'praise the sun'

    request_str = 'https://api.giphy.com/v1/gifs/random?api_key=' + \
        giphy_key + '&tag=' + search_term + '&rating=R'
    r = requests.get(request_str).json()
    file_name = r["data"]["image_original_url"]
    return file_name


def compile(message, compiler):
    # parse message for code blocks and send it to hackerrank API

    arr = message.split('```')

    lang = arr[0].split(' ')[1].strip()
    source = arr[1]

    result = compiler.run({
        'source': source,
        'lang': lang
    })

    out = result.output
    if out != None:
        msg = str(out[0])

        if len(msg) != 0:
            return msg
        else:
            "An error occured. Check your code."
    else:
        return str(result.message)