class BrowserHistory:

    def __init__(self, homepage: str):
        self.save = [homepage]
        self.visitnum = -1

    def visit(self, url: str) -> None:
        if self.visitnum == -1: self.save.append(url)
        else:
            self.save = self.save[:self.visitnum+1]
            self.save.append(url)
        self.visitnum = -1


    def back(self, steps: int) -> str:

        if 0 > self.visitnum - steps >= - len(self.save):
            self.visitnum -= steps
            return self.save[self.visitnum]

        if self.visitnum - steps < - len(self.save):
            self.visitnum = - len(self.save)
            return self.save[self.visitnum]

    def forward(self, steps: int) -> str:
        
        if 0 > self.visitnum + steps>= - len(self.save):
            self.visitnum += steps
            return self.save[self.visitnum]

        if self.visitnum + steps >=0 :
            self.visitnum = -1
            return self.save[self.visitnum]

a = BrowserHistory("leetcode.com")
print(a.visit("1.com"))
print(a.visit("2.com"))
print(a.visit("3.com"))
print(a.back(2))
print(a.visit("4.com"))
print(a.back(10))
print(a.visit("5.com"))
print(a.back(1))
