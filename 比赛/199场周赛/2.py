

class Solution:
    def getFolderNames(self, names):
        nameset = dict(names)

        res = ['' for _ in range(len(names))]
        for i in range(len(names)):
            if names[i] in nameset and nameset[names[i]] == 0:
                res[i] = names[i]
            if names[i] in nameset and nameset[names[i]] > 0:
                res[i] = names[i] + '(' + str(nameset[names[i]]) + ')'
                nameset.add(res[i])

        return res



        
            