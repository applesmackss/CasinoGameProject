import math
from random import*
from tkinter import*



#setup
root = Tk()

#makes the background
Board = PhotoImage(file='RouletteBoard.png')
canvas = Canvas(root, width=600, height=300)
canvas.pack()


money = 1000
#main run function
def run_roulette():
    #global variables and initializing booleans
    global money, bet_amount,play_again

    bet = True

    print('welcome to Roulette ')


    while bet:
        #geting the bet amount
        bet_amount = input(f'you have {money} how much would u like to bet: ')

        #checks if it can be converted to a float
        #by trying to convert bet_amount
        try:
            float(bet_amount)
            is_float = True

        #if there is an error bet_amount is not a float
        except ValueError:
            is_float = False

        #checks if bet_amount is a float or more than you can afford
        #then would ask you again based on our while loop
        if  is_float == False or float(bet_amount)>float(money) :
            print('you cant bet this amount because its more then you have ')

        #if bet_amount is a float, and you have enough money then
        #we make bet false and to close the loop and take away your money you spent on the bet
        if is_float == True and float(bet_amount) <= money  :
            bet = False
            money -= float(bet_amount)



#running the function
run_roulette()

#bulit in function from tinker to check if the user clicks on the image/screen
def check_click(event):
    #global variables
    global money, bet_amount

    #next steps are to find the closet distance

    #we set the current_dis to a very high number
    #this is because we are finding the smallest distance
    current_dis = 10**10

    #this will make number None if they are off the bored
    if not(bounds_checker(event.x, event.y)):
        print('click again on the bored please')

    #this will run only if they are the bored
    if bounds_checker(event.x, event.y):

        #we make circles to compute the distance instead of doing
        #several hit boxes more details later

        #a for loop that goes through a list of circles x and y coordinates
        for n in circles:

            #checks the distance between mouse and current circle being checked
            distance = math.dist(n, [event.x,event.y])

            #checks if the distance in this instance is less then the
            #current smallest distance
            if current_dis > distance :

                #this will update the smallest distance to this distance
                #this will also update the number which is the index of the circle in the circle list
                current_dis = distance
                number = circles.index(n)


        #function that will go through the index values and make type guess and string
        # values either an exact value or a list and mult the money multiple based on the odds
        type_guess, values, mult = check_guess(number)

        #a random number between -1 and 36 -1 because of the 00
        outcome = randint(-1,36)

        #turns bet amount into a float and another original bet to find net gain
        bet_amount = float(bet_amount)
        org_bet_amount = bet_amount


        #checks if the type of guess is in the following list as these are a list of vaules
        if type_guess in ['black', 'red', 'odd', 'even', '1 to 18', '19 to 36', 'column', 'row']:
            #checks if the outcome (random value) is in the list of chosen values
            if int(outcome) in values:

                #if it is we will update the bet amount with the mult
                bet_amount *= mult
                #then add the updated bet amount to the money
                money += float(bet_amount)

        #if the guess is an exact value
        if type_guess == 'number':
            #we check if the outcome is exactly equal to the value chosen
            if int(outcome) == values:
                #if so same process as above of multiplying
                #the bet amount then adding to the total money
                bet_amount *= mult
                money += float(bet_amount)

        #zero case
        if type_guess == 'zero':
            #if the outcome is zero and values is 1 meaning the user chose 0 not 00
            if int(outcome) == 0 and values  == 1:
                #used same method of adding as above
                bet_amount *= mult
                money += float(bet_amount)

            #if outcome is -1 and user chose 00 not 0 the values will equal 0
            if int(outcome) == -1 and values == 0:
                #used same method of adding as above
                bet_amount *= mult
                money += float(bet_amount)

        #prints on if they clicked on the bored lists things like:
        #the outcome what they picked (type) and there bet and how much they made
        print(f'''you selected numbers {values} and the outcome that was spun is {outcome} 
your bet was {org_bet_amount} which got you a return of {bet_amount - org_bet_amount}''')

        #asks if they would like to play again requires them to hit enter if they would
        play_again = input('would you like to play again type hit enter if you would')

        #if they hit enter we run again carrying over the money
        if play_again == '':
            run_roulette()
        #if not we exit the code
        else:
            exit()

#hitboxs for numbers on bored
#process is the same across next three chunks

#intail x and y position
x = 87
y = 162

