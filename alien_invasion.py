import sys
import pygame
from settings import Settings
from pygame.sprite import Group
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf
import time
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button=Button(ai_settings, screen, "Fight!!!")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    bullets = Group()
    aliens = Group()
    ship = Ship(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    alien = Alien(ai_settings, screen)

    pygame.mixer.music.load("bgm/music.mp3")
    while True:
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
        gf.check_events(ai_settings, screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, sb,screen, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()