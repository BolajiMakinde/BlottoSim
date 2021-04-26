'''
At Jane Street, our day-to-day work involves figuring out what's happening in financial markets and building algorithms and 
systems to do better trades. This often presents us with challenging and interesting problems. However, many of us also enjoy
solving puzzles and playing games for their own sake. One game (technically, class of games) we like to play is called Blotto. Here is 
one instance: 
There are 10 castles, numbered 1, 2, 3, ... , 10, and worth 1, 2, 3, ... , 10 points respectively. You have 100 soldiers, which you can 
allocate between the castles however you wish. Your opponent also (independently) does the same. The number of soldiers on 
each castle is then compared, and for each castle, whoever has the most soldiers on that castle wins its points (in the case of a tie, 
no one gets points). In a given match, castles are fought in order (starting with castle 1). If at any point a player wins 3 consecutive 
castles, that player is automatically awarded all remaining castles.
For example, here is one potential match:
C1 C2 C3 C4 C5 C6 C7 C8 C9 C10
Alice 10 10 10 10 20 0 0 0 20 20
Carol 20 0 10 5 10 5 10 20 0 0
In the example match above, Alice wins castles 2, 4, and 5, for a total of 11 points. Carol wins castles 1, 6, 7, and 8 — and then 
castles 9 and 10 — for a total of 41 points. (No one wins castles 3, since that was a tie. Alice does not win castles 9 or 10 because 
those were awarded to Carol after she won castles 6 through 8.).
We're going to play a tournament. You get one entry and your final score is the average of your scores playing head-to-head
against entries from over 300 Jane Streeters. An entry should be submitted as a list of 10 non-negative integers, adding up to 100, 
where the Nth element is the number of soldiers being sent to castle N.
What's your entry? How did you go about coming up with it?
'''
import random
import pandas as pd
import numpy as np
#= 10000 trial uniform random distribution win rate
#*= 10000 trial random probability distribution win rate
example_alice = [10,10,10,10,20,0,0,0,20,20] #= 0.23 #*= 0.23
example_carol = [20,0,10,5,10,5,10,20,0,0] #= 0.01 #*= ?
test = [20,0,20,0,20,0,20,0,20,0] #= 0.00 #*= 0.00
test2 = [0,20,0,20,0,20,0,20,0,20] #= 0.99 #*= 0.89
bola = [1,1,35,1,1,20,1,11,14,15] #= 0.87 #*= 0.68
kole = [0,0,35,33,32,0,0,0,0,0] #= 1.00 #*= 1.00
uju = [2,2,38,2,2,19,2,19,12,2] #= 0.00 #*= 0.02
babs = [1,1,21,1,1,21,1,11,31,11] #= 0.65 #*= 0.57
even_distribution = [10]*10 #= 0.55 #*= 0.50
first_three = [33,33,34,0,0,0,0,0,0,0] #= 1.00 #*= 1.00
second_three = [0,0,33,33,34,0,0,0,0,0] #= 1.00 #*= 1.00
kole2 = [0,20,40,40,0,0,0,0,0,0]

tourney = [example_alice, test, test2,bola,kole,uju,babs,even_distribution,first_three,second_three,kole2]

def simulate_tournament(trials, use_prob_distribution = True, contestants = None):
    number_of_contestants = len(contestants)
    tournament_results = []
    for x in range(number_of_contestants):
        a = []
        for y in range(number_of_contestants):
            a.append(0)
        tournament_results.append(a)

    #print(tournament_results)
    if number_of_contestants < 2:
        return None
    contestant_scores = [0] * number_of_contestants
    contestant1 = 0
    while contestant1 < number_of_contestants-1:
        contestant2 = contestant1+1
        while contestant2 < number_of_contestants:
            tournament_results[contestant1][contestant2] = float(round(simulate(trials, c1 = contestants[contestant1], c2 = contestants[contestant2], print_result = False, print_castles = False),5))
            tournament_results[contestant2][contestant1] = -1*tournament_results[contestant1][contestant2]
            #print("c1: " + str(contestant1) + "c2 " + str(contestant2))
            contestant2+=1
        contestant1 += 1
    print(tournament_results)
    return tournament_results

