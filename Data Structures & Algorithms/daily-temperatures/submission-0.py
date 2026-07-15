class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #the simplest solution would be, while traverse the array, we keep track
        #of every individual element's state. For every element that does not
        #have a warmer temperature, we compare it to the current element. 

        #How do I solve it using a stack? 
        #An intuitive solve would be to keep track of a stack for 
        #each individual element, but that's kinda the same
        
        #What if I want to evaluate it backward?
        #Treat the input array as a stack. The first pop automatically 0.
        #All later pop would be compare with current_min. If it is smaller than
        #curr_min, then its position would be in relative to curr_min_pointer.

        #the prev is wrong. Another approach: pop it into another array. When 
        #evaluating what is being pop, we traverse array to find it. nlogn solution
        #so three array. 

        #track the array:
        #30, 38, 30, 36, 35, 40, 28.
        #pop 28. -> 28 insert to array. Insert 0
        #pop 40 -> compare to array element. Find only 28. Insert 0
        #pop 35 -> compare to array element. Find 40 at position 0 -> insert 1
        #pop 36 -> compare to array element. Find 40 at position 1 -> insert 0

        #revert the array later

        element_array = []
        result_array = []
        element_array.append(temperatures.pop())
        result_array.append(0)
        
        while True:
            if len(temperatures) == 0:
                break
            curr = temperatures.pop()
            found = 0
            for n in element_array:
                if n > curr:
                    found = element_array.index(n) + 1
                    break
            element_array.insert(0, curr)
            result_array.append(found)

        return result_array[::-1]