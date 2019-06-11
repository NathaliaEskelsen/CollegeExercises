class KindleBook:
    __totalBooksSold = 0
    __wordsPerScreen = 400

    def __init__(self, bookTitleIn, bookISBN, customerNameIn, currentPageIn = 0):
        self.bookTitle = bookTitleIn
        if len(bookISBN) == 17 and str(bookISBN).count("-") == 4:
            self.ISBN = bookISBN
        else:
            self.ISBN = "Unknown"

        self.customerName = customerNameIn
        if currentPageIn > 0:
            self.currentPage = currentPageIn
        else:
            self.currentPage = 0

        #Class Variables
        KindleBook.__totalBooksSold += 1


    def nextPage(self):
        self.currentPage += 1


    def prevPage(self):
        if self.currentPage > 0:
            self.currentPage -= 1


    def getNumberPages(self):
        file = open("alicewonder.txt", "r")
        text = file.read()
        file.close()
        text = text.split(" ")
        return round(len(text) / KindleBook.__wordsPerScreen,0)
    

    def getPage(self):
        file = open("alicewonder.txt", "r")
        text = file.read()
        file.close()
        startingPoint = self.currentPage * KindleBook.__wordsPerScreen
        endPoint = startingPoint + KindleBook.__wordsPerScreen
        page = text[startingPoint:endPoint]
        return page

    def bookDetails(self):
        print("************************************")
        print("*********** Kindle Book ************")
        print("************************************")
        print("Title:       ", self.bookTitle )
        print("ISBN:        ", self.ISBN)
        print("Customer:    ", self.customerName)
        print("Current Page:", self.currentPage)
        print("Total Pages :", self.getNumberPages())
        print("************************************")


# Testing
myBook = KindleBook("Alice In Wonderland","978-17-22107-15-4","Keith Quille")
myBook.bookDetails()
print(myBook.getPage())
myBook.nextPage()
myBook.nextPage()
myBook.bookDetails()
print(myBook.getPage())

