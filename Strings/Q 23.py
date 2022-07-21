paragraph = input().split()

articles = ['a','an','the']

words_after_articles = []
for index,word in enumerate(paragraph):
    if word.lower() in articles:
        words_after_articles.append(paragraph[index+1])

if len(words_after_articles) > 0:
    print(*words_after_articles)
else:
    print(-1)
