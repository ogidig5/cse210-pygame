import pygame
from constants import *
from game.paddle1 import Paddle1
from game.paddle2 import Paddle2
from game.ball import Ball

class Director:

    def __init__(self):
        pygame.init()

        self.win = pygame.display.set_mode((750, 500))

        pygame.display.set_caption('Pong Game')

        self.paddle1 = Paddle1()
        self.paddle1.rect.x = 25
        self.paddle1.rect.y = 225

        self.paddle2 = Paddle2()
        self.paddle2.rect.x = 715
        self.paddle2.rect.y = 225

        self.ball = Ball()
        self.ball.rect.x = 375
        self.ball.rect.y = 250

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.paddle1, self.paddle2, self.ball)

        self.run = True

    def playGame(self):
        while self.run:

            pygame.time.delay(10)

            # Quit Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            # Paddle Movement
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and self.paddle1.rect.y > 0:
                self.paddle1.rect.y -= PADDLE_SPEED
            if key[pygame.K_s] and self.paddle1.rect.y < 425:
                self.paddle1.rect.y += PADDLE_SPEED
            if key[pygame.K_UP] and self.paddle2.rect.y > 0:
                self.paddle2.rect.y -= PADDLE_SPEED
            if key[pygame.K_DOWN] and self.paddle2.rect.y < 425:
                self.paddle2.rect.y += PADDLE_SPEED

            # Moves pong ball
            self.ball.rect.x += self.ball.speed * self.ball.dx
            self.ball.rect.y += self.ball.speed * self.ball.dy

            # Wall and Paddle Bounces
            if self.ball.rect.y > 490:
                self.ball.dy = -1

            if self.ball.rect.y < 1:
                self.ball.dy = 1

            if self.ball.rect.x > 740:
                self.ball.rect.x, self.ball.rect.y = 375, 250
                self.ball.dx = -1
                self.paddle1.points += 1

            if self.ball.rect.x < 1:
                self.ball.rect.x, self.ball.rect.y = 375, 250
                self.ball.dx = 1
                self.paddle2.points += 1

            if self.paddle1.rect.colliderect(self.ball.rect):
                self.ball.dx = 1

            if self.paddle2.rect.colliderect(self.ball.rect):
                self.ball.dx = -1

            # Runs redraw function above
            self.redraw()

        pygame.quit()

    def redraw(self):
    # Draws black screen
        self.win.fill(BLACK)

        # Title font
        font = pygame.font.SysFont('Chiller', 30)
        text = font.render('PONG', False, WHITE)
        textRect = text.get_rect()
        textRect.center = (750 // 2, 25)
        self.win.blit(text, textRect)

        # Player 1 Score
        p1_score = font.render(str(self.paddle1.points), False, WHITE)
        p1Rect = p1_score.get_rect()
        p1Rect.center = (50, 50)
        self.win.blit(p1_score, p1Rect)

        # Player 2 Score
        p2_score = font.render(str(self.paddle2.points), False, WHITE)
        p2Rect = p2_score.get_rect()
        p2Rect.center = (700, 50)
        self.win.blit(p2_score, p2Rect)

        # Updates all Sprites
        self.all_sprites.draw(self.win)

        # Draws updates
        pygame.display.update()
