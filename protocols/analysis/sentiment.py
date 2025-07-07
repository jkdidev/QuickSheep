import asyncio
import nltk
from models import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# download nltk corpus (first time only)
import nltk

analyser = SentimentIntensityAnalyzer()

async def preprocess_text(text: str) -> str:
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    processed_text = ' '.join(lemmatized_tokens)

    return processed_text


async def main(site_datas: list[Site_Data]):
    results = await asyncio.gather(*(analyse(site_data) for site_data in site_datas))
    return results


async def analyse(site_data: Site_Data) -> Site_Data:
    titles = site_data.titles()

    #print("Preprocessing titles...")
    preprocessed_titles = await asyncio.gather(*(preprocess_text(title) for title in titles))

    #print("Analysing sentiments...")
    site_data.set_sentiments(await asyncio.gather(*(get_sentiment(title) for title in preprocessed_titles)))
    #interesting_sentiments = [(title_sentiment_pair[0], title_sentiment_pair[1]['compound']) for title_sentiment_pair in sentiments if abs(title_sentiment_pair[1]['compound'])]# > 0.3]

    return site_data


async def get_sentiment(text: str) -> dict[str, float]:
    #print(text)
    scores = analyser.polarity_scores(text)

    return scores