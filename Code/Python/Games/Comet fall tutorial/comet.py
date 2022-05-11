from config import *


class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.speed = randint(2, 5)
        self.rect.x = randint(0, roundplus(resolution[0] * 0.8))
        self.rect.y = - randint(10, 800)
        self.comet_event = comet_event
        self.damage_dealing = comet_damage

    def remove(self):
        self.comet_event.comets.remove(self)

        if len(self.comet_event.comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.game.start()

    def fall(self):
        if self.rect.y >= resolution[1] + 20:
            self.remove()

        if self.comet_event.game.check_collision(self, self.comet_event.game.player):
            self.comet_event.game.player.damage(self.damage_dealing)
            self.comet_event.game.sound_manager.play("meteor")
            self.remove()

        self.rect.y += self.speed
