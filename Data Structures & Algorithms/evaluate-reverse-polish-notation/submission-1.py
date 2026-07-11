class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #reverse polish notation: 1 + 2 -> 1 2 +
        #have the target stack and the original stack
        #push from ori to target until we have an operand
        #then pop 2 element from stack and calculate result and push back
        #until theres nothing left and you have the original stack

        if tokens == []:
            return []

        store = []

        while True:
            if len(tokens) == 0:
                return int(store.pop())
            else:
                curr = tokens.pop(0)
                if curr == "+":
                    first = store.pop()
                    second = store.pop()
                    result = int(first) + int(second)
                    store.append(result)
                elif curr == "-":
                    first = store.pop()
                    second = store.pop()
                    result = int(second) - int(first)
                    store.append(result)
                elif curr == "*":
                    first = store.pop()
                    second = store.pop()
                    result = int(first) * int(second)
                    store.append(result)
                elif curr == "/":
                    first = store.pop()
                    second = store.pop()
                    result = int(second) / int(first) 
                    store.append(result)
                else:
                    store.append(curr)
            