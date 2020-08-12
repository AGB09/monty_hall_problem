import random as r
import matplotlib.pyplot as plt
import copy as c

doors = ['a', 'b','c']
plays = 1000


def monty_hall_many(doors, plays):

    car_behind_door = [doors[r.randrange(0,len(doors))] for i in range(1,plays+1)]

    first_choice = [doors[r.randrange(0,len(doors))] for i in range(1,plays +1)]



    open_door = []
    switch_to = []

    for first, car in zip(first_choice, car_behind_door):
        if first == car:
            choice = c.deepcopy(doors)
            choice.remove(first)
            choose = choice[r.randrange(0,len(choice))]
            open_door.append(choose)
            choice.remove(choose)
            switch_to.append(choice)
            
        elif first != car:
            choice = c.deepcopy(doors)
            choice.remove(first)
            choice.remove(car)
            open_door.append(choice[r.randrange(0,len(choice))])
            switch_to.append(car)
    
    
    def switch_y_n(switch):
        win_or_no = []
        if switch == 'no':
            for i, j in zip(first_choice, car_behind_door):
                win_or_no.append(i==j)
            
        elif switch == 'yes':
            for i, j in zip(switch_to, car_behind_door):
                win_or_no.append(i==j)

        pct_win = 100*sum(win_or_no)/plays
        print("Winning percentage = {}%".format(pct_win))


        ## plotting

        x = list(range(1,plays+1))

        # running winning pct
        y=[]
        for i, j in enumerate(win_or_no):
                y.append(sum(win_or_no[:i])/(i+1))

        plt.scatter(x,y, label = "Switched door? {}".format(switch))
        plt.legend()
        

    switch_y_n('yes')
    switch_y_n('no')
    plt.title("Simulating results of Monty Hall problem with {} doors and {} runs".format(len(doors), plays))
    plt.xlabel("Runs")
    plt.ylabel("Success %")
    plt.show()

monty_hall_many(doors, 5000)
