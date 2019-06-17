import csv
from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
from collections import Counter
file_name="sentiment.csv"
with open(file_name, 'r') as data:
 counter = Counter()
 for row in csv.DictReader(data):
    counter[row['Sentiment']] += 1
 positive = counter['positive']
 negative = counter['negative']
 neutral = counter['neutral']
## declare the variables for the pie chart, using the Counter variables for "sizes"
colors = ['green', 'red', 'grey']
sizes = [positive, negative, neutral]
labels = 'Positive', 'Negative', 'Neutral'

## use matplotlib to plot the chart
plt.pie(
 x=sizes,
 shadow=True,
 colors=colors,
 labels=labels,
 startangle=90
)
plt.title("Sentiment of User's Tweets about cancer")
plt.show()