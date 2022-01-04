import collections

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = []
        length = len(strs)
        result = ''
        
        for i in strs:
            for j in range(len(i)):
                arr.append((j,i[j]))
                
        a = dict(collections.Counter(arr))
        k_arr = []
        
        for k,v in a.items():
            if v == length:
                k_arr.append(k)
        
        k_arr.sort(key=lambda x:x[0])
        
        for j in range(len(k_arr)):    
            if j==0 and k_arr[j][0] !=0:
                break
    
            if k_arr[j][0] !=j:
                break
            else:
                result = result + k_arr[j][1]
            
        print(result)
        return result