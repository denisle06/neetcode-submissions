class Solution:
    def isValid(self, s: str) -> bool:
        
        #Start handling string s from left to right. Set up a counter.
        #As long as there are no close brackets, open bracket will be transferred
        #into a stack. Whenever we encounter a close bracket, immediately poping
        #simultaneously from a stack. If the poped from the stack and the close
        #bracket from the list do not match, immediately return false. If one of 
        #the two array or stack have element remaining, then return false also

        #string length being odd indicate not enough brackets


        bracket = {"(": ")", "{": "}", "[": "]"}
        stack = []
        if s == "":
            return True

        for i in range(0, len(s)):
            if s[i] in bracket.keys():
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    opening = stack.pop()
                    if bracket[opening] != s[i]:
                        return False
                    else:
                        continue
        
        if len(stack) == 0:
            return True
        else:
            return False
        





