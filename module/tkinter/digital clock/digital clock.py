import pygame
import time
screen_size = [700, 700]
# enter time:
# count time:
def add(hour, minute, second):
    # global hour
    #    global minute
    #    global second
    # increase time
    while True:
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        second = second+1
        if second == 60:
            minute = minute+1
            second = 0
        if minute == 60:
            hour = hour+1
            minute = 0
        if hour == 24:
            hour = 0
        hour = str(hour)
        minute = str(minute)
        second = str(second)
        if len(str(hour)) == 2:
            x1 = hour[0]
            x2 = hour[1]

        else:
            x1 = 0
            x2 = hour[0]

        # minute
        if len(str(minute)) == 2:
            x3 = minute[0]
            x4 = minute[1]

        else:
            x3 = 0
            x4 = minute[0]

        # sec
        if len(str(second)) == 2:
            x5 = second[0]
            x6 = second[1]

        else:
            x5 = 0
            x6 = second[0]

        # image load
        time.sleep(1)

        h1 = pygame.image.load(f'{x1}.png')
        h2 = pygame.image.load(f'{x2}.png')
        m1 = pygame.image.load(f'{x3}.png')
        m2 = pygame.image.load(f'{x4}.png')
        s1 = pygame.image.load(f'{x5}.png')
        s2 = pygame.image.load(f'{x6}.png')
        colon = pygame.image.load('colon.png')
        screen = pygame.display.set_mode(screen_size)
        screen.blit(h1, [300, 300])

        screen.blit(h2, [350, 300])

        screen.blit(colon, [400, 295])

        screen.blit(m1, [450, 300])

        screen.blit(m2, [500, 300])

        screen.blit(colon, [550, 295])

        # sec
        screen.blit(s1, [600, 300])

        screen.blit(s2, [650, 300])
        pygame.display.update()


clock = add(1, 0, 50)
