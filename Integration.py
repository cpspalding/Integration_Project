"""This is my main file for this project."""
"""This program is a basic estimator for Spalding Carpet Cleaners, whether it's
 used by the customer or cleaner."""
__author__ = "Charles Spalding"
# Integration-Project
# My name is Charles Spalding but I prefer to be called Patrick.


def main():
    """This main function goes through the outline of the estimate, adding
    the singular carpet, tile, and upholstery estimates together influenced by
    the users choices."""
    print("Welcome to the basic estimating program for Spalding Carpet "
          "Cleaners!")
    print("Cleaners measure areas of room at a time, then multiply that by a")
    print("price seen fit for labor/size of job.")
    carpetChoice = input("Would user like to measure carpet?(yes or no):")
    yes = ['y', 'ye', 'yes', 'yess', 'yyes', 'yees']
    if carpetChoice in yes:
        not_number = True
        initialCarpet = 0
        while not_number:
            try:
                initialCarpet = float(input("How many square feet of carpet "
                                            "would user like "
                                            "cleaned?(Whole number/decimal):"))
                not_number = False
            except ValueError:
                print("Your input is invalid, please try again.")
        priceOfCarpet = carpet_estimate(initialCarpet)
        tileChoice = input("Are there also areas of tile and grout?"
                           "(yes or no):")
        if tileChoice in yes:
            not_number = True
            initialTile = 0
            while not_number:
                try:
                    initialTile = float(input("How many square feet of tile "
                                              "would user like cleaned?("
                                              "Whole number/decimal):"))
                    not_number = False
                except ValueError:
                    print("Your input is invalid, please try again.")
            priceOfTile = tile_estimate(initialTile)
            upholsteryChoice = input("Would user like to estimate upholstery"
                                     " as well?(yes or no):")
            if upholsteryChoice in yes:
                not_number = True
                initialUpholstery = 0
                while not_number:
                    try:
                        initialUpholstery = int(input("How many sofas would "
                                                      "user like cleaned?"
                                                      "(3 bottom cushions)"
                                                      "(Enter whole number or"
                                                      " 0):"))
                        not_number = False
                    except ValueError:
                        print("Your input is invalid, please try again.")
                totalUpholsteryPrice = upholstery_estimate(initialUpholstery)
                totalEstimate = (priceOfCarpet + priceOfTile +
                                 totalUpholsteryPrice)
                print("Your estimate for carpet is: $" +
                      format(priceOfCarpet, ".2f"),
                      ",tile is: ${0}, and upholstery is: ${1}".
                      format(format(priceOfTile, ".2f"),
                             format(totalUpholsteryPrice, ".2f")))
                print("Coming to a combined total of",
                      format(totalEstimate, '.2f'), "dollars.")
            else:
                print("User selected no upholstery.")
                print("Your estimate for carpet is: $" +
                      (format(priceOfCarpet, ".2f")),
                      "and tile is: $" + format(priceOfTile, '.2f'))
                print("Coming to a combined total of",
                      format(priceOfCarpet + priceOfTile, ".2f"), "dollars.")
        else:
            print("User selected no tile.")
            upholsteryChoice = input("Would user like to measure "
                                     "upholstery?(yes or no):")
            if upholsteryChoice in yes:
                not_number = True
                initialUpholstery = 0
                while not_number:
                    try:
                        initialUpholstery = int(input("How many sofas would "
                                                      "user like cleaned?"
                                                      "(3 bottom cushions)"
                                                      "(Enter whole number or "
                                                      "0):"))
                        not_number = False
                    except ValueError:
                        print("Your input is invalid, please try again.")
                totalUpholsteryPrice = upholstery_estimate(initialUpholstery)
                totalUpholsteryPlusCarpet = \
                    totalUpholsteryPrice + priceOfCarpet
                print("Your estimate for carpet is: $" +
                      format(priceOfCarpet, '.2f'),
                      ",upholstery is:$" + format(totalUpholsteryPrice, ".2f"))
                print("Coming to a combined total of",
                      format(totalUpholsteryPlusCarpet, '.2f'), "dollars.")
            else:
                print("User selected no upholstery.")
                print("Your estimate for carpet is",
                      format(priceOfCarpet, ".2f"), "dollars.")
    elif carpetChoice != 'yes':
        print("User selected no carpet.")
        tileChoice = input("Would user like to measure tile and grout?"
                           "(yes or no):")
        if tileChoice in yes:
            not_number = True
            initialTile = 0
            while not_number:
                try:
                    initialTile = float(input("How many square feet of tile "
                                              "would user like cleaned?("
                                              "Whole number/integer):"))
                    not_number = False
                except ValueError:
                    print("Your input is invalid, please try again.")
            totalTilePrice = tile_estimate(initialTile)
            upholsteryChoice = input("Would user also like to measure"
                                     " upholstery?(yes or no):")
            if upholsteryChoice in yes:
                not_number = True
                initialUpholstery = 0
                while not_number:
                    try:
                        initialUpholstery = int(input("How many sofas would"
                                                      " user like cleaned? ("
                                                      "3 bottom cushions)("
                                                      "Enter whole number or "
                                                      "decimal):"))
                        not_number = False
                    except ValueError:
                        print("Your input is invalid, please try again.")
                totalUpholsteryPrice = upholstery_estimate(initialUpholstery)
                totalTilePlusUpholstery = totalUpholsteryPrice + totalTilePrice
                print("Your estimate price for tile is: $" +
                      format(totalTilePrice, '.2f'),
                      "and upholstery is: $" +
                      format(totalUpholsteryPrice, ".2f"))
                print("For a combined total of",
                      format(totalTilePlusUpholstery, ".2f"), "dollars.")
            else:
                print("User selected no upholstery.")
                print("Your estimate price for tile is",
                      format(totalTilePrice, ".2f"), "dollars.")
        else:
            print("User selected no tile.")
            upholsteryChoice = input("Would user like to measure "
                                     "upholstery?(yes or no):")
            if upholsteryChoice in yes:
                not_number = True
                initialUpholstery = 0
                while not_number:
                    try:
                        initialUpholstery = int(
                            input("How many sofas would user like cleaned?"
                                  "(3 bottom cushions)(Enter whole number or"
                                  " 0):"))
                        not_number = False
                    except ValueError:
                        print("Your input is invalid, please try again.")
                totalUpholsteryPrice = upholstery_estimate(initialUpholstery)
                print("Your estimate price for upholstery is: $" +
                      format(totalUpholsteryPrice, ".2f"), "dollars.")
            else:
                print("User selected no upholstery.")
                print("I apologize for being no use.")
                print("Have a nice day!")