#the difference in the x and y each time
diffx = 38.75
diffy = 48

#empty circles list
circles = []

#repeat this 13 times amount of columns
for i in range(13):

    #we rest the y position after every run
    y = 162

    #repeat three times for each row
    for j in range(3):
        #makes a circle at the x and y position the size and colour are irrelevant
        circle = canvas.create_oval(x-2, y-2, x+2,  y+2, fill='blue', outline="blue")
        #take away the y diff each time since we started at the top
        y-=diffy
        #add the circles x and y position to the list of circles information
        circles.append([canvas.coords(circle)[0]+2,canvas.coords(circle)[1]+2])
    #add x difference meaning we started at the top left of the gird
    x+=diffx

#hit box for lower options
x = 87
y = 229
diffx = 38.75
diffy = 29
for i in range(12):
    y = 229
    for j in range(2):
        circle = canvas.create_oval(x-2, y-2, x+2,  y+2, fill='red', outline="red")
        y-=diffy
        circles.append([canvas.coords(circle)[0]+2,canvas.coords(circle)[1]+2])
    x+=diffx

#0 and 00 values
x = 53
y = 167.5625
diffy = 35.875
for j in range(4):
    circle = canvas.create_oval(x-2, y-2, x+2,  y+2, fill='red', outline="red")
    y-=diffy
    circles.append([canvas.coords(circle)[0]+2,canvas.coords(circle)[1]+2])

#makes the acc bored you see which is just a png image done using tkinter
canvas.create_image(0, 0, anchor=NW, image=Board)

#check the guess which returns three different things:
#type of guess, value and the money multiplayer and takes in a int
#which is the index in the circles list
def check_guess(x):

    #if its between 0 and 35 it's a number and we can just add one to its value
    #as its saved in the list in order of number and lists start at 0
    if x >= 0 and x<=35:
        return "number", x + 1, 2

    #index 36 is the top row
    if x == 36:
        return "row", [1,4,7,10,13,16,19,22,25,28,31,34],3

    #index 37 is the middle row
    if x == 37:
        return "row", [2,5,8,11,14,17,20,23,26,29,32,35], 3

    #this is the bottom row
    if x == 38:
        return  "row", [3,6,9,12,15,18,21,24,27,30,33,36],3

    #this is 00
    if x == 63 or x == 64:
        return'zero', 0, 36

    #this one is 0
    if x ==65 or x == 66:
        return  'zero', 1, 36

    #this is the numbers 1 to 12
    if x in [40,42,44,46]:
        return 'column', [1,2,3,4,5,6,7,8,9,10,11,12], 3

    #this is numbers 13 to 24
    if x in [48,50,52,54]:
        return 'column', [13,14,15,16,17,18,19,20,22,23,24],3

    #this is numbers 25 to 36
    if x in [56,58,60,62]:
        return 'column', [25,26,27,28,29,30,31,32,33,34,36], 3

    #this is the first half of numbers
    if x == 39 or x == 41:
        return  '1 to 18', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 2

    #this is the last half of numbers
    if x == 59 or x == 61:
        return  '19 to 36', [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], 2

    #this is even list of numbers
    if x == 43 or x == 45:
        return  'even', [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36], 2

    #this is the odd list of numbers
    if x == 55 or x == 57:
         return 'odd', [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35], 2

    #this is the list of red numbers
    if x == 47 or x == 49:
        return  'red', [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36], 2

    #this is the list of black numbers
    if x == 51 or x == 53:
        return 'black', [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35], 2

#this function checks the bounds of the bored
#going over any this return False
def bounds_checker(x1, y1):
    #this the case of the corner is the bottom left
    #in which its on the overall rectangle but due to the
    #over hanging ends its excluded
    if x1< 68 and y1 > 187:
        return False

    #this is the same for right side and needs to be taken account for
    if x1>532 and y1 > 187:
        return False

    #left and right side searches if the x is off the bored on either side
    if x1 < 38 or x1 > 571:
        return False

    #checks top and bottom of the board
    if y1 < 42 or y1 > 243.5:
        return False
    #if none of the cases above are true we return true meaning we clicked on the board
    else:
        return True







#these are standard in tkinter this check when we click to run the check_click function
canvas.bind("<Button-1>", check_click)
#this creates the main GUI for use
root.mainloop()