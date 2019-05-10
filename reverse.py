def reverse(self,head):
    prev= None
    cur = head
   
    
    if head is None or head.next is None:
        return head
   
    next = head.next     
        
    while cur is not None:
        #real_next = next.next #saving next.next value for moving forward
        next = cur.next #save cur.next since i will be changing that
        cur.next=prev #pointing it backwards
        prev= cur #   
        cur = next
        #next = next.next 
    
    
    return prev #
