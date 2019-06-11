myList = []
percentage = 0
total = 0

print("Please insert the candidate information!")
for fot in range(4):
    name = input("Candidate's name:")
    votes = int(input("Number of votes:"))
    constituency = input("Candidate's constituency:")
    print("Thank you!")
    myList.append([name,votes,constituency])
    total += votes

print("{0:<10}".format("Name") + "{0:<10}".format("Votes") + "{0:<10}".format("Constituency") + "{0:<10}".format("%%%%%%"))
print("-----------------------------------------------")
counter = 0
for info in myList:
    for each in info:
        if type(each) == int:
            percentage = (100 * each) / total
        print("{0:<10}".format(each), end="")
    print(percentage)
    print()

winner = myList[0][1]
loser = myList[0][1]
indexWinner = 0
indexLoser = 0

for index, candidates in enumerate(myList):
    if candidates[1] > winner:
        winner = candidates[1]
        indexWinner = index
    if candidates[1] < loser:
        loser = candidates[1]
        indexLoser = index


print("Winner is: ", myList[indexWinner][0])
print("Loser is: ", myList[indexLoser][0])
