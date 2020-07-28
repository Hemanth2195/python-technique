#palindromic strings

S=input()
z=S[::-1]   #this gives the string s in the reverse order.
if S==z:
    print("YES")
else:
    print("NO")


#remember: 'hemanth'!='htnameh'
#even though both have same set of alphabets
