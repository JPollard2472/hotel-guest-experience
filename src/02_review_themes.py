import sqlite3
import pandas as pd

conn = sqlite3.connect("data/hotel_reviews.db")

with open("sql/01_review_themes.sql") as f:
    query = f.read()

result = pd.read_sql(query, conn)
print(result.to_string(index=False))

conn.close()