class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                x, y = stack.pop(), stack.pop()
                stack.append(x + y)
                continue
            elif i == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
                continue
            elif i == "*":
                x, y = stack.pop(), stack.pop()
                stack.append(x * y)
                continue
            elif i == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y/x))
                continue
            stack.append(int(i))
        return stack[0]