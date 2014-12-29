'''
Created on Dec 27, 2014

@author: chad
'''
from itertools import count
from test.test_typechecks import Integer
import sys
import operator

class PerfectPermutation(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        self.n = len(perm)
        self.perm = [ e for e in perm ]
        self.diff = sys.maxint
        '''
        self.n = 0
        self.perm = []
        self.diff = sys.maxint
    def noDupes(self, arr):
        return len(set(arr))==len(arr)
    def isSolution(self, solution):
        result = False
        if len(solution) == self.n:
            if self.noDupes(solution):
                c =self.getChild(solution)
                if self.noDupes(c):
                    result = True
        return result
    def candidates(self, solution):
        '''arbitrary choices for solution may yield child array elements that point into future.
        so we must constantly check to see if earlier child array elements now violate rules 
        to prune solution asap
        '''
        candidates = []
        prune = False
        if not prune: 
            for i in range(self.n):
                if not solution.count(i):
                    '''here we cannot check that our candidate would violate sanctity of child array
                    because the element we're about to add may look into future. instead we wait
                    until future becomes present to prune it. if it points to past/present now, 
                    the very next call will prune it.
                    '''
                    candidates.append(i)  
        return candidates
    
    def backtrack(self, solution):
        if not self.isSolution(solution):
            child = self.getChild(solution)
            childPresent = filter(lambda x : x != -1, child)
            prune = not self.noDupes(childPresent)
            if not prune:
                for cand in self.candidates(solution):
                    self.backtrack(solution + [cand])
        else:
#             print solution
            s =sum(map(bool, map(operator.sub, solution, self.perm)))
            self.diff = min(self.diff,s)
    
    def getChild(self, solution):
        child = [0]
        n = len(solution)
        for i in range(n-1):
            solutionIndex = child[i]
            #we can't know the future of our solution, so we use -1 in those, since it won't arise in our prune search.
            child.append(solution[solutionIndex] if solutionIndex < len(solution) else -1)
        return child
    
    def reorder(self, p):
        self.n = len(p)
        self.perm = p[:]
        self.backtrack([])
        return self.diff

if __name__ == "__main__":
#     p = PerfectPermutation([2, 0, 1, 4, 3])
#     p = PerfectPermutation([4, 2, 6, 0, 3, 5, 9, 7, 8, 1])
    p = PerfectPermutation()
    print p.reorder([4, 2, 6, 0, 3, 5, 9, 7, 8, 1])
        