def simulate(trials, c1 = None, use_prob_c1 = True, c2 = None, use_prob_c2 = True, print_result = True, print_castles = True):
    Alice = []
    Carol = []
    if print_castles & print_result == True:
        print("----------------------------------------------")
    trial = 1
    Alice_wins = 0
    Carol_wins = 0
    Draws = 0
    while trial <= trials:
        if c1 == None:
            Alice = select_random_castles()
            Alice = generate_probability(kole)
            #Alice = generate_probability(bola)
        else:
            Alice = c1
            if use_prob_c1:
                Alice = generate_probability(c1)
        if print_castles == True:
            print("ALICE CASTLES: ")
            print(Alice)
        if c2 == None:
            Carol = select_random_castles()
            Carol = bola
            #Carol = generate_probability(select_random_castles())
        else:
            Carol = c2
            if use_prob_c2:
                Carol = generate_probability(c2)
        if print_castles == True:
            print("CAROL CASTLES: ")
            print(Carol)
        result, points, winning_castles = determine_winner(Alice, Carol)
        
        if result == "Draw":
            if print_result == True:
                print(result + "!")
            Draws+=1
        else:
            if print_result == True:
                print(result + " Wins by " + str(points) + " Points!")
            if result == "Alice":
                Alice_wins += 1
            else:
                Carol_wins += 1
        if print_castles == True:
            print(winning_castles)
        trial += 1
        if print_result == True:
            print("____________________________________________________")
    if print_result == True:
        print("====================================================")
        print("Alice Wins: " + str(Alice_wins/trials) + "Carol Wins: " + str(Carol_wins/trials) + "Draws: " + str(Draws/trials))
        print("====================================================")
    return (Alice_wins/trials) - (Carol_wins/trials)

def select_random_castles():
    castles = [0]*10
    iteration = 1
    while iteration <= 100:
        castles[random.randint(0,9)] += 1
        iteration += 1
    return castles

def generate_probability(castles):
    temp_arr = [0]*100
    iteration = 1
    ret = [0]*10
    while iteration <= 100:
        temp_arr[random.randint(0,99)] += 1
        iteration += 1
    #---------------------------------------
    iteration = 1
    col = 0
    sum_cols = castles[col]
    while iteration <= 100:
        while iteration > sum_cols:
            col += 1
            if sum_cols == 100:
                break
            sum_cols += castles[col]
        ret[col] += temp_arr[iteration-1]
        iteration += 1
    return ret

def determine_winner(Alice, Carol):
    col = 0
    Alice_points = 0
    Carol_points = 0
    winning_castles = ['U']*10
    while (col < 10):
        if Alice[col] > Carol[col]:
            winning_castles[col] = 'A'
            Alice_points += col+1
        elif Alice[col] < Carol[col]:
            winning_castles[col] = 'C'
            Carol_points += col+1
        else:
            winning_castles[col] = 'X'
        if col >= 2 and winning_castles[col] != 'X' and winning_castles[col] == winning_castles[col-1] and winning_castles[col] == winning_castles[col-2]:
            while (col < 10):
                winning_castles[col] = winning_castles[col-1]
                if winning_castles[col] == 'C':
                    Carol_points += col+1
                else:
                    Alice_points += col+1
                col += 1
            break
        col += 1
    if Alice_points > Carol_points:
        return "Alice", Alice_points, winning_castles
    elif Alice_points < Carol_points:
        return "Carol", Carol_points, winning_castles
    else:
        return "Draw", Alice_points, winning_castles

a = np.array(simulate_tournament(10000,contestants=tourney))
#np.savetxt('my_file.csv',a,delimiter=',')
pd.DataFrame(a).to_csv("my_file.csv")
df = pd.DataFrame(a).T
#df.to_excel(excel_writer = 'my_file.xlsx')