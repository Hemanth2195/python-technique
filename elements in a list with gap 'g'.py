#printing sum of elemnts in a list with gap 'g' from index 'i' :sum(l[i::g])

l=list(map(int,input().split()))
print(sum(l[0::3]))
