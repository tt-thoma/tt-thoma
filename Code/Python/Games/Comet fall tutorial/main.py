from config import *
from game import Game
from math import ceil

pygame.init()

clock = pygame.time.Clock()


disp.set_caption("Comet Fall Game")

bg = load("assets/bg.jpg")

banner = load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = ceil(resolution[0]/2 - banner.get_size()[0]/2)

launch_button = load("assets/button.png")
launch_button = pygame.transform.scale(launch_button, (400, 150))
launch_button_rect = launch_button.get_rect()
launch_button_rect.x = ceil(resolution[0]/2 - launch_button.get_size()[0]/2)
launch_button_rect.y = ceil(resolution[1]/2)

game = Game()

running = True

while running:

    insert(bg, (0, -200))

    if game.is_running:
        game.update(window)
    else:
        insert(launch_button, launch_button_rect)
        insert(banner, banner_rect)

    refresh()

    for e in event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            game.pressed[e.key] = True

            if e.key == pygame.K_SPACE:
                if game.is_running:
                    game.player.launch_projectile()
                else:
                    game.start()
                    game.sound_manager.play("click")

        elif e.type == pygame.KEYUP:
            game.pressed[e.key] = False

        elif e.type == pygame.MOUSEBUTTONDOWN:
            if launch_button_rect.collidepoint(e.pos):
                game.start()
                game.sound_manager.play("click")

    clock.tick(FPS)
