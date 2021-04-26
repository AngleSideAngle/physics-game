import os
import pygame
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

def collide(object, border, axis):
    directions = {
        "left" : (object.dimensions.left, object.rect.left),
        "right" : (object.dimensions.right, object.rect.right),
        "top" : (object.dimensions.top, object.rect.top),
        "bottom" : (object.dimensions.bottom, object.rect.bottom)
    }
    difference = directions[border][0] - directions[border][1]
    object.velocity[axis] = -object.velocity[axis]
    object.velocity[axis] /= object.bounce
    return difference
    

    '''
    for axis in range(len(direction)):
        if direction[axis] == True:
            object.velocity[axis] = -object.velocity[axis] # changes speed

    move_back = object.velocity # amount object must return
    
    for axis in range(len(direction)):
        if direction[axis] == True:
            object.velocity[axis] /= object.bounce # reduces speed
            '''