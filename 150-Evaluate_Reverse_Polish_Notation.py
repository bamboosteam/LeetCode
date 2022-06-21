class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ope = ["+", "-","/","*"]
        
        idx = 0
        
        while len(tokens) > 1:
            if tokens[idx] in ope:
                if tokens[idx] == "+":
                    tokens[idx-2] = str(int(tokens[idx-2]) + int(tokens[idx-1]))
                elif tokens[idx] == "-":
                    tokens[idx-2] = str(int(tokens[idx-2]) - int(tokens[idx-1]))
                elif tokens[idx] == "/":
                    tokens[idx-2] = str(int(int(tokens[idx-2]) / int(tokens[idx-1])))
                else:
                    tokens[idx-2] = str(int(tokens[idx-2]) * int(tokens[idx-1]))
                del tokens[idx-1:idx+1]
                idx -= 2
            idx += 1
        
        return tokens[0]