from config import *
from comet import Comet


class CometFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.bar_color = comet_bar_color
        self.back_bar_color = comet_back_bar_color
        self.bar_height = comet_bar_height
        self.bar_speed = comet_bar_speed
        self.tmp = None
        self.reducing = False
        self.comets = pygame.sprite.Group()
        self.game = game
        self.resetting_bar = False

    def add_percent(self, amount):
        self.percent += amount / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.tmp = self.bar_color
        self.bar_color = self.back_bar_color
        self.back_bar_color = self.tmp
        if self.resetting_bar:
            self.resetting_bar = False
        else:
            self.resetting_bar = True
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, 10):
            self.comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.monsters) == 0 and not self.resetting_bar:
            self.meteor_fall()

    def update_bar(self, surface):
        if self.resetting_bar:
            self.add_percent(self.bar_speed * 10)
        else:
            self.add_percent(self.bar_speed)

        pygame.draw.rect(surface, self.back_bar_color, [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            self.bar_height
        ])
        pygame.draw.rect(surface, self.bar_color, [
            0,
            surface.get_height() - 20,
            surface.get_width() / 100 * self.percent,
            self.bar_height,
            ])
