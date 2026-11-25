# Logical Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Terminal-specific Libraries
from readchar import readkey as rk # Navigating Menus
from clear import clear # Clears the terminal.
from termcolor import colored as tcol # Text colour in Python

"""
###############################
# PANDAS: INIT + READ / WRITE #
###############################
"""

df = pd.read_csv('product_details.csv', skipinitialspace=True) # Initialise Pandas (specifying DataFrame)


# Reads data from specific row

def readPandas(row):
    # row = Product by order ID (in order of how its stored in CSV)

    ############################## LIST #################################
    #               0         1        2      3         4         5     #
    # rowData = [Product, Condition, Stock, Loaned, LoanPeriod, Price]  #
    #####################################################################

    rowData = df.loc[row, df.columns].tolist()
    return rowData


# Writes data to specific row

def writePandas(row, data):
    # row = Product by order ID (in order of how its stored in CSV)
    # data = [Product, Condition, Stock, Loaned, LoanPeriod, Price]

    ############################## LIST #################################
    #               0         1        2      3         4         5     #
    # rowData = [Product, Condition, Stock, Loaned, LoanPeriod, Price]  #
    #####################################################################

    df.loc[row, df.columns] = data # Passes data array contents into the selected row.

    # Save the modified data
    df.to_csv('product_details.csv', index=False)



""" 
############################
# SHARED PROGRAM FUNCTIONS #
############################
"""


def windowTitle(screenTitle): # Handles banner logic for all windows (Branding + Screen Title)

    # Variable: screenTitle - STRING - Used to hold the title of the actual 'screen' the user visits.

    print(tcol("==========================================", "light_yellow", "on_blue"))
    print(tcol("QL Ltd.".center(42, " "), "light_yellow", "on_blue"))
    print(tcol("==========================================", "light_yellow", "on_blue"))
    print(tcol("||||||||||||||||||||||||||||||||||||||||||", "white", "on_white")) # Spacing - Text is black on some IDEs for readability which I cant change.
    print(tcol("==========================================", "light_yellow", "on_blue")) 
    print(tcol(screenTitle.center(42, " "), "light_yellow", "on_blue")) # Outputs content of title variable and centers it to middle of UI (42 chars == Length of barriers)
    print(tcol("==========================================", "light_yellow", "on_blue"))
    print("\n") # Double Blank line - Spacing



class dialogs(): # ERROR HANDLING CODE - Used a class to sort of 'group' all of the areas into one section but serves no other real purpose.
    
    # Function: invalidData - Throws 'Invalid Input' Error Message
    # Function: noExist - Throws 'Option doesn't exist' Error Message
    # Variable: returnFunction - The data is a function name so this shared function knows what screen to return to afterwards.

    def invalidData(returnFunction):
        print(tcol("[ERROR]", "red", attrs=["bold"]), "Invalid input. Please try again.\n")
        print(tcol("[PRESS ANY KEY TO CONTINUE]", "light_yellow", "on_blue"))
        rk() # Pause
        returnFunction()


    def noExist(returnFunction):
        print(tcol("[ERROR]", "red", attrs=["bold"]), "This option does not exist. Please try again.\n")
        print(tcol("[PRESS ANY KEY TO CONTINUE]", "light_yellow", "on_blue"))
        rk() # Pause
        returnFunction()


    def insufficientStock(returnFunction):
        print(tcol("[ERROR]", "red", attrs=["bold"]), "Insufficent Stock. You are trying to return more items than are currently available. Please try again.\n")
        print(tcol("[PRESS ANY KEY TO CONTINUE]", "light_yellow", "on_blue"))
        rk() # Pause
        returnFunction()

    def recordsUpdated(returnFunction):
        print(tcol("[SUCCESS]", "green", attrs=["bold"]), "Records Updated Successfully!\n")
        print(tcol("[PRESS ANY KEY TO CONTINUE]", "light_yellow", "on_blue"))
        rk()
        returnFunction()


    def cancelOperation(reason):
        print(tcol("[WARN]", "yellow", attrs=["bold"]), "The operation could not be completed.", reason, "\nYou will now be directed to the Main Menu.\n")
        print(tcol("[PRESS ANY KEY TO CONTINUE]", "light_yellow", "on_blue"))
        rk() # Pause
        mainMenu()



