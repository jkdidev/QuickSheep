import sqlite3
from models import *
from collections import Counter

def initialise_databases():
    connection = sqlite3.connect("quicksheep.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS keywords (
            keyword_id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT UNIQUE,
            frequency INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_articles (
            article_id INTEGER PRIMARY KEY AUTOINCREMENT,
            article_title TEXT,
            neg REAL,
            neu REAL,
            pos REAL,
            compound REAL
        )
    ''')

    connection.commit()
    connection.close()

def increment_keywords(title_datas: list[Title_Data]):
    connection = sqlite3.connect("quicksheep.db")
    cursor = connection.cursor()

    keywords = sum([title_data.keywords for title_data in title_datas], [])
    frequency_counter = Counter(keywords)

    for keyword in set(keywords):
        frequency = frequency_counter[keyword]
        # Try to update the keyword
        cursor.execute("""
            UPDATE keywords
            SET frequency = frequency + ?
            WHERE keyword = ?
        """, (frequency, keyword))

        if cursor.rowcount == 0:
            # If keyword doesn't exist, insert it
            cursor.execute("""
                INSERT INTO keywords (keyword, frequency) VALUES (?, ?)
            """, (keyword, frequency))

    connection.commit()
    connection.close()

def add_daily_articles(site_datas: list[Site_Data]) -> list[Title_Data]:
    ret = []
    connection = sqlite3.connect("quicksheep.db")
    cursor = connection.cursor()

    for site_data in site_datas:
        titles = site_data.titles()
        sentiments = site_data.get_sentiments()
        for i in range(len(titles)):
            cursor.execute("""
                SELECT EXISTS(SELECT 1 FROM daily_articles WHERE article_title = ?)
            """, (titles[i],))

            exists = cursor.fetchone()[0]
            if not exists:
                ret.append(site_data.title_datas[i])
                cursor.execute("""
                    INSERT INTO daily_articles (article_title, neg, neu, pos, compound)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    titles[i],
                    sentiments[i]["neg"],
                    sentiments[i]["neu"],
                    sentiments[i]["pos"],
                    sentiments[i]["compound"]
                ))

    connection.commit()
    connection.close()

    return ret



initialise_databases()
