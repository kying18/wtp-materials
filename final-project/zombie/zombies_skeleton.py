import random
import numpy as np
strength_range = (0, 0.5)  # tuple of low and high bounds for resistance
cure_time = (10, 4) #the first value is the mean, then second is the 'mu' or standard deviation: ask a TA if you have any questions!


class Person(object):
    def __init__(self, state):
        '''
        Initial constructor of a person. Holds their susceptibility (float, range 0:1), and state.
        'S' = susceptible (human)
        'I' = infected (aka zombie)
        'R' = recovered + immune (cured and incapable of becoming a zombie again, represented by a robot)
        '''
        self.strength = random.uniform(*strength_range)  # unpacking notation
        # equivalent to = random.uniform(strength_range[0], strength_range[1])
        self.recovery_time = random.gauss(*cure_time)
        #uses a normal distribution based on the cure_time tuple above with the first value as the mean, second as the standard deviation


        #TO_DO: write a line that creates a variable 'num_rounds' for EACH student, and sets that variable to zero

        #TO_DO: bind the 'state' variable to the student object

    def interact(self):
        '''
        returns a boolean based on whether or not an interaction with an infected student results in an infection
        "R" = resistant and no infection will occur
        '''
        viral_strength = random.random()  # random value of infection strength
        ###
        #TO_DO: write code that returns the correct value if the student is resistant
        ###

        #TO_DO: compare student and virus strength. If the virus is stronger, they are infected
        # if student strength is less than virus strength, infected

        #Note: make sure that your code returns a BOOLEAN (not None), in every possible scenario

    def get_state(self):
        '''
        Returns the state, either 'S', 'I' or 'R'
        :return:
        '''
        #TO_DO

    def set_state(self, state):
        '''
        Sets the state given 'S', 'I', or 'R'
        '''
        #TO_DO


class School(object):
    def __init__(self, num_students, initial_spread, beta=2):  # discuss including variable name in header?
        '''
        Constructs a school given a number of students and the initial probability of infection.
        '''
        ## TO_DO bind beta
        ## TO_DO bind num_students
        ## TO_DO initialize list_students as []
        for _ in range(num_students):
            # weighted choices, unpacking list
            rand_disease = random.choices(['S', 'I'], weights=[1-initial_spread, initial_spread])[0]
            ## TO_DO add a student to list_students with the given rand_disease state
            # Hint: a student is an instance of the Person classs



    def infect_round(self):
        '''
        Simulates a day of student interactions, controlled by the sociality variable 'BETA"
        '''
        # TO_DO
        # generate a list of infected students

        # for each infected student, have them interact with some random subset of students
        for _ in infected_students:
            #the underscore (_) is a python convention: when we don't use the VALUE of a term (like student in infected students)
            #we don't put a real term there, and it's just like a counter (equivalent to say for i in range(len(infected_students)
            for i in range(round(self.beta)):  # in this code, beta can be a float
                contact = random.randint(0, self.school_size-1)
                infected = self.list_students[contact].interact()
                if infected:
                    self.list_students[contact].set_state('I')
        #TO_DO
        #if a student is infected, increment their num rounds by one
        #if a student's rounds are greater than their recovery time, have them recover


    def get_num_infected(self):
        '''
        Returns number of zombie students as an integer
        '''

    def get_num_immune(self):
        '''
        Returns number of immune/robot students as an integer
        '''

    def can_continue(self):
       ##TO_DO
        # returns false if every student is a robot
        # returns false if every student is a zombie
        #otherwise returns true

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
        #TO_DO
        #Only takes one line

    def strengthen_students(self):
        '''
        Reduces the susceptibility of all students by 10%
        '''
        #TO_DO
        #We suggest iterating through all students

    def shorten_cure_time(self):
        '''
        Shortens the time to cure of all students by 10%
        '''
        #TO_DO
        #We suggest iterating through all students

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