def getCharSelection(returnFunction, message, type=int):

    # Variable: returnFunction - The data is a function name so this shared function knows what screen to return to afterwards.

    print("------------------------------------------")
    print(message) # Underscores added to help signal to the user they need to input something.
    choice = rk() # gather single character.
    print("------------------------------------------\n") # Barrier
    try:
        choice = type(choice)
    except:
        dialogs.invalidData(returnFunction)
    return choice



def getStringSelection(returnFunction, message, type=str):

    # Variable: returnFunction - Stores function to call when error occurs
    # Variable: message - Stores custom input message.
    # Variable: type - stores data type conversion command.

    print("------------------------------------------")
    choice = input(message)
    print("------------------------------------------")

    try:
        choice = type(choice)
    except:
        dialogs.invalidData(returnFunction)
    return choice

    

def productSelection(returnFunction):

    # Function: getCharSelection - Gets user's character input and feeds the value back in integer format.
    # Class: dialogs - Stores all error messages in a group (I probably could've avoided using a class as it wasn't used for its proper purpose. But I think grouping errors makes it more readable.)
    # Variable: choice - fetches user choice inputted info after function returns data

    print("1.  Laptops      |   4.  Raspberry Pi Kits")
    print("2.  Cameras      |   5.  Networking Kits")
    print("3.  Microphones  |   6.  VR Headsets")

    productChoice = getCharSelection(returnFunction, "Enter Choice [1-6]: ____")

    try:
        productChoice = int(productChoice)
    except:
        dialogs.invalidData(returnFunction)

    productChoice -= 1 # Index starts at 0 when its a list or Pandas. so I have to shift the user's input slightly. 

    if not (productChoice >= 0 and productChoice <= 6): # Input Validation Check
        dialogs.noExist(returnFunction)


    return productChoice # Passes all data back in list format. (0-6)



""" 
###########################
# ACTUAL SCREEN FUNCTIONS #
###########################
"""


# Main Menu


def mainMenu():

    # Class: dialogs - Stores all error messages in a group.
    # Function: getCharSelection - Gets user's character input and feeds the value back in integer format.
    # Function: equipmentMenu - Calls the equipment menu function
    # Variable: choice - fetches user choice inputted info after function returns data

    clear()
    windowTitle("Main Menu")
    print("1. View Equipment")
    print("2. Loan / Return Equipment")
    print("3. Display Visual Summary")
    print("4. Exit Application")

    choice = getCharSelection(mainMenu, "Enter Choice [1-4]: ____")

    if choice == 1:
        equipmentMenu()
    elif choice == 2:
        loanReturnMenu()
    elif choice == 3:
        visualSummary()
    elif choice == 4:
        print("Goodbye!")
        exit()
    else:
        dialogs.invalidData(productSelection)


# Equipment Menu


def equipmentMenu():
    clear() # Clears previous screen
    windowTitle("Equipment Menu") # Spawns banner + title on screen.

    rowID = productSelection(equipmentMenu) # List products + Get Selection

    ############################## LIST ################################
    #               0         1        2      3         4         5    #
    # csvRow = [Product, Condition, Stock, Loaned, LoanPeriod, Price]  #
    ####################################################################
    
    csvRow = readPandas(rowID)


    print("SELECTED:", csvRow[0])           # Product | Index 0
    print("Condition:", csvRow[1])          # Condition | Index 1
    print("Remaining Stock:", csvRow[2])    # Stock | Index 2
    print("Price: £" + str(csvRow[5]))      # Price | Index 5

    print("\n", tcol("[PRESS ANY KEY TO CONTINUE]", "light_yellow", "on_blue")); rk()
    mainMenu()

