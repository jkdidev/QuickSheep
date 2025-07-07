import asyncio
import time
from protocols.fetching.headlines import main as fetch_headlines
from protocols.analysis.sentiment import main as analyse_sentiments
from protocols.analysis.decision_making import interpret_results
from protocols.storing.dbmanager import *
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
# Certain keywords should be negative modifiers. Model is trained to adjust modifiers based on market performance of certain days vs that day's articles.

DEBUG = False
SLEEP_DURATION_SECONDS = 10 * 60 # Wait 10 mins

def main(debug: bool):
    initialise_databases()
    print("Initialised.")
    i = 0
    while(True):
        print(f"Iteration: {i}")
        results = fetch_headlines(debug, keywords)

        sentiments = asyncio.run(analyse_sentiments(results))

        results = asyncio.run(interpret_results(sentiments))

        new_titles = add_daily_articles(sentiments)
        print("New titles: " + str([title_data.title for title_data in new_titles]))
        increment_keywords(new_titles)

        time.sleep(SLEEP_DURATION_SECONDS)

if __name__ == "__main__":
    main(DEBUG)