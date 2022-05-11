from config import *


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name: str, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 1
        self.images = animations.get(sprite_name)
        self.animation_speed = animation_speed
        self.animated = False
        self.sprite_name = sprite_name

    def start_animation(self):
        self.animated = True

    def animate(self, loop=False):

        if self.animated:
            if self.sprite_name in animation_slowing_sprites:
                self.current_image += self.animation_speed / 100
            else:
                self.current_image += 1

            if self.current_image >= len(self.images):
                self.current_image = 1
                if not loop:
                    self.animated = False

            self.image = self.images[int(self.current_image)]
            self.image = pygame.transform.scale(self.image, self.size)


def load_animation_images(sprite_name):
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"

    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(load(image_path))

    return images


animations = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien")
}
