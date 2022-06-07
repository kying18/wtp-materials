import sys
import pygame
import zombies as zombies

SCREENSIZE = (900, 600)
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
num_students = SCREENSIZE[0]//100*(SCREENSIZE[1]//100-1)
school = zombies.school(num_students, 0.05)
num_rounds = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREENSIZE)
    zombie = pygame.image.load(r'zombie3.png')
    person = pygame.image.load(r'person2.png')
    robot = pygame.image.load(r'robot.png')
    while True:
        checkEvents()
        screen.fill(GREY)
        font = pygame.font.Font('freesansbold.ttf', 32)
        num_string = 'NUM_ROUNDS: ' + str(num_rounds)
        text = font.render(num_string, True, BLACK)
        cure = font.render('press \'c\' to cure a student', True, BLACK)
        rect = text.get_rect()
        screen.blit(text, (0, SCREENSIZE[1]-100), area=rect)
        screen.blit(cure, (0, SCREENSIZE[1]-50))
        for j in range(SCREENSIZE[1]//100-1):
            for i in range(SCREENSIZE[0]//100):
                student_num = j*SCREENSIZE[0]//100+i
                print(student_num)
                state = school.list_students[student_num].get_state()
                print('state = ', state)
                if state == 'I':
                    screen.blit(pygame.transform.scale(zombie, (100, 100)), (100*i,100*j))
                if state == 'S':
                    screen.blit(pygame.transform.scale(person, (100, 100)), (100 * i, 100 * j))
                if state == 'R':
                    screen.blit(pygame.transform.scale(robot, (100, 100)), (100 * i, 100 * j))


        pygame.display.update()


def checkEvents():
    global num_rounds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                school.cure_student()
            print('infecting round')
            school.infect_round()
            num_rounds += 1

if __name__ == '__main__':
    main()
