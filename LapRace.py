import csv

# stock 2D List
laps = []


def menu():
    print("\t\t***************************")
    print("\t\t*     Laps.ie Racing      *")
    print("\t\t***************************")
    print("\t\t* 1) Add Lap              *")
    print("\t\t* 2) Race Summary         *")
    print("\t\t* 3) Exit                 *")
    print("\t\t***************************")


def race_summary():
    currentBestResults = []
    allRacersNoDuplicates = []

    # this list will have duplicates (upto ten)
    allRacersWithDuplicates = [int(racer[0]) for racer in laps]

    # Loop gets unique numbers in the races list with no duplicates.
    for racer in allRacersWithDuplicates:
        # if its not in unique list add it
        if allRacersNoDuplicates.__contains__(racer) == False:
            allRacersNoDuplicates.append(racer)
    
    # for each unique racer, get fastest time and number of laps
    for racer in allRacersNoDuplicates:
        # set to default
        racerBestTime = None
        racerLaps = 0
        for item in laps:
            if int(item[0]) == racer:
                if racerBestTime == None or float(item[1]) < racerBestTime:
                    racerBestTime = float(item[1])
                racerLaps += 1
        currentBestResults.append([racer, racerBestTime, racerLaps])
    
    print("\n\n\t\t****************************************************************")
    print("\t\t*                            Race Summary                      *")
    print("\t\t****************************************************************")
    print("\t\t{0:<15}".format("Race Number") +
          "{0:<15}".format("Best Time") +
          "{0:<15}".format("Laps Complete"))
    for item in currentBestResults:
        print("\t\t{0:<15}".format(item[0]) +
          "{0:<15}".format(item[1]) +
          "{0:<15}".format(item[2]))




option = 0

# Import Cars before we begin
with open("laps.csv", "r") as file:
    laps = list(csv.reader(file))

# main menu loop
while option != 3:
    # run menu definition
    menu()
    option = int(input("\t\tPlease enter option:"))

    if option is 1:
        # sell a car
        print("\t\t***************************")
        print("\t\t*        Add Lap          *")
        print("\t\t***************************")
        raceNo = int(input("\t\tPlease racers number :"))
        allRacers = [int(racer[0]) for racer in laps]
        raceNoOccurances = 0
        for racer in allRacers:
            if racer == raceNo:
                raceNoOccurances +=1
        
        if raceNo > 0 and raceNo <= 100 and raceNoOccurances <= 10:
            lapTime = float(input("\t\tPlease lap time :"))
            laps.append([raceNo, lapTime])
        elif raceNoOccurances > 10:
            print("\t\tError: The racer has completed more than ten laps.")
        else:
            print("\t\tError: The racer number is not between 1 and 100.")
        print()

    elif option is 2:
        # Race Summary
        race_summary()
        print()

    elif option is 3:
        # Save file to CSV (overriding the original file)
        with open("laps.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(laps)
