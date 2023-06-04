from flask import Flask, request, render_template
import textwrap
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        thread_title = request.form.get('thread_title', '')
        hashtag = request.form.get('hashtag', '')
        split_texts = []

        # Max tweet length accounting for spaces and thread footer
        max_tweet_len = 280 - len(thread_title) - len(hashtag) - len(' (Tweet 1/1)') - 4  # 4 spaces

        # Splitting logic
        sentences = re.split('(?<=[.!?]) +', text)
        current_tweet = thread_title
        for sentence in sentences:
            if len(current_tweet) + len(sentence) + 1 <= max_tweet_len:  # +1 for space between sentences
                current_tweet += ' ' + sentence
            else:
                split_texts.append((current_tweet, len(current_tweet)))
                current_tweet = sentence
        split_texts.append((current_tweet, len(current_tweet)))  # append the last tweet

        # Adding thread footer and hashtag
        for i, (tweet, _) in enumerate(split_texts):
            thread_footer = f' (Tweet {i+1}/{len(split_texts)})'
            split_texts[i] = (f'{tweet}{thread_footer} {hashtag}', len(tweet) + len(thread_footer) + len(hashtag) + 2)  # +2 for spaces

        return render_template('index.html', split_texts=split_texts)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
