from Library import Library

techcamplib = Library(bks=1000,gen=['Drama','Music','Comedy','Dancing'],membs=['Brayo','Amran','Jose'])

print(techcamplib.books)
print(techcamplib.members)
print(techcamplib.genre)

techcamplib.lend()
print(techcamplib.books)
