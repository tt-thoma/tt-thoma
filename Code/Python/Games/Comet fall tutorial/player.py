import animation
from config import *
from projectile import Projectile


class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = player_health
        self.max_health = self.health
        self.attack = player_attack
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = resolution[0]/2-self.image.get_size()[0]/2
        self.rect.y = floor
        self.projectiles = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def launch_projectile(self):
        self.projectiles.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play("shot")

    def update_health_bar(self, surface):
        bar_pos = [self.rect.x + 50, self.rect.y + 20, self.max_health, player_health_bar_height]
        pygame.draw.rect(surface, player_health_bar_color_back, bar_pos)
        bar_pos = [self.rect.x + 50, self.rect.y + 20, self.health, player_health_bar_height]
        pygame.draw.rect(surface, player_health_bar_color, bar_pos)

    def move(self, direction):
        if direction == "right" and self.rect.x + self.rect.width < resolution[0]:
            if not self.game.check_collision(self, self.game.monsters):
                self.rect.x += self.speed

        if direction == "left" and self.rect.x > -25:
            self.rect.x -= self.speed
