"""
Course: Introduction to Python Programming
Instructor: liang@cs.miami.edu
Student:
"""
# %% always put import statements at the very beginning


# %%
def HumanPlayer():
    instructions = ('Type "r" for rock, "p" for paper, or "s" for scissors.\n'
    'To print the record of the game, type "record".  To quit, type "quit".')
    print(instructions)
    choosing = True
    while choosing:
        choice = input('Your move: ')
        if choice=='r':
            return 'rock'
        elif choice == 'p':
            return 'paper'
        elif choice == 's':
            return 'scissors'
        elif choice == 'record':
            return 'record'
        elif choice == 'quit':
            return 'quit'
        else:
            print('Unknown command, please enter either r, p, s, record, or quit.')
        
#HumanPlayer(0)
    
    
    
    
    # Parameter: RecordOfGame (the record of both players' choices and outcomes)
    # Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    # Description:
    #  (1)This function asks the user to make a choice (i.e. input a string)
    #     This function will NOT return/exit until it gets a valid input from the user
    #     valid inputs are: rock or r, paper or p, scissors or s
    #  (2)This function will also ask if the user wants to print RecordOfGame or quit
    # --------------------------------------------------------


# %%
def ComputerPlayer():
    import random
    compute = random.randint(1,3)
    if compute == 1:
        return 'rock'
    elif compute == 2:
        return 'paper'
    elif compute == 3:
        return 'scissors'
    else:
        print('Error in method "ComputerPlayer": Computer has made an invalid choice')
        
#ComputerPlayer(0)
    
    # Parameter: RecordOfGame (the record of both players' choices and outcomes)
    # Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    # Description:
    #     ComputerPlayer will randomly make a choice
    #     ComputerPlayer should not looking at the current choice of HumanPlayer
    # --------------------------------------------------------


# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
        computer_choice = ChoiceOfComputerPlayer
        human_choice = ChoiceOfHumanPlayer
        if human_choice==computer_choice:
            return 0
        elif human_choice== 'rock' and computer_choice == 'paper':
            return 1
        elif human_choice== 'rock' and computer_choice == 'scissors':
            return 2
        elif human_choice== 'paper' and computer_choice == 'scissors':
            return 1
        elif human_choice== 'paper' and computer_choice == 'rock':
            return 2
        elif human_choice== 'scissors' and computer_choice == 'paper':
            return 2
        elif human_choice== 'scissors' and computer_choice == 'rock':
            return 1
        else:
            print('Error in method "Judge": Unknown comparrison between computer and player')
    
    # Parameters:
    #     ChoiceOfComputerPlayer is a string from ComputerPlayer
    #     ChoiceOfHumanPlayer is a string from HumanPlayer
    # Return: Outcome
    #     Outcome is 0 if it is a tie
    #     Outcome is 1 if ComputerPlayer wins
    #     Outcome is 2 if HumanPlayer wins
    # Description:
    #     this function determines the outcome of a game
    # --------------------------------------------------


# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    computer_choice = ChoiceOfComputerPlayer
    human_choice = ChoiceOfHumanPlayer
    print('You chose ',human_choice)
    print('The computer chose ',computer_choice)
    if Outcome == 0:
        print('Its a tie!\n')
    elif Outcome == 1:
        print('The computer won!\n')
    elif Outcome == 2:
        print('You won!\n')
    else:
        print('Error in method "PrintOutcome": Unknown outcome')
        
    
    # Parameters:
    #     Outcome is from Judge
    #     ChoiceOfComputerPlayer is a string from ComputerPlayer
    #     ChoiceOfHumanPlayer is a string from HumanPlayer
    # Return: None
    # Description:
    #     print Outcome, Choices and Players to the console
    #     the message should be human readable
    # --------------------------------------------------------


# %%
def UpdateRecordOfGame(RecordOfGame, gameNum, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    computer_choice = ChoiceOfComputerPlayer
    human_choice = ChoiceOfHumanPlayer
    if Outcome == 0:
        who_won = 'tie'
    elif Outcome == 1:
        who_won = 'computer'
    elif Outcome == 2:
        who_won = 'you'
    else:
        print('Error in method "UpdateRecordOfGame": Unknown victor')   
    record = RecordOfGame
    record[gameNum] = computer_choice, human_choice, who_won
    return record
    
    # Parameters: 
    #    RecordOfGame is the record of both players' choices and and outcomes
    #    ChoiceOfComputerPlayer is a string from ComputerPlayer
    #    ChoiceOfHumanPlayer is a string from HumanPlayer
    #    Outcome is an integer from Judge
    # Return: None
    # Description:
    #     this function updates RecordOfGame, a Python dictionary


# %%
def PrintRecordOfGame(RecordOfGame):
    print('---------GAME RECORD-----------')
    print("Game Number, Computer's Choice, Your Choice, Winner")
    print(RecordOfGame)
    print('-------------------------------\n')
    # Parameters: RecordOfGame (the record of both players' choices and outcomes)
    # Return: None
    # Description: this function prints the record of the game (see the sample run)
    #    the number of rounds. human wins x rounds. computer wins y rounds.
    #    the record of choices.

# %% the game
def PlayGame():
    gameNum = 0
    saved_record = dict()
    playing = True
    print ('\nWelcome to Rock, Paper, Scissors!')
    while playing:
        human_choice = HumanPlayer()
        if human_choice == 'quit':
            print('Done')
            playing = False
            break
        elif human_choice == 'record':
            if gameNum == 0:
                print('No record to print\n')
            else:
                PrintRecordOfGame(saved_record)
        else:
            computer_choice = ComputerPlayer()
            outcome = Judge(computer_choice, human_choice)
            PrintOutcome(outcome, computer_choice, human_choice)
            gameNum = gameNum + 1
            saved_record = UpdateRecordOfGame(saved_record, gameNum, computer_choice, human_choice, outcome )
        
    # This is the "main" function
    # In this function, the game will be played many rounds until the user wants to quit


# %% do not modify anything below
if __name__ == '__main__':
    PlayGame()
