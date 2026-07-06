class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i = 0
        j = len(s1)
        instances = {}
        for s in s1:
            if s in instances.keys():
                instances[s] += 1
            else:
                instances[s] = 1

        while True:
            if j == len(s2) + 1:
                return False
            else:
                s2_instances = {}
                for s in range(i, j):
                    if s2[s] in s2_instances.keys():
                        s2_instances[s2[s]] += 1
                    else:
                        s2_instances[s2[s]] = 1

                permutation = True
                for ins in instances.keys():
                    if ins not in s2_instances.keys():
                        permutation = False
                        break
                    else:
                        if s2_instances[ins] != instances[ins]:
                            permutation = False
                            break

                if permutation:
                    return True

                i += 1
                j += 1