#https://neetcode.io/problems/anagram-groups/question?list=neetcode150
#sol1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        s=[]
        copy=[]
        for i in range(len(strs)):
            copy.append(strs[i])
        for i in range(len(strs)):
            if strs[i] in copy:
                s.append(strs[i])
                copy.remove(strs[i])
            for j in range(i+1,len(strs)):
                if len(strs[i])!=len(strs[j]):
                    continue
                elif sorted(strs[i])==sorted(strs[j]):
                    if strs[j] in copy:
                        s.append(strs[j])
                        copy.remove(strs[j])  
                else:
                    pass
            if s not in a :
                if s !=[]:
                    a.append(s)
                    s=[]
        return a
                    
                    

#sol2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sortedS="".join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

#sol3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())
        