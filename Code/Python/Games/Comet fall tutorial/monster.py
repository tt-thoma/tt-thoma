from config import *
import animation


class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = None
        self.speed = None
        self.max_health = None
        self.attack = None
        self.rect = self.image.get_rect()
        self.rect.x = resolution[0] + randint(100, 750)
        self.rect.y = floor + self.image.get_size()[1]/3 - offset
        self.start_animation()
        self.death_points = None

    def set_speed(self, speed):
        self.speed = randint(round(speed - speed/2), speed)
        if self.speed == 0:
            self.speed = speed

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.score += self.death_points
            if self.game.comet_event.is_full_loaded() and not self.game.comet_event.resetting_bar:
                self.game.monsters.remove(self)
                self.game.comet_event.attempt_fall()
            else:
                self.rect.x = resolution[0] + randint(0, 750)
                self.health = self.max_health

    def animation_update(self):
        self.animate(True)

    def update_health_bar(self, surface):
        bar_pos = [self.rect.x + 10, self.rect.y - 20, self.max_health, monster_health_bar_height]
        pygame.draw.rect(surface, monster_health_bar_color_back, bar_pos)
        bar_pos = [self.rect.x + 10, self.rect.y - 20, self.health, monster_health_bar_height]
        pygame.draw.rect(surface, monster_health_bar_color, bar_pos)

    def forward(self):
        if not self.game.check_collision(self, self.game.player):
            self.rect.x -= self.speed
        else:
            self.game.player.damage(self.attack)

        if self.rect.x < -100:
            self.damage(self.max_health)


class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.health = mummy_health
        self.max_health = mummy_health
        self.attack = monster_attack
        self.set_speed(mummy_speed)
        self.death_points = mummy_death_points


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 200)
        self.health = alien_health
        self.max_health = alien_health
        self.attack = alien_attack
        self.set_speed(alien_speed)
        self.death_points = alien_death_points
