import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #maintain a min heap with size k. For each pass, compare it with min of heap
        #If it is larger than min of heap, put it in. Pop the min of heap for answer
        min_heap = []
        heapq.heapify(min_heap)

        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                if n > min_heap[0]:
                    heapq.heappushpop(min_heap, n)

        return min_heap[0]