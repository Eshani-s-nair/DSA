#https://neetcode.io/problems/is-anagram/question?list=neetcode150
#sol1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            count={}
            for i in s:
                if i in count:
                    count[i]+=1
                else:
                    count[i]=1
            for j in count:
                if j in t:
                    if count[j]==t.count(j):
                        continue
                    else:
                        return False
                else:
                    return False
                
            return True
        return False
#sol2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)
#sol3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS={}
        countT={}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT
#sol4
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            count[t[i]]=count.get(t[i],0)-1
        return all (v==0 for v in count.values())
        
        
        
            
            
        