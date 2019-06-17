# Ellis Mclaughlan | Hangman # 

# LIBARIES #
import time

# DICTIONARY #
# THIS COMMENT DID NOT EXIST BEFORE
gamer = {"gg":"Good Game.  A gesture of good sportsmanship","ezpz":"Short for easy peasy. Toxic people use this."}
# THIS COMMENT DID NOT EXIST BEFORE
# FUNCTIONS #
# THIS COMMENT DID NOT EXIST BEFORE
def cleanScreen():
    import os
    os.system('cls')
# THIS COMMENT DID NOT EXIST BEFORE
def displayOptions():
    # DISPLAY FRONT END#
    time.sleep(5)
    cleanScreen()
    print("""
    0 - Quit
    1 - Look Up a Gamer Term
    2 - Add a Gamer Term
    3 - Redefine a Gamer Term
    4 - Delete a Gamer Term
    5 - Display Full Dictionary
    """)
# THIS COMMENT DID NOT EXIST BEFORE
# THIS COMMENT DID NOT EXIST BEFORE
def chooseOption():
    choice = input(" Choice: ")
    print()
# THIS COMMENT DID NOT EXIST BEFORE
    #QUIT#
    if choice == "0":
        print(" Good Bye")
        return 0
# THIS COMMENT DID NOT EXIST BEFORE
    # RETRIVE DEFINITION #
    if choice == "1":
        term = input(" What would you like to translate?\n term: ")
        if term in gamer:
            definition = gamer[term]
            print("\n ",term,"means",definition)
        else:
            print("\n Sorry I don't know",term)

    # ADD NEW DEFINITION (K,V) #
    elif choice == "2":
        term = input(" What term do you want me to add?\n term: ")
        if term not in gamer:
            definition = input(" What is the definition?\n definition: ")
            gamer[term] = definition
            print(" \n",term,"has been added.")
        else:
            print(" \n",term,"already exists! Try Redefining instead.")

    # REDEFINE #
    elif choice == "3":
        term = input(" Which term would you like to redefine?\nterm: ")
        if term in gamer:
            definition = input(" New definition: ")
            gamer[term] = definition
            print("\n ",term,"has been updated to",definition)
        else:
            print("\n ",term,"does not exist! Try adding it.")
    
    # DELETE ENTRY #
    elif choice == "4":
        print(gamer)
        term = input("\n Which term do you want to delete?\n term: ")
        if term in gamer:
            print("\n ",term,"found in dictionary the definition is",gamer[term])
            x = input("\n Are you sure you want to delete the term?\nYES|NO\t: ")
            while x not in ["YES","NO"]:
                print("\n Invalid choice, answer with YES or NO")
            if x == "YES":
                del gamer[term]
                print("\n ",term,"successfully deleted!")
            else:
                print("\n Deletion of term",term,"cancelled.")

    
    # DISPLAY DICTIONARY #
    elif choice == "5":
        print("\n\n Posting dictionary...\n\n",gamer,"\n\n Done!")
        time.sleep(5)

    # UNKNOWN ENTRY #
    else:
        print("Sorry that choice was invalid, try again.")


    return 1


displayOptions()
ctrl = chooseOption()

while ctrl == 1:
    displayOptions()
    ctrl = chooseOption()

print("\n\nOperation finished")