def carpet_estimate(start_carpet):
    """Function designed to add the first area of carpet (the parameter)
    with additional areas if necessary, then be multiplied by price per
    foot to figure out estimate"""
    additionalCarpet = input("Does user have additional carpet?(yes or no)")
    yes = ['y', 'ye', 'yes', 'yess', 'yyes', 'yees']
    if additionalCarpet in yes:
        feetOfCarpet = 1
        totalCarpet = 0
        print("Please continue adding areas of rooms until necessary.")
        print("When user would like to stop adding, enter the value 0.")
        while feetOfCarpet != 0:
            not_number = True
            while not_number:
                try:
                    feetOfCarpet = float(input(
                        "Insert how much additional square feet of carpet."
                        "(Whole number/Decimal):"))
                    not_number = False
                except ValueError:
                    print("Your input is invalid, please try again.")
            totalCarpet += feetOfCarpet
        totalCarpet = start_carpet + totalCarpet
    else:
        print("User selected no additional carpet.")
        totalCarpet = start_carpet
    carpetPrice = input(
        "Is it commercial or residential carpet?(commercial/residential):")
    commercialCarpet = float(.20)
    residentialCarpet = float(.30)
    residential = ['r', 're', 'res', 'resid', 'reside', 'residen', 'resident',
                   'residenti', 'residentia', 'residential', 'residientiall',
                   'rresidential']
    if carpetPrice in residential:
        print("User selected residential.")
        totalCarpetPrice = totalCarpet * residentialCarpet
    else:
        print("User selected commercial.")
        totalCarpetPrice = totalCarpet * commercialCarpet
    return totalCarpetPrice


