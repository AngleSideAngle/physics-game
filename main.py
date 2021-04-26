from pygame.locals import *
from avatar import avatar, pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,600))
    pygame.display.set_caption("amogus")
    pygame.key.set_repeat(1,10)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    player = avatar(x = background.get_width()/2, y = background.get_height()/2, color = "red")
    allsprites = pygame.sprite.RenderPlain((player))
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        user_input = [0,0]
        jump = False
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return

            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_w or event.key == K_UP):
                jump = True
            if event.type == KEYDOWN and (event.key == K_a or event.key == K_LEFT):
                user_input[0] -= 1
            if event.type == KEYDOWN and (event.key == K_d or event.key == K_RIGHT):
                user_input[0] += 1

        allsprites.update(user_input = user_input, jump = jump)

        screen.blit(background, (0,0))
        allsprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()