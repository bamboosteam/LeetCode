class Solution:
    def countAndSay(self, n: int) -> str:
        MAX = 30
        sequences = {1:'1'}
        digit = '1'
        # Create the mountain of digits for count-n-say
        for i in range(MAX - 1):
            # Initiate value for count-n-say
            value = ''
            # Count-n-say the previous line
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
            # Update digit for next pile
            digit = value
            # Register the value and key as dictionary
            sequences[i + 2] = value
        return sequences[n]