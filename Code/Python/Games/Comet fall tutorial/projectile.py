from config import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.speed = projectile_speed
        self.player = player
        self.image = load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 100
        self.origin_image = self.image
        self.angle = randint(0, 359)
        self.rotation_speed = projectile_rotation_speed

    def rotate(self):
        self.angle += self.rotation_speed
        self.image = pygame.transform.rotate(self.origin_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.projectiles.remove(self)

    def move(self):
        if self.rect.x < resolution[0]:
            self.rotate()
            self.rect.x += self.speed
        else:
            self.remove()

        for monster in self.player.game.check_collisiontwo(self, self.player.game.monsters):
            monster.damage(randint(self.player.attack, self.player.attack + 3))
            self.remove()
