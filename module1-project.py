import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/storms.csv"
df_storms = pd.read_csv(url)
# Save to a CSV file
# df_storms.to_csv('storms.csv', index=False)

fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(data=df_storms, 
                x="year", 
                y="status", 
                size="n", 
                hue="status",
                sizes=(20, 400),
                ax=ax)
plt.title("Storm Distribution with Size and Color Encoding")
plt.show()