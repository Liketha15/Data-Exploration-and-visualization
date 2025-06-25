import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer

# Step 2: Load the dataset
df = pd.read_csv(r'C:\Users\user\Downloads\spam.csv', encoding='latin-1')

# Step 3: Understand the dataset structure
print("First few rows of the dataset:")
print(df.head())  # Display first 5 rows

print("\nDataset information (columns, types, and non-null counts):")
print(df.info())  # Check the data types, null values

print("\nStatistical summary of the dataset:")
print(df.describe())  # Get descriptive statistics

# Step 4: Check for null/missing values
print("\nMissing values in each column:")
print(df.isnull().sum())  # Check for missing values

# Step 5: Analyze class distribution (spam vs ham)
# Explicitly assign 'v1' to the hue argument to avoid the FutureWarning
plt.figure(figsize=(8, 6))
sns.countplot(x='v1', data=df, hue='v1', palette='viridis', legend=False)
plt.title('Class Distribution (Ham vs Spam)')
plt.xlabel('Label')
plt.ylabel('Count')
plt.show()

# Step 6: Visualize data distribution using plots
# Adding a new column for message length
df['message_length'] = df['v2'].apply(len)  # Assuming 'v2' contains the message text

# Plot the distribution of message lengths
plt.figure(figsize=(10, 6))
sns.histplot(df['message_length'], bins=50, kde=True, color='blue')
plt.title('Distribution of Message Lengths')
plt.xlabel('Message Length')
plt.ylabel('Frequency')
plt.show()

# Step 7: Perform text-specific analysis
# 7a. Message length statistics
average_length = df['message_length'].mean()
median_length = df['message_length'].median()
std_length = df['message_length'].std()

print(f"\nAverage message length: {average_length}")
print(f"Median message length: {median_length}")
print(f"Standard deviation of message length: {std_length}")

# 7b. Word frequency analysis (word clouds)
# Split dataset into spam and ham messages
spam_messages = df[df['v1'] == 'spam']['v2']  # 'v1' for label, 'v2' for message text
ham_messages = df[df['v1'] == 'ham']['v2']

# Create word cloud for spam messages
spam_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(spam_messages))
plt.figure(figsize=(10, 6))
plt.imshow(spam_wordcloud, interpolation='bilinear')
plt.title("Word Cloud for Spam Messages")
plt.axis('off')
plt.show()

# Create word cloud for ham messages
ham_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(ham_messages))
plt.figure(figsize=(10, 6))
plt.imshow(ham_wordcloud, interpolation='bilinear')
plt.title("Word Cloud for Ham Messages")
plt.axis('off')
plt.show()

# 7c. Word frequency analysis (top words)
vectorizer = CountVectorizer(stop_words='english', max_features=10)

# Get the most frequent words in spam messages
spam_words = vectorizer.fit_transform(spam_messages).toarray()
spam_word_freq = pd.DataFrame(spam_words, columns=vectorizer.get_feature_names_out()).sum(axis=0).sort_values(ascending=False)

# Get the most frequent words in ham messages
ham_words = vectorizer.fit_transform(ham_messages).toarray()
ham_word_freq = pd.DataFrame(ham_words, columns=vectorizer.get_feature_names_out()).sum(axis=0).sort_values(ascending=False)

# Display the top 10 frequent words in spam and ham
print("\nTop 10 words in Spam messages:\n", spam_word_freq.head(10))
print("\nTop 10 words in Ham messages:\n", ham_word_freq.head(10))

# Step 8: Check correlations (if any)
# Correlation between message length and whether it's spam or ham
df['is_spam'] = df['v1'].apply(lambda x: 1 if x == 'spam' else 0)
correlation = df[['message_length', 'is_spam']].corr()
print("\nCorrelation between message length and spam/ham:\n", correlation)
