import sqlite3
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/hotel_reviews.db")
with open("sql/01_review_themes.sql") as f:
    themes = pd.read_sql(f.read(), conn)
with open("sql/02_guest_groups.sql") as f:
    groups = pd.read_sql(f.read(), conn)
conn.close()

# Chart 1: how each theme moves the star rating
themes = themes.sort_values("vs_overall")
colors = ["#d1495b" if v < 0 else "#2a9d8f" for v in themes["vs_overall"]]
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(themes["theme"], themes["vs_overall"], color=colors)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_xlabel("Stars above or below the average review")
ax.set_title("Bad Experiences Hurt Ratings Far More Than Good Ones Help")
plt.tight_layout()
plt.savefig("output/theme_impact.png", dpi=150)
plt.close()

# Chart 2: what disappointed vs delighted guests talk about
order = ["Delighted (5)", "Satisfied (3-4)", "Disappointed (1-2)"]
groups = groups.set_index("guest_group").loc[order]
cols = {"pct_friendly_staff": "Friendly staff", "pct_rude_staff": "Rude staff",
        "pct_dirty": "Dirty", "pct_noise": "Noise"}
plot = groups[list(cols)].rename(columns=cols).T
ax = plot.plot(kind="bar", figsize=(9, 5), color=["#2a9d8f", "#8d99ae", "#d1495b"], rot=0)
ax.set_ylabel("% of reviews mentioning it")
ax.set_title("What Delighted and Disappointed Guests Talk About")
ax.legend(title="")
plt.tight_layout()
plt.savefig("output/guest_groups.png", dpi=150)
plt.close()

print("Charts saved to output/")