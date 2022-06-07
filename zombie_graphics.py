import sys
import pygame
import zombies as zombies

SCREENSIZE = (800, 600)
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
school = zombies.school(48, 0.05)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREENSIZE)
    zombie = pygame.image.load(r'zombie.png')
    person = pygame.image.load(r'person.png')
    while True:
        checkEvents()
        screen.fill(GREY)
        for j in range(SCREENSIZE[1]//100):
            for i in range(SCREENSIZE[0]//100):
                student_num = j*SCREENSIZE[0]//100+i
                print(student_num)
                state = school.list_students[student_num].get_state()
                print('state = ', state)
                if state == 'I':
                    screen.blit(pygame.transform.scale(zombie, (100, 100)), (100*i,100*j))
                if state == 'S':
                    screen.blit(pygame.transform.scale(person, (100, 100)), (100 * i, 100 * j))
        pygame.display.update()


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print('infecting round')
            school.infect_round()

if __name__ == '__main__':
    main()
