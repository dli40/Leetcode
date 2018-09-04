class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range (1,n+1):
            x = ''
            if i%3==0:
                x+= 'Fizz'
            if i%5==0:
                x+= 'Buzz'
            if i %3 != 0 and i%5 !=0:
                x+= str(i)
            ans.append(x)    
        return ans        
            
        #analysis
        '''Time: O(n)
        Space: O(n)
        Switch might be faster? But doesn't make that much of a difference'''
