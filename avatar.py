from os import terminal_size
from functions import getImage, collide, pygame

class avatar(pygame.sprite.Sprite):
    def __init__(self, 
    x = 0, 
    y = 0, 
    velocity = [0,0], 
    gravity = 1, 
    bounce = 1.1, 
    strength = 10, 
    jumps = 2, 
    terminal_velocity = 25,
    ground_boundary = 50, 
    color = "red"
    ):
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
        self.terminal_velocity = terminal_velocity
        self.ground_boundary = ground_boundary

        self.dimensions = pygame.display.get_surface().get_rect()

    def update(self, user_input = [0,0], jump = False):
        self.velocity[0] += user_input[0]
        self.velocity[1] += user_input[1]

        coords = self.rect.move(self.velocity)
        self.rect = coords

        if not self.dimensions.contains(coords):
            difference = [0, 0]
            # horizontal borders of the screen
            if self.rect.left < self.dimensions.left:
                difference[0] = collide(self, "left", 0)
            elif self.rect.right > self.dimensions.right:
                difference[0] = collide(self, "right", 0)
            

            if self.rect.top < self.dimensions.top:
                difference[1] = collide(self, "top", 1)
            elif self.rect.bottom > self.dimensions.bottom:
                difference[1] = collide(self, "bottom", 1)

            coords = self.rect.move(difference)
            self.rect = coords

            if self.jumps < self.max_jumps:
                self.jumps += 1
        
            # might cause character to glitch into wall
            if self.velocity[0] > 0:
                self.velocity[0] -= 1
            elif self.velocity[0] < 0:
                self.velocity[0] += 1
            
        self.velocity[1] += self.gravity

        # terminal velocity
        for index in range(len(self.velocity)):
            if self.velocity[index] > self.terminal_velocity:
                self.velocity[index] = self.terminal_velocity
            elif self.velocity[index] < -self.terminal_velocity:
                self.velocity[index] = -self.terminal_velocity
            
        if self.rect.bottom < self.ground_boundary and -1 < self.velocity[1]:
            self.velocity[1] = 0

    
        if jump == True:
            self._jump()

    def _jump(self):
        if self.jumps > 0:
            self.velocity[1] -= self.strength
            self.jumps -= 1