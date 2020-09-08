class Solution:
    def countAndSay(self, n: int) -> str:
        MAX = 30
        sequences = {}
        digit = '1'
        sequences[1] = digit
        for i in range(MAX - 1):
            value = ''
            while digit:
                temp = digit[0]
                res = 0
                while temp == digit[res]:
                    res += 1
                    if res + 1 > len(digit):
                        break
                digit = digit.lstrip(digit[0])
                value += str(res)
                value += temp
            sequences[i + 2] = value

        return sequences[n]
