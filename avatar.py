from functions import getImage, pygame

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