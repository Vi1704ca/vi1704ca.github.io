import pygame
import os

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((700, 700))

frame = pygame.Rect(100, 100, 515, 515)

shift = pygame.font.SysFont('Times New Romans', 45)
text = shift.render("Крестики нолики", True, (253, 0, 0))

squares = [
    pygame.Rect(120, 120, 145, 145),
    pygame.Rect(285, 120, 145, 145),
    pygame.Rect(450, 120, 145, 145),
    pygame.Rect(120, 285, 145, 145),
    pygame.Rect(285, 285, 145, 145),
    pygame.Rect(450, 285, 145, 145),
    pygame.Rect(120, 450, 145, 145),
    pygame.Rect(285, 450, 145, 145),
    pygame.Rect(450, 450, 145, 145)
]

directory = os.path.dirname(__file__)

image_x = pygame.image.load(os.path.join(directory, "pic", "image_x.png"))
image_o = pygame.image.load(os.path.join(directory, "pic", "image_o.png"))
icon = pygame.image.load(os.path.join(directory, "pic", "ico.png"))

pygame.display.set_icon(icon)

image_x_small = pygame.transform.scale(image_x, (145, 145))
image_o_small = pygame.transform.scale(image_o, (145, 145))

square_show = [False] * 9
player_moves = [None] * 9

game_over = False
winner = None

def check_win(moves):
    # Проверяем горизонтали
    if moves[0] == moves[1] == moves[2] and moves[0] is not None:
        return moves[0]
    if moves[3] == moves[4] == moves[5] and moves[3] is not None:
        return moves[3]
    if moves[6] == moves[7] == moves[8] and moves[6] is not None:
        return moves[6]
    # Проверяем вертикали
    if moves[0] == moves[3] == moves[6] and moves[0] is not None:
        return moves[0]
    if moves[1] == moves[4] == moves[7] and moves[1] is not None:
        return moves[1]
    if moves[2] == moves[5] == moves[8] and moves[2] is not None:
        return moves[2]
    # Проверяем диагонали
    if moves[0] == moves[4] == moves[8] and moves[0] is not None:
        return moves[0]
    if moves[2] == moves[4] == moves[6] and moves[2] is not None:
        return moves[2]
    return None

while not game_over:
    screen.fill((230, 230, 230))
    pygame.draw.rect(screen, (0, 0, 0), frame)

    for i in range(len(squares)):
        pygame.draw.rect(screen, (250, 250, 250), squares[i])
        if square_show[i]:
            if player_moves[i] == "x":
                screen.blit(image_x_small, squares[i])
            elif player_moves[i] == "o":
                screen.blit(image_o_small, squares[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not winner:
            for i in range(len(squares)):
                if squares[i].collidepoint(event.pos) and not square_show[i]:
                    if player_moves.count(None) % 2 == 0:
                        player_moves[i] = "x"
                    else:
                        player_moves[i] = "o"
                    square_show[i] = True
                    winner = check_win(player_moves)
                    if winner:
                        if winner == "x":
                            text = shift.render("Победил крестик!", True, (253, 0, 0))
                        elif winner == "o":
                            text = shift.render("Победил нолик!", True, (253, 0, 0))
                    elif all(square_show) and not winner:
                        text = shift.render("Победила дружба", True, (253, 0, 0))
                        
    screen.blit(text, (260, 45))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
