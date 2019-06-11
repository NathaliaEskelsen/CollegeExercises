#Exercise1 - write txt files

stock = input("Please enter name:")
while(len(stock) > 0):
    myFile = open("stock.txt", "a")
    singleEntry = [stock]
    myFile.write(stock+"\n")
    stock = input("Please enter name:")

#Exercise2 -read txt files

stockName = input("Input the stock you want to search")

file = open("stock.txt", "r")
text = file.read()
col = text.split("\n")

if col.__contains__(stockName):
    print("Yes")
else:
    print("NO")


file.close()

#Exercise3 - read csv file and manipulate data
import csv
with open("pima.csv", "r") as file:
    my2DListOfCSV = list(csv.reader(file))
    colPreg = [int(col[0]) for col in my2DListOfCSV] #1D LIST OF NUM OF TIMES PREG
    colThick = [int(col[3]) for col in my2DListOfCSV]  # 1D LIST OF MM OF THICKNESS


    averagePreg = sum(colPreg) / len(colPreg)
    maxPreg = max(colPreg)
    minPreg = min(colPreg)

    averageThick = sum(colThick) / len(colThick)
    maxThick = max(colThick)
    minThick = min(colThick)
    averageThickRound = round(averageThick, 2)
    averagePregRound = round(averagePreg)


print("SKIN FOLD THICKNESS")
print("AVERAGE: "+str(averageThickRound)+"mm")
print("MAX: "+str(maxThick)+"mm")
print("MIN: "+str(minThick)+"mm")
print()
print("TIMES OF PREGNANCY")
print("AVERAGE: "+str(averagePregRound)+ " times")
print("MAX: "+str(maxPreg)+ " times")
print("MIN: "+str(minPreg)+ " times")
