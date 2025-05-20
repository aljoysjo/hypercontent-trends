import requests, pandas as pd, datetime as dt

url = "https://www.tiktok.com/api/trending/item_list/?count=30&region=AR"
resp = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}).json()

rows = [{"text": itm["desc"],
         "plays": itm["stats"]["playCount"],
         "source":"tiktok",
         "ts": dt.date.today()} for itm in resp["itemList"]]

pd.DataFrame(rows).to_csv("data/tiktok.csv", index=False)
