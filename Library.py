class Library:
    genre=[]
    books=0
    members=[]

    def __init__(self,gen,bks,membs):
        self.genre=gen
        self.books=bks
        self.members=membs

    def lend(self):
        self.books-=1
