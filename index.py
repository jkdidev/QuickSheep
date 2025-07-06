import asyncio
from headlines import main as fetch_headlines
from sentiment import main as analyse_sentiments
from decision_making import interpret_results
from constants import *

"""
QuickSheep is a program that repeatedly queries live financial RSS feeds, it then
runs sentiment analysis on the titles of articles from those feeds. If the
news is good, above a threshold, it buys the US dollar. If the news is bad,
it buys gold. It ranks each feed by 'usefullness' - a score proportional to
the profit it has made when making trades in response to that feed's articles.
The bot operates on the philosophy that daytraders are predictable, acting like
sheep who are shepherded by positive and negative news articles to make financial
decisions.

QuickSheep concedes that perhaps more money could be made by going against the grain in
certain circumstances. However, there are so many financial institutions who spend
millions to do that. Instead, with limited resources, QuickSheep goes with the grain,
like a sheep, but tries its best to be the quickest to the mark.
"""

# Importance of ignore words: "Call centres could be a gold mine for Africa".
# Certain keywords should be negative modifiers. E.g. - a positive article about BRICS should be considered as a negative USD article.

DEBUG = False

def main(debug: bool):
    print("Initialised.")
    results = fetch_headlines(debug, keywords) # = seed_data

    sentiments = asyncio.run(analyse_sentiments(results))
    #print(sentiments)

    asyncio.run(interpret_results(sentiments))

if __name__ == "__main__":
    main(DEBUG)