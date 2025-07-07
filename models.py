class Title_Data():
    def __init__(self, title: str, keywords: list[str], sentiments: dict[str, float]):
        self.title = title
        self.keywords = keywords
        self.sentiments = sentiments

    def __repr__(self) -> str:
        return f"{self.title[0:4]}-"

class Site_Data():
    def __init__(self, url: str, title_datas: list[Title_Data], response_time: float):
        self.url = url
        self.title_datas = title_datas
        self.response_time = response_time

    def __repr__(self) -> str:
        return f'"{self.url}" {self.title_datas}'
    
    def titles(self) -> list[str]:
        return [title_data.title for title_data in self.title_datas]
    
    def keywords(self) -> list[str]:
        return sum([title_data.keywords for title_data in self.title_datas], [])
    
    def get_sentiments(self) -> list[dict[str, float]]:
        return [title_data.sentiments for title_data in self.title_datas]
    
    def set_sentiments(self, sentiments: list[dict[str, float]]):
        for i in range(len(self.title_datas)):
            self.title_datas[i].sentiments = sentiments[i]
    
    def compounds(self) -> list[float]:
        return [title_data.sentiments["compound"] for title_data in self.title_datas]
    
class Transaction():
    def __init__(self, commodity: str, stake_AUD: float):
        self.commodity = commodity
        self.stake_AUD = stake_AUD
