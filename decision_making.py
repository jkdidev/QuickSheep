from models import *
import asyncio

async def interpret_results(site_datas: list[Site_Data]) -> Transaction:
    avg_compounds = await asyncio.gather(*(avg_sentiment(site_data, "compound") for site_data in site_datas))
    avg_compound = sum(avg_compounds) / len(site_datas)

    print(f"Average compound = {avg_compound}")
    return Transaction("0", 0)

async def avg_sentiment(site_data: Site_Data, key: str) -> float:
    sum_total = sum([sentiments[key] for sentiments in site_data.sentiments])
    return sum_total / len(site_data.sentiments)