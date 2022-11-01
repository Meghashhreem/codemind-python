s=input()
s=list(s)
for i in range(len(s)):
    if s[i]=='6':
         s[i]='9'
         break
s="".join(s)
print(s)
        