def tile_estimate(start_tile):
    """Function designed to add the original area of tile (the
    parameter) with multiple other areas of tile if necessary,
    then be multiplied by price per foot to figure out estimate."""
    totalTile = 0
    additionalTile = input("Does user have additional tile?(yes or no):")
    yes = ['y', 'ye', 'yes', 'yess', 'yyes', 'yees']
    if additionalTile in yes:
        feetOfTile = 1
        print("Please continue adding areas of rooms until necessary.")
        print(
            "When user would like to stop adding sections of rooms, enter the"
            " value 0.")
        while feetOfTile != 0:
            feetOfTile = float(input("Insert square feet of tile for this"
                                     " additional section."
                                     "(Whole number/Decimal):"))
            totalTile += feetOfTile
        totalTile = totalTile + start_tile
    else:
        print("User selected no additional tile.")
        totalTile = start_tile
    tilePrice = input("Is it commercial or residential tile?"
                      "(commercial/residential):")
    residentialTile = float(.65)
    commercialTile = float(.55)
    residential = ['r', 're', 'res', 'resid', 'reside', 'residen', 'resident',
                   'residenti', 'residentia', 'residential', 'residientiall',
                   'rresidential']
    if tilePrice in residential:
        print("User selected residential.")
        totalTilePrice = totalTile * residentialTile
    else:
        print("User selected commercial.")
        totalTilePrice = totalTile * commercialTile
    return totalTilePrice


def upholstery_estimate(start_upholstery):
    """Function created to ask a series of questions to determine
upholstery estimate. There are many different types of upholstery so it
makes it difficult to give an estimate without seeing the furniture in
person"""
    not_number = True
    numberOfLoveSeats = 0
    while not_number:
        try:
            numberOfLoveSeats = int(
                input("How many love seats would user like cleaned?"
                      "(2 bottom cushions)(Enter whole number or 0):"))
            not_number = False
        except ValueError:
            print("Your input is invalid, please try again.")
    not_number = True
    numberOfRecliners = 0
    while not_number:
        try:
            numberOfRecliners = int(
                input("How many recliners would user like cleaned?/"
                      "(1 bottom cushion)(Enter whole number or 0):"))
            not_number = False
        except ValueError:
            print("Your input is invalid, please try again.")
    not_number = True
    numberOfPillows = 0
    while not_number:
        try:
            numberOfPillows = int(
                input("How many pillows would user like cleaned?"
                      "(Enter whole number or 0):"))
            not_number = False
        except ValueError:
            print("Your input is invalid, please try again.")
    not_number = True
    numberOfOttomans = 0
    while not_number:
        try:
            numberOfOttomans = int(
                input("How many ottomans would user like cleaned?"
                      "(Enter whole number or 0):"))
            not_number = False
        except ValueError:
            print("Your input is invalid, please try again.")
    not_number = True
    numberOfDiningChairs = 0
    while not_number:
        try:
            numberOfDiningChairs = int(
                input("How many dining room chairs would user"
                      " like cleaned?(Enter whole number or 0):"))
            not_number = False
        except ValueError:
            print("Your input is invalid, please try again.")
    biggerThanThat = input("Do you have any couches larger than previously"
                           " described?(yes or no):")
    yes = ['y', 'ye', 'yes', 'yess', 'yyes', 'yees']
    if biggerThanThat in yes:
        biggerCushions = int(input("How many bottom cushions does it have?:"))
        totalUpholsteryPrice = (start_upholstery * 85) + \
                               (numberOfLoveSeats * 65) + \
                               (numberOfRecliners * 45) + \
                               (20 * biggerCushions + 25) + \
                               (numberOfDiningChairs * 10) + \
                               (numberOfPillows * 5) + (numberOfOttomans * 15)
    else:
        print("You selected no larger couches.")
        totalUpholsteryPrice = (start_upholstery * 85) + \
                               (numberOfLoveSeats * 65) + \
                               (numberOfRecliners * 45) + \
                               (numberOfDiningChairs * 10) + \
                               (numberOfPillows * 5) + (numberOfOttomans * 15)
    return totalUpholsteryPrice


main()
