class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleast(k):
            set1={}
            cons=0
            count=0
            low=0
            for high in range(len(word)):
                if word[high]=='a' or word[high]=='e' or word[high]=='i' or word[high]=='o' or word[high]=='u':
                    set1[word[high]] = set1.get(word[high], 0) + 1
                else:
                    if word[high]!='a' and word[high]!='e' and word[high]!='i' and word[high]!='o' and word[high]!='u':
                        cons+=1
                while len(set1)==5 and cons>=k:
                    
                    count+=len(word)-high
                    if word[low]=='a' or word[low]=='e' or word[low]=='i' or word[low]=='o' or word[low]=='u':
                        set1[word[low]]=set1.get(word[low],0)-1
                        if set1[word[low]]==0:
                            del set1[word[low]]
                    
                    else:
                        cons-=1
                    low+=1
                
            return count
        return atleast(k)-atleast(k+1)





