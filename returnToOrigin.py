class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        move_counts ={'U':0,'D':0,'L':0,'R':0}
        
        for move in moves:
            move_counts[move]+=1
        
        if move_counts['U'] == move_counts['D'] and move_counts['L'] == move_counts['R']:
            return True
        return False
        
        #determines if something at the origin returned back to origin on 2d plane. all moves equal value.
        
        #time: O(n),one pass through moves
        #space: O(n)
