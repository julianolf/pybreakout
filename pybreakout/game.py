import pygame


def main():
    pygame.init()
    pygame.display.set_caption('PyBREAKOUT')
    pygame.display.set_mode((480, 640))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()
