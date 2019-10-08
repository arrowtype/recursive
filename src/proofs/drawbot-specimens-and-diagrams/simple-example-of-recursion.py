def makeType(daysLeft):
    print("just " + str(daysLeft) + " to make type!")
    if daysLeft >= 1:
        makeType(daysLeft - 1)
        
makeType(7)