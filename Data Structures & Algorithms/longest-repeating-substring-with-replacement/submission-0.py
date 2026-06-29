class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Sliding window technique. 
        #A complexity of O(n) means that it only pass one time only.
        #We need a way to detect the number of replacement inside a window.
        #The first pass is easy. We place two pointer near each other.
        #Incrementally increase j and record the the number of element
        #into a hashmap. If the number of unique element exceed 2, then stop

        #How do you detect if there is the maximum number of replacement has
        #been reached? One of the following condition apply:
        #There are more than 3 unique word.
        #If there are 3 unique word, if any two of them >= 2, then stop
        #If there are 2 unique word, if the smaller word count > 2, then stop

        #How do you forward pass in a normal string? If in a string with n character
        #already exist a substring of m character, we only need to find the substring
        #that larger or equal to it.

        #solution comprise of two part. First is applying sliding window. Second is
        #within the window, constantly keep track of the conditions above. Update the
        #state of the condition with each increment

        #Sequence of action: With the current i and j, check if the condition applied.
        #if yes, update i until it does not apply. Then update j up until j is the last
        #element. If i is updated, then the validation must run again. Essentially
        #it must run until i stop being updated. 

        #When will comparison happen? Every time j change, the length of current 
        #substring will need to be updated. However each time i change it is updated
        #to. And adding j is after the condition, so the verification may not be true

        #Thus it calls for the rearrangement of the condition. j should start at 0, and
        #j should be add first, then the verification. If it passed, that means we can
        #now update the length. What if it does not pass? Then we increment i until
        #it pass, then we update the length
        
        #WRONG CONDITION. THERE SHOULD BE K CHANGES NOT 2 CHANGES.
        #Rethink the logic: Loop through the dictionary's key and find the length of each element. Then
        #calculate if the sum of other element except for the largest one exceed k.
        #Other way: Calculate if k + max of list < length of list. If yes then i need to be updated

        if len(s) == 0: 
            return 0

        if len(s) == 1:
            return(1)

        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2

        i = 0
        j = 1
        longest_substring = 1
        track_char = {}
        track_char[s[i]] = 1

        while j < len(s):
            # print("Current j: ")
            # print(j)
            
            if s[j] in track_char.keys():
                current_count = track_char[s[j]]
                track_char[s[j]] = current_count + 1
            else:
                track_char[s[j]] = 1    
            
            while True:
                count_of_element = []
                for key in track_char.keys():
                    count_of_element.append(track_char[key])
                    # print("Appending: ")
                    # print(track_char[key])
                
                if k + max(count_of_element) < j - i + 1:
                    current_count = track_char[s[i]] 
                    track_char[s[i]] = current_count - 1
                    i+= 1
                else:
                    break

            longest_substring = max((j - i + 1), longest_substring)
            j += 1
        
        return longest_substring