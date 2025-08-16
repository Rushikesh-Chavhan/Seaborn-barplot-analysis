# chart.py
# Author: 24f3002795@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Generate synthetic data
# -----------------------------
np.random.seed(42)

product_categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Toys", "Beauty"]
satisfaction_scores = [np.random.normal(loc=loc, scale=5, size=100) 
                       for loc in [78, 70, 74, 72, 68, 76]]

data = pd.DataFrame({
    "Category": np.repeat(product_categories, 100),
    "Satisfaction": np.concatenate(satisfaction_scores)
})

# -----------------------------
# 2. Set Seaborn style
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -----------------------------
# 3. Create barplot
# -----------------------------
plt.figure(figsize=(8, 8))  # ensures 512x512 with dpi=64
ax = sns.barplot(
    data=data,
    x="Category",
    y="Satisfaction",
    palette="viridis",
    ci="sd"   # show variability
)

# -----------------------------
# 4. Customize chart
# -----------------------------
ax.set_title("Average Customer Satisfaction by Product Category", fontsize=16, pad=20)
ax.set_xlabel("Product Category", fontsize=14)
ax.set_ylabel("Average Satisfaction Score", fontsize=14)
ax.set_ylim(0, 100)  # Satisfaction is usually 0-100 scale
plt.xticks(rotation=30, ha="right")

# -----------------------------
# 5. Save as PNG (512x512 px)
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # 8in * 64 dpi = 512 px
plt.close()
