alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
removed=[]

N = int(raw_input())
for i in xrange(N):
    word = raw_input()
    bla=len(alphabet)
    for j in xrange(bla):
        letter=alphabet[j]
        if word.find(letter) == -1:
            removed.append(letter)
solution = set(alphabet)-set(removed)
print len(solution)