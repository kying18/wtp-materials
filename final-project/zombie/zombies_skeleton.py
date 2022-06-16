import random
sus_range = (1, 1) #tuple of low and high bounds for susceptibility

class Person(object):
    def __init__(self, state):
        '''
        Initial constructor of a person. Holds their susceptibility (float, range 0:1), and state.
        'I' = infected (aka zombie)
        'S' = susceptible (human)
        'R' = recovered + immune (cured and incapable of becoming a zombie again)
        '''
        self.sus = random.uniform(*sus_range) #unpacking notation
        #equivalent to = random.uniform(sus_range[0], sus_range[1])

        #what other statement do we need here?

    def interact(self):
        '''
        returns a boolean based on whether or not an interaction with an infected student results in an infection
        "R" = resistant and no infection will occur
        '''
        if self.get_state() == 'R':
           ##return what here
        viral_strength = random.random() #random value of infection strength
        student_strength = 1 - self.sus
        if student_strength < viral_strength: #if student strength is less than virus strength, infected
            ##what about this case
        ##return something here??

    def get_state(self):
        '''
        Returns the state, either 'I', 'S', or 'R'
        :return:
        '''
        ###
        #What can we write to get the state of a student?
        ###

    def set_state(self, state):
        '''
        Sets the state given 'I', 'S', or 'R'
        '''
        ###
        #How can we *set* the state of a student

class School(object):
    def __init__(self, num_students, initial_spread, beta=2): #discuss including variable name in header?
        '''
        Constructs a school given a number of students and the initial probability of infection.
        '''
        ##Bind beta here
        self.list_students = []
        #creating a list of students, with a random chance of the disease
        for student in range(num_students):
            rand_disease = random.choices(['S', 'I'], weights=[1-initial_spread, initial_spread])[0] #weighted choices, unpacking list
            self.list_students.append(Person(rand_disease))
        self.school_size = ### what?

    def infect_round(self):
        '''
        Simulates a day of student interactions, controlled by the sociality variable 'BETA"
        '''
        #generate a list of infected students

        ##TO_DO

        #for each infected student, have them interact with some random subset of students
        for _ in infected_students:
            for i in range(round(self.beta)): #in this code, beta can be a float
                print('infecting student', i, 'for beta', self.beta)
                contact = random.randint(0, self.school_size-1)
                infected = self.list_students[contact].interact()
                if infected:
                    self.list_students[contact].set_state('I')

    def get_num_infected(self):
        '''
        Returns number of zombie students as an integer
        '''
        ##TO_DO implementation

    def can_continue(self):
        if self.school_size == self.get_num_infected():
            return False
        robo_count = 0
        #generate count of resistant/robot students

        ## TO_DO ##

        if robo_count == self.school_size:
            return False
        else:
            return True

    ###
    #METHODS TO LOWER INFECTION RATES
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
        ##TO_DO implement

    def strengthen_students(self):
        '''
        Reduces the susceptibility of all students by 10%
        '''
        ##TO_DO implement





    def __str__(self):
        '''
        overwrites main to_string method for helpful command-line debugging
        '''
        string = ''
        total_length = len(self.list_students)
        repr_dict = {'S': 'o', 'I': 'z', 'R': 'R'} #shows o for students and z for zombies
        for ix in range(total_length):
            string += repr_dict[self.list_students[ix].get_state()] + ' ' #adds each student
            if (ix+1) % 15 == 0: #line breaks every 15 students
                string += '\n'
        return string


    def __repr__(self):
        for student in self.list_students:
            print('Student', student.get_state())

if __name__ == "__main__":
    '''
    Runs a school simulation of size 75 with an initial infection chance of 1/20
    '''
    school = School(75, 0.05)
    start = input('Welcome, school administrator. Your school has been infected with a zombie virus. Type \'YES\' to start the simulation.')
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

