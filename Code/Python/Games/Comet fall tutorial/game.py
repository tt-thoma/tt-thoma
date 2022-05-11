from config import *
from comet_event import CometFallEvent
import pygame.sprite
from player import Player
from monster import Mummy, Alien
from sounds import SoundManager


class Game:
    def __init__(self):
        self.is_running = False
        self.players = pygame.sprite.Group()
        self.player = Player(self)
        self.players.add(self.player)
        self.monsters = pygame.sprite.Group()
        self.pressed = {}
        self.monstercount = monster_count
        self.comet_event = CometFallEvent(self)
        self.score = 0
        self.sound_manager = SoundManager()
        if custom_font:
            self.font = pygame.font.Font(custom_font_path, score_font_size)
        else:
            self.font = pygame.font.SysFont(score_font_name, score_font_size)

    def start(self):
        self.is_running = True
        self.spawn_monsters()

    def game_over(self):
        self.monsters = pygame.sprite.Group()
        self.comet_event.cometes = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_running = False
        self.comet_event.reset_percent()
        self.score = 0
        self.sound_manager.play("game_over")

    def update(self, screen):

        score_text = self.font.render(f"- {self.score} -", True, score_font_color)
        insert(score_text,
               (resolution[0]/2 - score_font_size/2 * (len(str(self.score)) - 1), 20)  # Get in the damn middle
               )

        insert(self.player.image, self.player.rect)
        self.comet_event.update_bar(window)

        if self.comet_event.is_full_loaded() and self.comet_event.resetting_bar:
            self.comet_event.reset_percent()

        self.player.update_health_bar(screen)

        self.player.update_animation()

        self.comet_event.comets.draw(window)

        for projectile in self.player.projectiles:
            projectile.move()

        for monster in self.monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.animation_update()

        for comet in self.comet_event.comets:
            comet.fall()

        self.player.projectiles.draw(screen)
        self.monsters.draw(window)

        if self.pressed.get(pygame.K_RIGHT):
            self.player.move("right")
        elif self.pressed.get(pygame.K_LEFT):
            self.player.move("left")

    def check_collisiontwo(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False)

    def check_collision(self, sprite, other):
        if type(other) == pygame.sprite.Group:
            for thing in other:
                return pygame.sprite.collide_mask(sprite, thing)
        else:
            return pygame.sprite.collide_mask(sprite, other)

    def spawn_monster(self, monster):
        self.monsters.add(monster.__call__(self))

    def spawn_monsters(self):
        for i in range(self.monstercount):
            if randint(0, alien_spawn_chance) == 0 or len(self.monsters) < 1:
                self.spawn_monster(Alien)

            self.spawn_monster(Mummy)
