class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "D":
                stack.append(int(2 * stack[-1]))
            elif op == "C":
                stack.pop()
            elif op == "+":
                stack.append(int(stack[-1] + stack[-2]))
            else:
                stack.append(int(op))

        return sum(stack)
