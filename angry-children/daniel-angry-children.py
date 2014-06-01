__author__ = 'sapiens'

n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
 ## Write code here to compute the answer using (n, k, candies)
result_start=max(candies[:k])-min(candies[:k])
result=result_start
for i in xrange(n-k):
    if result>max(candies[i:k+i])-min(candies[i:k+i]):
        result=max(candies[i:k+i])-min(candies[i:k+i])
min_diff = result

print min_diff