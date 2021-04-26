from functions import getImage, pygame

class avatar(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, velocity = [0,0], gravity = 1, bounce = 1.1, strength = 10, jumps = 2, color = "red"):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = getImage(img_name = "red.jpg", size = (80,80))
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity
        self.color = color
        self.gravity = gravity
        self.bounce = bounce # will divide upon ground impact
        self.strength = strength
        self.jumps = jumps
        self.max_jumps = jumps
        self.dimensions = pygame.display.get_surface().get_rect()

    def update(self, user_input = [0,0]):
        self.velocity[0] += user_input[0]
        self.velocity[1] += user_input[1] + self.gravity
        
        if self.velocity[0] > 0:
            self.velocity[0] -= 1
        elif self.velocity[0] < 0:
            self.velocity[0] += 1

        coords = self.rect.move(self.velocity)
        self.rect = coords

        # horizontal borders
        if self.rect.left < self.dimensions.left or self.rect.right > self.dimensions.right:
            self.velocity[0] = -self.velocity[0]
            self.rect.x += self.velocity[0]

        # bottom of the screen
        if self.rect.bottom > self.dimensions.bottom:
            self.velocity[1] = -self.velocity[1]
            self.rect.y += self.velocity[1]
            self.velocity[1] /= self.bounce
            # set velocity to 0 if it is negligable
            if self.velocity[1] > -1:
                self.velocity[1] = 0
            # update jump counter
            if self.jumps < self.max_jumps:
                self.jumps += 1
        
        # top of the screen
        if self.rect.top < self.dimensions.top:
            self.velocity[1] = -self.velocity[1]
            self.rect.y += self.velocity[1]
            self.velocity[1] /= self.bounce

    def jump(self):
        if self.jumps > 0:
            self.velocity[1] -= self.strength
            self.jumps -= 1