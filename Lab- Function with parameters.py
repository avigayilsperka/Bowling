
def main():
    x = int(input('Enter the number of bowlers on the team:'))                      #number of bowlers
    x = validatex(x)                                                                #pass to function to validate
    y = int(input('Enter the number of games played by the team:'))                 #number of games
    y = validatey(y)                                                                #pass to function to validate
    list=avg(x,y)                                                                   #call avg(),pass bowlers and games
    list.sort()                                                                     #recieve and sort list of averages. Display greatest.
    print('The highest player average is',list[-1])
            
def avg(bowler, game):
    list=[]                                                                         #Empty list for averages
    teamaverage = 0
    print('Enter the scores for each player:\n')
    for x in range(1,bowler+1):                                                     #loop for each player. Loops per game.
        average = 0
        playerscr = 0
        print('Player', x)
        for x in range(1,game+1):
           print('Game',x,':', end='')                                              #Receive scores per game per player
           score = int(input())
           score = validatescore(score)                                             #validate score. keep running total
           playerscr += score
        average = playerscr / game
        list.append(average)                                                        #Determine average per player and add to list                                                    
        teamaverage += average
        print('\toverall score:',playerscr)                                         #Print score and average per player
        print('\taverage:',average)
        print('\n')
    print('The team average is:',teamaverage/bowler)                                #calculate and print team average
    return list                                                                     #Return list of averages to main

def validatex(x):
    while x<2:
        x = int(input('Program only runs for 2 or more players.\nPlease re-enter the number of players:'))
    return x

def validatey(y):
    while y<3:
        y = int(input('Program only runs for 3 or more games.\nPlease re-enter the number of games:'))
    return y

def validatescore(score):
    while score > 300 or score<0:
        if score>300:
            score = int(input('Please re-enter a score below 300:'))
        else:
            score = int(input('Please re-enter a positive score:'))
    return score
        
main()
