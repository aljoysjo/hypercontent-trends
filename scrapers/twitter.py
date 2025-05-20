from twscrape import API
import asyncio, pandas as pd, datetime as dt, os

USER = os.getenv("TW_USER")       # cargalos luego como Secrets en Replit
PWD  = os.getenv("TW_PWD")

async def run():
    api = API()
    await api.pool.add_account(USER, PWD)
    q = "(argentina OR buenos aires) lang:es min_faves:20"
    tweets = await api.search(q, limit=400)
    rows = [{"text": t.rawContent, "source": "twitter", "ts": dt.date.today()} for t in tweets]
    pd.DataFrame(rows).to_csv("data/twitter.csv", index=False)

if __name__ == "__main__":
    asyncio.run(run())
