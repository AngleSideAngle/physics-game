from avatar import avatar, pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("amogus")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    amogus = avatar(x = 100, y = 100, velocity = [5,5], gravity = 1)
    allsprites = pygame.sprite.RenderPlain((amogus))
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        user_input = [0,0]
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            if event.type == KEYDOWN and event.key == K_a:
                user_input[0] -= 1
            if event.type == KEYDOWN and event.key == K_d:
                user_input[0] += 1

        allsprites.update(user_input = user_input)

        screen.blit(background, (0,0))
        allsprites.draw(screen)
        pygame.display.flip()
        
main()