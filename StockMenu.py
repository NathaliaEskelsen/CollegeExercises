menuOption = 0
stock = []
while menuOption != 4:
    print("\t***********************")
    print("\t* Menu *")
    print("\t***********************")
    print("\t* 1) Add Stock *")
    print("\t* 2) Stock List *")
    print("\t* 3) Sale Stock *")
    print("\t***********************")
    print("\t* 4) Exit *")
    print("\t***********************")

    menuOption = int(input("\tPlease enter menu option:"))
    if menuOption == 1:

        stockId = input("Input stock ID")

        allIDs = [col[0] for col in stock] #SEARCH ALL IDS
        if allIDs.__contains__(stockId): #IF THE STOCK ID INPUT IS ON THE STOCK ID LIST:
            qtd = int(input("How many products would you like to add?"))
            stock[allIDs.index(stockId)][3] = int(stock[allIDs.index(stockId)][3]) + qtd #stock[row of the stock id][col quantity] += qtd
        else:
            stockDescription = input("Input stock description")
            stockPrice = input("Input stock sale price")
            stockQtd = input("Input stock quantity")
            stock.append([stockId,stockDescription,stockPrice,stockQtd])

    elif menuOption == 2:
        print()
        if len(stock) == 0:
            print("The list is empty!")

        print("{0:<15}".format("STOCK ID") + "{0:<15}".format("DESCRIPTION") + "{0:<15}".format("PRICE") + "{0:<15}".format("QUANTITY"))

        print("-" * 50)
        for row in stock:
            for column in row:

                print("{0:<15}".format(column), end="")
            print()

    elif menuOption == 3:
        productId = input("Please input the stock ID ")
        productQtd = int(input("Please input the stock quantity"))
        if productQtd <= 0:
            print("Please input a number of sales greater then 0")
        else:
            allIDs = [col[0] for col in stock]
            qtdID = int(stock[allIDs.index(productId)][3])
            if productQtd > qtdID:
                print("There is not enough stock for sale!")
            else:
                stock[allIDs.index(productId)][3] = int(stock[allIDs.index(productId)][3]) - productQtd
                print("The sale has been successful completed")

    elif menuOption == 4:
        print("Thank you for using the software! :D")
    else:
        print("Error - Please enter number between 1 and 4.")
