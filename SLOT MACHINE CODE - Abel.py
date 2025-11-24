'''
Here, I have created a simple slot machine game
user will be prompted to click enter to start the game, in which the user will input a number for hwo much they want to bet in the session
they can play the slot machine a number of times until they run out of money.

'''
import random
import math

def rand_spin():
    symbols = ["🧪", "🔬", "💡", "⚗️", "🧬", "🔋"] # i chose the symbols to be chemical engineering related!
    spinrow = symbols[random.randint(0,len(symbols)-1)],symbols[random.randint(0,len(symbols)-1)],symbols[random.randint(0,len(symbols)-1)]
    return spinrow
    


#print("Spin Results: ", *spin_result) #STILL TRYING TO FIGURE THIS OUT

def show_spin(spin_result): #we can use the random result that we got in the previous function as a parameter, and print this in like a cool sandwich
    line = print("--------------------\n" , spin_result, "\n--------------------")
    return line


#_____________________________________________________________________________________________________________



def winnings(bet, spin_result):
    if spin_result[0] == spin_result[1] == spin_result[2]:
        if spin_result[0] == spin_result[1] == spin_result[2] == '🧪':
            return 100
        if spin_result[0] == spin_result[1] == spin_result[2] == '🔬':
            return 300
        if spin_result[0] == spin_result[1] == spin_result[2] == '💡':
            return 500
        if spin_result[0] == spin_result[1] == spin_result[2] == '⚗️':
            return 700
        if spin_result[0] == spin_result[1] == spin_result[2] == '🧬':
            return 1000
        if spin_result[0] == spin_result[1] == spin_result[2] == '🔋':
            print("JACKPOTTTT!!!!! WOOHOOOOOOOOOOOOOOOOOOOOOOO")
            return 12500000000000000000000000000
            
        
    return 0

def main():
    money = 100
    print("Welcome to Chem Eng Slots, spin to react and WIN TO BOND!")
    user_input = input("CLick enter to play or c to close the application")

    if user_input =="c":
        quit()
    elif not user_input =="":
        user_input = input("CLick enter to play or c to close the application")

    
    while money >= 0:
        earnings=0
        print("You have" , money , "dollars remaining to spend!")
        
        while True:
            print("How much would you like to bet for the next spin? ")
            bet_amount = input()

            if not bet_amount.isdigit():
                print("THATS NOT A DIGIT, PLEASE TRY AGAIN: ")
                bet_amount = input()

            bet = int(bet_amount)

            if money == 0:
                print("You don't have enough money to keep playing! Have a good night!")
                money = input("Please Input More Money to continue playing or click c to close: ")
                
                if money == 'c':
                    print("Have a good night!")
                    quit()
                else:
                    int(money)
                    main()

                
            if int(bet) <= 0:
                print("You can't bet negative money! Please enter valid bet: ")

                continue

            if int(bet) > money:
                print("Unfortunately, you have insufficient funds. Bet a value within your budget: ")
                continue
                
            
            money -= int(bet)
            print("Funds loaded, BALANCE: ", money)   
            print(' SPINNING.... GOOD LUCK!! ')
            spin_result = rand_spin() #set a variable equal to the result of the function(which will give us the 3 random symbols)

            print(show_spin(spin_result))
            earnings = winnings(bet, spin_result)
            money += earnings
            print('You have won: ', earnings, 'dollars!')

 
main()