class Solution:
    def isPalindrome(self, s: str) -> bool:
        first_list = []
        second_list = []
        for i in range(len(s)): 
            if s[i].isalnum():
                first_list.append(s[i].lower())
        

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                second_list.append(s[i].lower()) 
        

        first_string = "".join(first_list)
        second_string = "".join(second_list)

        if (first_string == second_string):
            return True
        else:
            return False

        