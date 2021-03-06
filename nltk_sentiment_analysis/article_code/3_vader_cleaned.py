from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
sentiment_scores = sia.polarity_scores("Today is a beautiful day :)")
print(sentiment_scores)

print("\n~x~\n")

from nltk import ClassifierI
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentIntensityAnalyzerWrapper(ClassifierI):
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def classify_many(self, featuresets):
        results = []
        for features in featuresets:
            sentiment_scores = self.sid.polarity_scores(features)
            if sentiment_scores["compound"] >= 0:
                results.append(1)
            else:
                results.append(0)
        return results


print("\n~x~\n")

import html

import preprocessor as tweet_preprocessor
from nltk.corpus import twitter_samples
from nltk.sentiment import SentimentAnalyzer

positive_tweets = twitter_samples.strings("positive_tweets.json")
negative_tweets = twitter_samples.strings("negative_tweets.json")

# Reset the tweet preprocessor to it's default settings
tweet_preprocessor.set_options(tweet_preprocessor.OPT.URL,
                               tweet_preprocessor.OPT.MENTION,
                               tweet_preprocessor.OPT.HASHTAG,
                               tweet_preprocessor.OPT.RESERVED,
                               tweet_preprocessor.OPT.NUMBER,
                               tweet_preprocessor.OPT.EMOJI,
                               tweet_preprocessor.OPT.SMILEY,
                               )

cleaned_postive_tweets = [tweet_preprocessor.clean(html.unescape(x)) for x in positive_tweets]
cleaned_negative_tweets = [tweet_preprocessor.clean(html.unescape(x)) for x in negative_tweets]

test_samples = [(t, 1) for t in cleaned_postive_tweets[4000:]] + [(t, 0) for t in cleaned_negative_tweets[4000:]]

siaw = SentimentIntensityAnalyzerWrapper()
sentim_analyzer = SentimentAnalyzer()

for key, value in sorted(sentim_analyzer.evaluate(test_samples, classifier=siaw).items()):
    print('{0}: {1}'.format(key, value))

print("\n~x~\n")
