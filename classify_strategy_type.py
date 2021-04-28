import main as m;

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
second_three_v2 = [0,0,34,33,33,0,0,0,0,0]
kole2 = [0,20,40,40,0,0,0,0,0,0]
kole2_modified = [0,22,40,38,0,0,0,0,0,0]
test3 = [5,15,5,15,5,15,5,15,5,15]
test4 = [20,40,40,0,0,0,0,0,0,0]
test4_modified = [20,38,42,0,0,0,0,0,0,0]
test4_modified_v2 = [21,37,42,0,0,0,0,0,0,0]
bola_v2 = [1,1,50,1,1,1,10,15,10,10]
test5 = [25,25,50,0,0,0,0,0,0,0]
test5_modified = [24,25,51,0,0,0,0,0,0,0]
test6 = [22,22,56,0,0,0,0,0,0,0]
test7 = [22,22,53,1,1,1,0,0,0,0]
test7_modified = [22,22,52,1,1,1,1,0,0,0,0]

test_strats = [example_alice, test, test2,bola,kole,uju,babs,even_distribution,first_three,second_three, second_three_v2,kole2,kole2_modified,test3,example_carol,test4,test4_modified,test4_modified_v2,bola_v2,test5,test5_modified, test6, test7, test7_modified]

test_strats_name = ["example_alice", "test", "test2","bola","kole","uju","babs","even_distribution","first_three","second_three", "second_three_v2","kole2","kole2_modified","test3","example_carol","test4","test4_modified","test4_modified_v2","bola_v2","test5","test5_modified", "test6", "test7", "test7_modified"]


def classify(castles, trials = 10000, threshold = .95, name = "None"):
    prob_distr, points_won, opponent_points, wins_by_three, opponents_win_by_three = m.simulate(trials, c1=castles, print_result=False, print_castles=False)
    print("Strategy Type" + "[" +  name + "]" + ": " + str(wins_by_three))
    if wins_by_three >= threshold:
        print("Aggresive")
    else:
        print("Conservative")

if __name__ == "__main__":
    #classify([0,0,25,25,25,5,0,0,10,10], name = "TESTS")
    #classify([0,0,15,0,0,15,0,20,20,30], name = "TESTS")
    for x in range(len(test_strats)):
        classify(test_strats[x], name=test_strats_name[x])