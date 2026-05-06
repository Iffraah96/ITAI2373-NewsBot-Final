# Basic dataset exploration
print("📊 DATASET OVERVIEW")
print("=" * 50)
print(f"Total articles: {len(df)}")
print(f"Unique categories: {df['Category'].nunique()}")
print(f"Categories: {df['Category'].unique().tolist()}")
#print(f"Date range: {df['date'].min()} to {df['date'].max()}")
#print(f"Unique sources: {df['source'].nunique()}")

print("\n📈 CATEGORY DISTRIBUTION")
print("=" * 50)
category_counts = df['Category'].value_counts()
print(category_counts)

# Visualize category distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Category', order=category_counts.index)
plt.title('Distribution of News Categories')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 💡 STUDENT TASK: Add your own exploratory analysis here
# - Check for missing values
print("\n❗ MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

# - Analyze text length distribution
df['text_length'] = df['Text'].astype(str).apply(len)

print("\n📏 TEXT LENGTH STATS")
print("=" * 50)
print(df['text_length'].describe())

# - Examine source distribution
# - Look for any data quality issues
duplicates = df.duplicated().sum()
print(f"\n🔁 Duplicate rows: {duplicates}")

short_articles = df[df['text_length'] < 50]
print(f"\n⚠️ Very short articles (<50 chars): {len(short_articles)}")

print("\n⚖️ CATEGORY BALANCE (%)")
print((category_counts / len(df)) * 100)
