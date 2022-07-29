import random
# simulate the Monty Hall problem

# revealing a door
# switching to another door


def get_another_door(door_1, door_2, n_doors):
    # door you reveal is not equal to the winning door
    door_choice = random.randrange(1, n_doors+1)
    while door_choice == door_1 or door_choice == door_2:
        door_choice = random.randrange(1, n_doors+1)

    return door_choice
# gets a door randomly between 1 and n, that is not door 1 or door 2


def run_trial(n_doors, user_switch):  # return True if we win, False if we lose
    # hide the prize behind a door
    winning_door = random.randrange(1, n_doors+1)  # 1, 2, 3
    user_door_choice = random.randrange(1, n_doors+1)  # 1, 2, 3

    # reveal a door, but the door cannot be winning_door
    revealed_door = get_another_door(winning_door, user_door_choice, n_doors)

    if user_switch:
        user_door_choice = get_another_door(revealed_door, user_door_choice, n_doors)

    # have we won?
    if user_door_choice == winning_door:
        return True
    else:
        return False


def run_simulation(n_doors, num_runs=100000):
    print("######################################################")
    print(f"Simulation with {n_doors} doors")
    # counting how many wins if we switch/not switch
    counter_switch = 0
    counter_not_switch = 0

    for switch in [True, False]:
        for i in range(num_runs):
            win_trial = run_trial(n_doors, switch)  # choose door 1, switch after reveal

            if win_trial:
                if switch:
                    counter_switch += 1
                else:
                    counter_not_switch += 1

    print(f"If we switch, we win {counter_switch/num_runs*100}% of the time.")
    print(f"If we do not switch, we win {counter_not_switch/num_runs*100}% of the time.")
    print("######################################################")


run_simulation(4)
run_simulation(10)
run_simulation(100)
