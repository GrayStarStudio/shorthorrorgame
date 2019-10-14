import sys #imports system functions that allow the use of sys.exit to end the program
def game_flow_a(): #this is the initial loop of the game
    action = input ("\nWhat will you do? ")
    while action == ("run"):
        print ("\nIt is still chasing you.")
        action = input ("\nWhat will you do? ")
    if action == ("run faster"): #this causes the "run faster" ending to happen in game_flow_a
        print ("\nYou are getting tired.")
        sys.exit(0)
    print ("\nYou can do nothing but run.")
    print ("\nIt is catching up to you.")
    game_flow_b()
def game_flow_b(): #this is the secondary loop of the game
    action = input ("\nWhat will you do? ")
    if action == ("run faster"):
        print ("\nYou are getting tired.")
        sys.exit(0)   
    while action != ("run"):
        print ("\nYou are not fast enough.""\n\nIt is catching up to you.")
        action = input ("\nWhat will you do? ")
        break
  #break allows game_Flow_b loop to end so that the run faster ending can be achieved. However it also causes the loop to break itself
  #meaning that the player will always return to game_flow_a after entering a command in game_flow_b  
    if action == ("run faster"):
        print ("\nYou are getting tired.")
        sys.exit(0)
    print ("\nIt is still chasing you.")    
    game_flow_a()
print ("You are being chased.")
game_flow_a()