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
        self.state = state
        #this might seem silly but it's important so we bind that original state to each Student object

    def interact(self):
        '''
        returns a boolean based on whether or not an interaction with an infected student results in an infection
        "R" = resistant and no infection will occur
        '''
        if self.get_state() == 'R':
            return False
        strength = random.random() #random value of infection strength
        if 1-self.sus < strength: #if student strength is less than virus strength, infected
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
        Sets the state given 'I', 'S', or 'R'
        '''
        assert state in ['S', 'I', 'R'] #do we want to cover assert statements?
        self.state = state

class School(object):
    def __init__(self, num_students, initial_spread, BETA=2):
        '''
        Constructs a school given a number of students and the initial probability of infection.
        '''
        self.BETA = BETA
        self.list_students = []
        for student in range(num_students):
            rand_disease = random.choices(['S', 'I'], weights=[1-initial_spread, initial_spread])[0]
            self.list_students.append(Person(rand_disease))
        self.school_size = num_students

    def infect_round(self):
        '''
        Simulates a day of student interactions, controlled by the sociality variable 'BETA"
        '''
        infected_students = []
        for student in self.list_students:
            if student.get_state() == 'I':
                infected_students.append(student)
        for _ in infected_students:
            for i in range(self.BETA):
                contact = random.randint(0, self.school_size-1)
                infected = self.list_students[contact].interact()
                if infected:
                    self.list_students[contact].set_state('I')

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
        robo_count = 0
        for student in self.list_students:
            if student.get_state() == 'R':
                robo_count += 1
                print(robo_count)
                print('school size =', self.school_size)
        if robo_count == self.school_size:
            print('returning false')
            return False
        else:
            return True

    def cure_student(self):
        random_list = self.list_students.copy()
        random.shuffle(random_list)
        if self.get_num_infected() == 0:
            print('no student to cure')
        else:
            for student in random_list:
                if student.get_state() == 'I':
                    student.set_state('R')
                    return None




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


