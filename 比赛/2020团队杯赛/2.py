class Solution:
    def expectNumber(self, scores) -> int:
        scores.sort()
        save = []
        num = scores[0]
        savenum = 1
        for i in range(1,len(scores)):
            
            if score != num:
                save.append(savenum)
                num = scores[i]
            else:
                savenum += 1
        count = 0
        for j in save:
            
            count += 
                    
