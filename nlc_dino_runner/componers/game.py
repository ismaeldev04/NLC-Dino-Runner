import pygame

from nlc_dino_runner.componers.powerups.lifes import Life
from nlc_dino_runner.componers.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import texxt_utils
from nlc_dino_runner.componers.obstacles.cactus import Cactus
from nlc_dino_runner.componers.obstacles.obstacle_manager import ObstacleManager
from nlc_dino_runner.utils.constants import (
    TITTLE,
    ICON,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BG

)
from nlc_dino_runner.componers.dinosaurio import Dinosaur
from nlc_dino_runner.utils.texxt_utils import black_color


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 30
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.hearth = Life()

    def print_number_lifes(self):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render(str(self.obstacle_manager.lifes), True, black_color)
        text_rect = text.get_rect()
        text_rect.center = (60, 10)
        self.screen.blit(text, text_rect.center)

    def score(self):
        self.points += 1
        if self.points % 20 == 0:
            self.game_speed += 1
        score_element, score_element_rec = texxt_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rec)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        half_width = SCREEN_WIDTH // 2
        half_height = SCREEN_HEIGHT // 2
        if self.death_count > 0:
            text_element, text_element_rec = texxt_utils.get_centered_message('press any key to restart')
        else:
            text_element, text_element_rec = texxt_utils.get_centered_message('press any key to start')
        self.screen.blit(text_element, text_element_rec)
        if self.death_count > 0:
            text_element, text_element_rec = texxt_utils.get_centered_message('death Count : ' + str(self.death_count), height = half_height + 50)
        self.screen.blit(text_element, text_element_rec)
        self.screen.blit(ICON, (half_width - 40, half_height - 150))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

    def run(self):
        self.points = 0
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(30)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        self.hearth.draw(self.screen)
        self.print_number_lifes()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_with = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_with:
            self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
