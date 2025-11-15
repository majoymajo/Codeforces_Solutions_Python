--Next Round--
n, k = map(int, input().split())
scores = list(map(int, input().split()))
 
cutoff = scores[k - 1]
advancers = 0
for score in scores:
    if score >= cutoff and score > 0:
        advancers += 1
 
print(advancers)
