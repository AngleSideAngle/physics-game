import os
import pygame
from pygame.locals import *

def getImage(img_name, size):
    img_path = os.path.join("resources", img_name)
    try:
        image = pygame.image.load(img_path)
        image = pygame.transform.scale(image, size)
    except pygame.error as eror:
        print(f"unable to load the image: {img_path}")
        raise SystemExit(eror)
    
    image = image.convert()

    return image, image.get_rect()

class avatar(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, velocity = [1,1], gravity = 1, color = "red"):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = getImage(img_name = "red.jpg", size = (100,100))
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity
        self.color = color
        self.gravity = gravity
        self.dimensions = pygame.display.get_surface().get_rect()

    def update(self, user_input = [0,0]):
        self.velocity[0] += user_input[0]
        self.velocity[1] =  self.velocity[1] + user_input[1] + self.gravity
        
        coords = self.rect.move(self.velocity)
        self.rect = coords

        if self.rect.left < self.dimensions.left or self.rect.right > self.dimensions.right:
            self.velocity[0] = -self.velocity[0]
            self.rect.x += self.velocity[0]
        if self.rect.top < self.dimensions.top or self.rect.bottom > self.dimensions.bottom:
            self.velocity[1] = -self.velocity[1] 
            self.rect.y += self.velocity[1]

    def jump(self, force):
        pass


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