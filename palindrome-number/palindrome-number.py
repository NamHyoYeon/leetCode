class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = False
        str_list =  [ i for i in str(x)]
        str_reverse = list(reversed(str_list))
        print(str_list)
        print(str_reverse)
        if ''.join(str_list) == ''.join(str_reverse):
            result = True

        return result
            
        