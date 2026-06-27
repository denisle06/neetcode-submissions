class Solution:
    encode_key = {}
    strs_length = 0
    def encode(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs):
            Solution.encode_key[i] = strs[i]
            i += 1
        Solution.strs_length = len(strs)
        enc = "".join(strs)
        return enc
    def decode(self, s: str) -> List[str]:
        dec = []
        for i in range(0, Solution.strs_length ):
            dec.append(Solution.encode_key[i])
        return dec

