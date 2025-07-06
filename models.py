class Site_Data():
    def __init__(self, url: str, title_keyword_pairs: dict[str, str], response_time: float):
        self.url = url
        self.keyword_title_pairs = title_keyword_pairs
        self.response_time = response_time
        self.sentiments = []
        self.useful_titles = {}

    def __repr__(self) -> str:
        return f'"{self.url}" {self.title_sentiment_pairs(True)}'
    
    def title_sentiment_pairs(self, shorten:bool = False) -> dict[str, dict[str, float]]:
        if not shorten:
            return dict(zip(self.titles(), self.sentiments))
        
        shortened_titles = [title[0:4] for title in self.titles()]
        return dict(zip(shortened_titles, self.sentiments))
    
    def titles(self) -> list[str]:
        return list(self.keyword_title_pairs.keys())
    
class Transaction():
    def __init__(self, commodity: str, stake_AUD: float):
        self.commodity = commodity
        self.stake_AUD = stake_AUD
