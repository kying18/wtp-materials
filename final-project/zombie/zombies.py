import random
import numpy as np
resistance_range = (0, 0.5)  # tuple of low and high bounds for resistance
cure_time = (10, 4) #the first value is the mean, then second is the 'mu' or standard deviation: ask a TA if you have any questions!


class Person(object):
    def __init__(self, state):
        '''
        Initial constructor of a person. Holds their susceptibility (float, range 0:1), and state.
        'S' = susceptible (human)
        'I' = infected (aka zombie)
        'R' = recovered + immune (cured and incapable of becoming a zombie again, represented by a robot)
        '''
        self.resistance = random.uniform(*resistance_range)  # unpacking notation
        # equivalent to = random.uniform(sus_range[0], sus_range[1])
        self.state = state
        # this might seem silly but it's important so we bind that original state to each Student object
        self.recovery_time = np.random.normal(*cure_time)
        #uses a normal distribution based on the cure_time tuple above with the first value as the mean, second as the standard deviation
        self.num_rounds = 0

    def interact(self):
        '''
        returns a boolean based on whether or not an interaction with an infected student results in an infection
        "R" = resistant and no infection will occur
        '''
        if self.get_state() == 'R':
            return False
        strength = random.random()  # random value of infection strength
        if self.resistance < strength:  # if student strength is less than virus strength, infected
            return True
        return False

    def get_state(self):
        '''
        Returns the state, either 'I', 'S', or 'R'
        :return:
        '''
        return self.state

    def set_state(self, state):
        '''
        Sets the state given 'S', 'I', or 'R'
        '''
        self.state = state


class School(object):
    def __init__(self, num_students, initial_spread, beta=2):  # discuss including variable name in header?
        '''
        Constructs a school given a number of students and the initial probability of infection.
        '''
        self.beta = beta
        self.list_students = []
        for _ in range(num_students):
            # weighted choices, unpacking list
            rand_disease = random.choices(['S', 'I'], weights=[1-initial_spread, initial_spread])[0]
            self.list_students.append(Person(rand_disease))
        self.school_size = num_students

    def infect_round(self):
        '''
        Simulates a day of student interactions, controlled by the sociality variable 'BETA"
        '''
        # generate a list of infected students
        infected_students = []
        for student in self.list_students:
            if student.get_state() == 'I':
                infected_students.append(student)
        # for each infected student, have them interact with some random subset of students
        for _ in infected_students:
            #the underscore (_) is a python convention: when we don't use the VALUE of a term (like student in infected students)
            #we don't put a real term there, and it's just like a counter (equivalent to say for i in range(len(infected_students)
            for i in range(round(self.beta)):  # in this code, beta can be a float
                print('infecting student', i, 'for beta', self.beta)
                contact = random.randint(0, self.school_size-1)
                infected = self.list_students[contact].interact()
                if infected:
                    self.list_students[contact].set_state('I')
        for student in self.list_students:
            student.num_rounds += 1
            if student.num_rounds >= student.recovery_time:
                student.set_state('R')

    def get_num_infected(self):
        '''
        Returns number of zombie students as an integer
        '''
        count = 0
        for student in self.list_students:
            if student.get_state() == 'I':
                count += 1
        return count

    def can_continue(self):
        if self.school_size == self.get_num_infected():
            return False
            #if everyone is infected, game over
        robo_count = 0
        for student in self.list_students:
            if student.get_state() == 'R':
                robo_count += 1
        if robo_count == self.school_size:
            return False
            #if everyone is cured, game won
        else:
            return True
            #otherwise keep playing

    ###
    # METHODS TO LOWER INFECTION RATES
    ###
    def cure_student(self):
        '''
        Turns a single student into a fully resistant robot
        '''
        random_list = self.list_students.copy()
        random.shuffle(random_list)
        if self.get_num_infected() == 0:
            print('no student to cure')
        else:
            for student in random_list:
                if student.get_state() == 'I':
                    student.set_state('R')
                    return None

    def lower_beta(self):
        '''
        Lowers the number of students each infected individual interacts with to 80% of current levels
        :return:
        '''
        self.beta = self.beta*0.8

    def strengthen_students(self):
        '''
        Reduces the susceptibility of all students by 10%
        '''
        for student in self.list_students:
            student.sus = 0.9*student.sus

    def shorten_cure_time(self):
        '''
        Shortens the time to cure of all students by 10%
        '''
        for student in self.list_students:
            student.recovery_time = 0.9*student.recovery_time

    def __str__(self):
        '''
        overwrites main to_string method for helpful command-line debugging
        '''
        string = ''
        total_length = len(self.list_students)
        repr_dict = {'S': 'o', 'I': 'z', 'R': 'R'}  # shows o for students and z for zombies
        for ix in range(total_length):
            string += repr_dict[self.list_students[ix].get_state()] + ' '  # adds each student
            if (ix+1) % 15 == 0:  # line breaks every 15 students
                string += '\n'
        return string


if __name__ == "__main__":
    '''
    Runs a school simulation of size 75 with an initial infection chance of 1/20
    '''
    school = School(75, 0.05)
    start = input(
        'Welcome, school administrator. Your school has been infected with a zombie virus. Type \'YES\' to start the simulation.')
    if start in ['YES', 'yes', 'Y', 'y']:
        print(school)
        num_rounds = 0
        while True:
            next = input('Press enter to start the next round')
            if next == 'y':
                school.cure_student()
            if next == '':
                school.infect_round()
                print('after infection')
                print(school)
                num_rounds += 1
                print('num_rounds', num_rounds)
                if school.get_num_infected() == school.school_size:
                    print('All your students are now zombies. Your school survived', num_rounds-1, 'rounds')
                    exit()
