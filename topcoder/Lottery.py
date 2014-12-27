import math, operator
class Lottery:
    '''intended to solve TopCoder arena, SRM 144 DIV 1, 550 point problem'''
    def sortByOdds(self, rules):
        ruleArray = [ self.parseRuleString(s) for s in rules ]
        #sort the list of tuples by name, so subsequent stable sort keeps equal items sorted by name
        ruleArray = sorted(ruleArray,key=operator.itemgetter(0))
        answers = [ self.numTickets(*elm) for elm in ruleArray ]
        #sort it by most likely to win, equal items will sorted by name because sort is stable.
        answers = sorted(answers,key=operator.itemgetter(1),reverse=False)
        for t in answers:
            print '{:>20}:{:>20}'.format(*t) #TODO: convert to some kind of logger.
        return [elm[0] for elm in answers]
    def numTickets(self, name, choices, blanks, sorted, unique):
        assert( choices > blanks )
        ret = 0
        if not (sorted or unique):
            ret = math.pow(choices,blanks)
        else:
            func = self.perm if sorted else self.comb
            #why are we allowed to pick N first, 1 second, and still have N-2 remaining choices?
            n = choices if unique else choices+blanks-1
            k = blanks
            ret = func(n, k)
            print name, choices, n, k, ret
        return name, ret
    def parseRuleString(self, str):
        name, rules = tuple(str.split(':'))
        choices, blanks, sorted, unique = tuple(rules.strip().split(' '))
        return name, int(choices), int(blanks), sorted == 'T', unique == 'T'
    def comb(self, n, k):
        return math.factorial(n)/math.factorial(n-k)
    def perm(self, n, k):
        return self.comb(n,k)/math.factorial(k)
        
if __name__ == "__main__":
    l = Lottery()
    print l.parseRuleString('INDIGO: 93 8 T F')
    print l.sortByOdds(("INDIGO: 93 8 T F","ORANGE: 29 8 F T","VIOLET: 76 6 F F","BLUE: 100 8 T T","RED: 99 8 T T","GREEN: 78 6 F T","YELLOW: 75 6 F F",))