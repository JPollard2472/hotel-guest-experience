import sqlite3
import pandas as pd

# Read the reviews
reviews = pd.read_csv("data/tripadvisor_hotel_reviews.csv")
reviews.columns = ["review", "rating"]          # lowercase column names
reviews.insert(0, "review_id", range(1, len(reviews) + 1))  # give each review an ID

# Load into the database
conn = sqlite3.connect("data/hotel_reviews.db")
reviews.to_sql("reviews", conn, if_exists="replace", index=False)

# Check it worked
print(pd.read_sql("SELECT COUNT(*) AS total_reviews FROM reviews", conn))
print()
print(pd.read_sql("""
    SELECT rating,
           COUNT(*) AS reviews,
           ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM reviews), 1) AS pct
    FROM reviews
    GROUP BY rating
    ORDER BY rating DESC
""", conn).to_string(index=False))

conn.close()