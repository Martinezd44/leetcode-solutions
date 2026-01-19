class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        
        if not l1 and not l2 and carry==0:
            return None
        
        val1 = l1.val if l1 else 0 #gets the curr value from the linked list
        val2 = l2.val if l2 else 0
  
        total = val1 + val2 + carry # gets the sum
        new_carry = total//10 #new carry
        digit = total%10 #what single digit is the carry

        result = ListNode(digit) # get the digit to the linked list

        result.next = self.addTwoNumbers(l1.next if l1 else None, 
        l2.next if l2 else None,new_carry)
 #recursive call
        return result