def loanReturnMenu():
    clear()
    windowTitle("Loan / Return Equipment")

    rowID = productSelection(loanReturnMenu) # Outputs Products + Gets Selection

    ############################## LIST ################################
    #               0         1        2      3         4         5    #
    # csvRow = [Product, Condition, Stock, Loaned, LoanPeriod, Price]  #
    ####################################################################

    csvRow = readPandas(rowID)

    print("SELECTED:", csvRow[0]) # Product

    LRMChoice = getStringSelection(loanReturnMenu, "Enter Choice [LOAN / RETURN / MENU]: ", str) # LRM Choice = Loan / Return / Menu Choice

    LRMChoice = LRMChoice.lower() # Takes user input and puts the answer in lowercase to prevent user confusion (i.e if they type with a capital letter)

    if LRMChoice == "loan":



        """
        #################
        #  LOAN CHOICE  #
        #################
        """

        print("How many items are you borrowing?")
        borrow = getStringSelection(loanReturnMenu, "Enter Number: ", int)

        print("\nEquipment Condition:", csvRow[1])
        print("Equipment Stock:", csvRow[2])
        print("Loan Period:", csvRow[4])
        print("Total Cost:", (csvRow[5] * borrow)) # Show User total cost.
        
        print("\n Do you want to continue?")
        choice = getCharSelection(loanReturnMenu, "Enter Choice [Y / N]: ____", str)
        choice.lower() # Turns user input lowercase.

        if choice == "y": # User agrees to continue with transaction

            #Stock Validation Logic
            newStock = csvRow[2] - borrow   # Stock  | Index 2
            newLoan = csvRow[3] + borrow    # Loaned | Index 3

            if newStock < 0:
                dialogs.insufficientStock(loanReturnMenu)
            else:
                # PANDAS UPDATE LOGIC HERE

                ############################## LIST ################################
                #               0         1        2      3         4         5    #
                # csvRow = [Product, Condition, Stock, Loaned, LoanPeriod, Price]  #
                ####################################################################


                writePandas(
                    row = rowID, #Row ID - Declared at top of function.
                    data = [csvRow[0], csvRow[1], newStock, newLoan, csvRow[4], csvRow[5]] # Rewrites entire record but with modifications
                    )

                dialogs.recordsUpdated(mainMenu) # Redirects to Main Menu due to Finished Interaction

        elif choice == "n": # User disagrees with transaction (Cancel)
            dialogs.cancelOperation(reason = "You have cancelled the operation.")



        """
        #################
        # RETURN CHOICE #
        #################
        """

    elif LRMChoice == "return":
        print("\nHow many items are you returning?")
        returning = getStringSelection(loanReturnMenu, "Enter Number: ", int)
        
        #Stock Validation Logic
        newStock = csvRow[2] + returning   # Stock  | Index 2
        newLoan = csvRow[3] - returning    # Loaned | Index 3

        # VALIDATION LOGIC HERE - I can't think what it is off the top of my head I need to check for at the moment

        # Loaned can't go below 0. Reject input if 'loaned' goes below 0.

        if newLoan < 0:
            dialogs.insufficientStock(loanReturnMenu)
        else:
            
            ############################## LIST ################################
            #               0         1        2      3         4         5    #
            # csvRow = [Product, Condition, Stock, Loaned, LoanPeriod, Price]  #
            ####################################################################

            writePandas(
                row = rowID,
                data = [csvRow[0], csvRow[1], newStock, newLoan, csvRow[4], csvRow[5]]
            )

            dialogs.recordsUpdated(mainMenu) # Redirect as interaction has been completed.

        """
        ###############
        # MENU CHOICE #
        ###############
        """


    elif LRMChoice == "menu": # User accessible way to access Main Menu
        mainMenu()
    
    else:
        dialogs.noExist(loanReturnMenu)



def visualSummary():
    clear()
    windowTitle("Visual Summary Menu")

    rowID = productSelection(visualSummary)

    ############################## LIST ################################
    #               0         1        2      3         4         5    #
    # csvRow = [Product, Condition, Stock, Loaned, LoanPeriod, Price]  #
    ####################################################################

    csvRow = readPandas(rowID) # Get all the data

    plt.title("Summary of " + csvRow[0] + "s")

    labels = ["Available Stock", "Loaned"]
    data = [csvRow[2], csvRow[3]]

    plt.bar(labels, data) # Plot labels + data

    plt.show() # Present the graph.


    print(tcol("[PRESS ANY KEY TO CONTINUE]", "light_yellow", "on_blue")); rk() # My equivalent to CMD 'pause' command... but with colour.
    mainMenu()

# Script execution starts here!!!
mainMenu()