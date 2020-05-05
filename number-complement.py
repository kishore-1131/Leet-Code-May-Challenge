class Solution:
    def findComplement(self, num: int) -> int:
        binary = "{0:b}".format(num)
        binary = binary.strip("")
        ones = ""
        n = len(binary)
        for i in range(n):
            ones += '1' if (binary[i]=='0') else '0'
        num = ones
        return int(num, 2)