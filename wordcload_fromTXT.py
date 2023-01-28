from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Open the text file

with open('example.txt', 'r') as f:
    text = f.read()
    
# Generate the word cloud

wordcloud = WordCloud().generate(text)

# Display the word cloud

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()    
