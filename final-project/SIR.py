import matplotlib.pyplot as plt

initial_pop = 10000 #10 thousand
beta = 0.2 #4 people infected/day
gamma = 1/100 #4 days to recover or 1/4 people recovering/day

def run_simulation():
    S = initial_pop - 1
    I = 1 #patient 0
    R = 0

    S_list = []
    I_list = []
    R_list = []
    while True:
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
        S, I, R = calculate_next(S, I, R)
        delta_S = abs(S - S_list[-1]) #new value and last one stored
        print('S =', S)
        print('I = ', I)
        print('R = ', R)
        if S < 0 or delta_S < 0.0001:
            plt.plot(S_list)
            plt.plot(I_list)
            plt.plot(R_list)
            plt.show()
            exit()

def calculate_next(s, i, r):
    s_next = s - beta * i * s/initial_pop
    i_next = i + beta * i * s/initial_pop - gamma * i
    r_next = r + gamma * i
    S = s
    I = i
    R = r
    return (s_next, i_next, r_next)

run_simulation()