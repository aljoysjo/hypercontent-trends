from pytrends.request import TrendReq
import pandas as pd, datetime as dt

py = TrendReq(hl="es-ES", tz=-180)
py.build_payload(["*"], timeframe="now 7-d", geo="AR")
df = py.trending_searches(pn="argentina")
df["source"] = "gtrends"
df["ts"] = dt.date.today()
df.to_csv("data/gtrends.csv", index=False)
