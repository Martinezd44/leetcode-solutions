class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i = len(a)-1#loop through string a
        j = len(b)-1#loop through string B
        carry=0
        while (i>=0 or j>=0 or carry): # loop for going through a and b and if we have a carry
            diga = int(a[i]) if i >=0 else 0 # we convert it to a int from the string if its not greater than 0
            digb = int(b[j]) if j >=0 else 0

            total = diga + digb + carry # we add up all the totals

            result.append(str(total % 2)) #we mod this to get the binary of base 2 and find the carry
            carry = total // 2 # this is how we get the carry usually only gonna be 1

            i -=1
            j -=1

        return "".join(reversed(result)) # reverse the list since we worked left to right 
