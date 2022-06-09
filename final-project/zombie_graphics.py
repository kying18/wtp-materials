import sys
import pygame
import zombies as zombies

SCREENSIZE = (900, 600) #works for my laptop, should be changable
BLACK = (0, 0, 0)
GREY = (165, 182, 184)
num_students = SCREENSIZE[0]//100*(SCREENSIZE[1]//100-1)
school = zombies.School(num_students, 0.05) #starting with 1/20 infected
num_rounds = 0 #global rounds counter

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREENSIZE)
    zombie = pygame.image.load(r'zombie3.png')
    person = pygame.image.load(r'person2.png')
    robot = pygame.image.load(r'robot.png')
    while True:
        checkEvents()
        screen.fill(GREY)
        font = pygame.font.Font('freesansbold.ttf', 20)
        num_string = 'NUM_ROUNDS: ' + str(num_rounds) #counts rounds
        text = font.render(num_string, True, BLACK)
        cure = font.render('press \'c\' to cure a student', True, BLACK)
        beta = font.render('press \'b\' to cure a lower beta 10%', True, BLACK)
        strong = font.render('press \'s\' to strengthen all students 10%', True, BLACK)
        rect = text.get_rect()
        screen.blit(text, (0, SCREENSIZE[1]-100), area=rect)
        screen.blit(cure, (0, SCREENSIZE[1]-75))
        screen.blit(beta, (0, SCREENSIZE[1] - 50))
        screen.blit(strong, (0, SCREENSIZE[1] - 25))
        for j in range(SCREENSIZE[1]//100-1):
            for i in range(SCREENSIZE[0]//100):
                student_num = j*SCREENSIZE[0]//100+i
                state = school.list_students[student_num].get_state()
                if state == 'I':
                    screen.blit(pygame.transform.scale(zombie, (100, 100)), (100*i,100*j))
                if state == 'S':
                    screen.blit(pygame.transform.scale(person, (100, 100)), (100 * i, 100 * j))
                if state == 'R':
                    screen.blit(pygame.transform.scale(robot, (100, 100)), (100 * i, 100 * j))

        if school.get_num_infected() == school.school_size:
            screen.blit(pygame.transform.scale(zombie, SCREENSIZE), (0, 0))
            lose = font.render('you lose!!', True, BLACK)
            lose_stats = font.render('you survived ' + str(num_rounds) + ' rounds', True, BLACK)
            screen.blit(lose, (SCREENSIZE[0]//2-50, SCREENSIZE[1]//2-200))
            screen.blit(lose_stats, (SCREENSIZE[0]//2-120, SCREENSIZE[1]//2-150))

        if school.get_num_infected() == 0:
            screen.blit(pygame.transform.scale(person, SCREENSIZE), (0, 0))
            lose = font.render('you win!!', True, BLACK)
            lose_stats = font.render('you took ' + str(num_rounds) + ' rounds', True, BLACK)
            screen.blit(lose, (SCREENSIZE[0]//2-50, SCREENSIZE[1]//2-200))
            screen.blit(lose_stats, (SCREENSIZE[0]//2-120, SCREENSIZE[1]//2-150))



        pygame.display.update()


def checkEvents():
    global num_rounds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                school.cure_student()
            if event.key == pygame.K_b:
                school.lower_beta()
                print(f'{school.beta}')
            if event.key == pygame.K_s:
                school.strengthen_students()
            school.infect_round()
            if school.can_continue():
                num_rounds += 1

if __name__ == '__main__':
    main()
