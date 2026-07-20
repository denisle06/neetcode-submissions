import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #similarly, maintain a heap for each element. Bind the result of the 
        #euclidean distance to the element in a dictionary. Push the result
        #into a min heap. Return the value bind with the results



        distances = {}
        heap = []
        
        for x, y in points:
            dist = x*x + y*y
            distances[(x, y)] = dist
            heapq.heappush(heap, (dist, (x, y)))
        
        result = []
        for _ in range(k):
            d, point = heapq.heappop(heap)
            result.append([point[0], point[1]])
        
        return result