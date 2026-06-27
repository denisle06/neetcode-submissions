class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #2-D matrix with integer target. Binary search = pick high + low and turn
        #high and low to median number each time. binary search within an array is
        #log(n). For a solution of log(m * n) then we need 2 binary search function.
        #one for the first array and one for the second array. The matrix is essentially
        #sorted in increasing order. 

        #approach. Two part solution. First part binary search in array. Get the first
        #and last number and assign it to low and high. Get the low + high / 2 and compare
        #it to the target. If higher, then low = result. If lower then high = result.
        #if the target is non-existent then declare that the number does not exist.

        #second part: Binary search in matrix. Get the first element of each array in the matrix
        #The target must exist in an array that has first element < target and first element of 
        #next array < target
        #Need to find the array first.
        #We not neccessaryly find the first element that match the target. We just need
        #to find the array that could contain the element first

        #under what condition an array could contain the target? We essentially need
        #to find the matrix that has the first integer <= target and the next first integer 
        #> the target. So that means we can use a for m in matrix and get the first int[i]
        #and compare it to first int [i+1]. The loop end whenever first int[i + 1] <= the
        #target
        
        
        #first attempt on searching a list is too big since the matrix could be veri big
        #Now we need to apply proper binary search on the matrix. Maybe we could apply
        #the same principle: Use the first int as the value for comparison
        
        #how do I adapt binary search to it? The goal is to find an array that has first int < target and next array has first int > target. So it is simpler than match target because we would always have an array to search nonetheless. The end condition would be low + 1 = high. 
        #And we will choose low atp. Still have edge case that low + high // 2 = low. Edge case 2 would be low > target. In that case return false

        numberMatrixNeedSearch = None
        
        highArrayIndex = len(matrix) - 1
        lowArrayIndex = 0
        
        findingArray = True
        
        while findingArray == True:
            midArrayIndex = (highArrayIndex + lowArrayIndex) // 2 
            if matrix[lowArrayIndex][0] > target:
                return False
            if highArrayIndex == lowArrayIndex:
                numberMatrixNeedSearch = lowArrayIndex
                findingArray = False
                break
            if highArrayIndex == lowArrayIndex + 1:
                if matrix[highArrayIndex][0] <= target:    
                    numberMatrixNeedSearch = highArrayIndex
                else:
                	numberMatrixNeedSearch = lowArrayIndex
                findingArray = False
                break
            
            if matrix[midArrayIndex][0] == target:
                return True
            elif matrix[midArrayIndex][0] > target:
                highArrayIndex = midArrayIndex
            else: 
                lowArrayIndex = midArrayIndex
            
        matrixNeedSearch = matrix[numberMatrixNeedSearch]
        
        high = len(matrixNeedSearch) - 1
        low = 0
        
        finding = True
        targetExist = False

        while finding == True:
            mid = (high + low) // 2
            if matrixNeedSearch[high] == target or matrixNeedSearch[low] == target:
                return True
            if high <= low + 1:
                finding = False
                break
            else:
                if matrixNeedSearch[mid] == target:
                    targetExist = True
                    finding = False
                    break
                elif matrixNeedSearch[mid] < target:
                    low = mid
                else:
                    high = mid  

        return targetExist