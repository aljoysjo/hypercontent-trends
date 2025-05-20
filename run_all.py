import subprocess, glob, pandas as pd, sqlite3

# Ejecuta todos los scrapers
for f in glob.glob("scrapers/*.py"):
    subprocess.run(["python", f])

# Une outputs
dfs = [pd.read_csv(p) for p in glob.glob("data/*.csv")]
df = pd.concat(dfs, ignore_index=True).drop_duplicates("text")

# Score = ocurrencias en fuentes + normalización de plays/favs
df["score"] = df.groupby("text")["source"].transform("nunique")
if "plays" in df.columns:
    df["score"] += (df["plays"]/df["plays"].max()).fillna(0)

# Guarda para el generador
conn = sqlite3.connect("trends.db")
df.to_sql("latam", conn, if_exists="replace", index=False)
conn.close()
