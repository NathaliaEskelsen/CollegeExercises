class Table:

    tablesInUse = 0
    totalSales = 0

    def __init__(self, tableIn, seatsIn):
        self.tableNumber = tableIn
        self.maximumSeats = seatsIn
        self.totalBill = 0
        self.order = []
        self.isUsed = False
        self.isBooked = False


    def table_booking(self, numOfPeople):
        if numOfPeople <= self.maximumSeats:
            self.isBooked = True
        return True

    def seat_customers(self):
        if self.isBooked == True:
            self.isUsed = True
            Table.tablesInUse += 1
            return True
        else:
            return False

    def add_order(self, order_description, order_amount):
        self.totalBill += order_amount
        self.order.append(order_description)

    def get_cheque(self):
        Table.tablesInUse -= 1
        Table.totalSales += self.totalBill
        self.isUsed = False
        print("---------------")
        print("Table number:",self.tableNumber)
        print("Total bill:",self.totalBill)
        print("Bill Orders:")
        item = 1
        for i in self.order:
            print("Item",item,":", i)
            item+=1
        self.totalBill = 0
        self.order = []

table1 = Table(1,5)
table1.table_booking(4)
table1.seat_customers()
table1.add_order("Pizza", 15.20)
table1.add_order("Pasta", 19.20)
table1.add_order("Steak", 27.50)
table1.get_cheque()
