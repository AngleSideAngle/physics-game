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