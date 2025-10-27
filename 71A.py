----Way Too Long Words----

num_words = int(input())
for _ in range(num_words):
    word = input().strip()
    if len(word)>10:
        print(word[0]+ str(len(word)-2)+word[-1])
    else:
        print(word)
