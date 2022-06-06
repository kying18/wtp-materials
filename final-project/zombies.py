import random
BETA = 2 #number of students infected by each per day

class person(object):
    def __init__(self, sus, state):
        self.sus = sus
        self.state = state

    def interact(self):
        '''
        returns a boolean based on whether or not an interaction with an infected student results in an infection, also changes state
        '''
        return True

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

class school(object):
    def __init__(self, num_students):
        self.list_students = []
        for student in range(num_students):
            rand_disease = random.choices(['S', 'I'], weights=[90, 10])[0]
            self.list_students.append(person(1, rand_disease))
        self.school_size = num_students

    def infect_round(self):
        infected_students = []
        for student in self.list_students:
            if student.get_state() == 'I':
                infected_students.append(student)
        for student in infected_students:
            for i in range(BETA):
                contact = random.randint(0, self.school_size-1)
                infected = self.list_students[contact].interact()
                if infected:
                    self.list_students[contact].set_state('I')

    def get_num_infected(self):
        count = 0
        for student in self.list_students:
            if student.get_state() == 'I':
                count += 1
        return count




    def __str__(self):
        string = ''
        count = 0
        total_length = len(self.list_students)
        width = round((total_length)**(1/2))
        repr_dict = {'S': 'o', 'I': 'z'}
        overall_string = ''
        for ix in range(total_length):
            string += repr_dict[self.list_students[ix].get_state()] + ' '
            if (ix+1) % 15 == 0:
                string += '\n'
        return string

    def __repr__(self):
        for student in self.list_students:
            print('Student', student.get_state())

if __name__ == "__main__":
    school = school(75)
    start = input('Welcome, school administrator. Your school has been infected with a zombie virus. Type \'YES\' to start the simulation.')
    if start:
        print(school)
        num_rounds = 0
    while True:

        next = input('Press enter to start the next round')
        if next == '':
            school.infect_round()
            print('after infection')
            print(school)
            num_rounds += 1
            print('num_rounds', num_rounds)
            if school.get_num_infected() == school.school_size:
                print('All your students are now zombies. Your school survived', num_rounds-1, 'rounds')
                exit()


