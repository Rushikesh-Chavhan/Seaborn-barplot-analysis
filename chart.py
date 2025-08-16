import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Synthetic customer satisfaction data
data = {
    "Product Category": ["Electronics", "Clothing", "Furniture", "Groceries", "Toys"],
    "Satisfaction Score": [8.2, 7.5, 6.9, 8.7, 7.9]
}
df = pd.DataFrame(data)

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Fix figure size to 512×512 pixels
# Use exact dimensions: 4 inches at 128 DPI = 512 pixels
plt.figure(figsize=(4, 4), dpi=128)

# Create barplot
sns.barplot(data=df, x="Product Category", y="Satisfaction Score", palette="viridis")

# Titles and labels
plt.title("Average Customer Satisfaction by Product Category", fontsize=14)
plt.xlabel("Product Category")
plt.ylabel("Satisfaction Score")

# Save chart EXACTLY 512×512 px
plt.savefig("chart.png", dpi=128, bbox_inches=None, pad_inches=0)
