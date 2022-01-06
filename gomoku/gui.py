import pygame
from gomoku import Gomoku

TABLE_ORDER = 15
PIXELS_PER_ORDER = 40
N_PIXELS_TABLE = PIXELS_PER_ORDER * TABLE_ORDER


class Square(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((PIXELS_PER_ORDER - 1, PIXELS_PER_ORDER - 1))
        self.image.fill((155, 155, 155, 0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_click(self, mouse, gomoku: Gomoku):
        if self.rect.collidepoint(mouse):
            if gomoku.current_player_symbol == "O":
                self.image.fill((255, 255, 255, 0))
            else:
                self.image.fill((0, 0, 0, 0))
            pos = (self.rect.x // (PIXELS_PER_ORDER - 1), self.rect.y // (PIXELS_PER_ORDER - 1))
            gomoku.play(pos)


def run_gui():
    pygame.init()
    pygame.display.set_caption("Gomoku")
    w, h = (N_PIXELS_TABLE, N_PIXELS_TABLE)
    display_surface = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    squares_group = pygame.sprite.Group([
        Square(x, y)
        for x in range(0, w, PIXELS_PER_ORDER)
        for y in range(0, h, PIXELS_PER_ORDER)
    ])

    gomoku = Gomoku()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for square in squares_group:
                    square.check_click(event.pos, gomoku)

        squares_group.update()
        squares_group.draw(display_surface)
        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    run_gui()
