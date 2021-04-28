import main as m;
import pandas as pd
import numpy as np
import classify_strategy_type as cst;


arr_prob = []
arr_castle_avg_score = []
arr_opponent = []
arr_opponent_avg_score = []
arr_castle_wins_by_three = []
arr_opponent_wins_by_three = []
arr_opponent_aggressiveness = []
my_file = []

def performance_vs_aggressiveness(trials, castle):
    for x in range(trials):
        opponent = m.select_random_castles()
        opponent_aggressiveness = cst.classify(opponent,250,.95,"Opponent " + str(x))
        prob, castle_avg_score, opponent_avg_score, castle_wins_by_three, opponent_wins_by_three = m.simulate(200, castle,c2=opponent,print_result=False,print_castles=False)
        arr_prob.append(prob)
        arr_castle_avg_score.append(castle_avg_score)
        arr_opponent_avg_score.append(opponent_avg_score)
        arr_castle_wins_by_three.append(castle_wins_by_three)
        arr_opponent_wins_by_three.append(opponent_wins_by_three)
        arr_opponent_aggressiveness.append(opponent_aggressiveness)
    my_file.append(arr_prob)
    my_file.append(arr_castle_avg_score)
    #my_file.append(arr_opponent)
    my_file.append(arr_opponent_avg_score)
    my_file.append(arr_castle_wins_by_three)
    my_file.append(arr_opponent_wins_by_three)
    my_file.append(arr_opponent_aggressiveness)
    return my_file

if __name__ == "__main__":
    a = np.array(performance_vs_aggressiveness(10000,castle = [10,10,10,10,20,0,0,0,20,20]))
    pd.DataFrame(a).to_csv("performance_aggressiveness_alice.csv")