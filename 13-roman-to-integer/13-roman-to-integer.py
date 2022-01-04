class Solution:
    def romanToInt(self, s: str) -> int:
        s_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        exp_map = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        
        cal = []
        
        for k in exp_map.keys():
            if k in s:
                cal.append(s.count(k)*exp_map[k])
                s=s.replace(k,'')
        
        for i in s:
            for k in s_map.keys():
                if i == k:
                    cal.append(s_map[i])
                    break
            
        result = sum(cal)
        #print(result)
        
        return result
        