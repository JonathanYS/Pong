"""
This program was written by Yonatan Deri.
"""
import pygame
import time

from utils.menu import Menu
from utils.consts import Constants
from utils.audio import Audio
from utils import ball, text, player

pygame.display.set_caption("Pong")

RETRY_OPTION_IMAGE = "Images/retry_option.png"
EXIT_AT_START_MENU = "Images/exit_at_start_menu.png"
EXIT_OPTION = "Images/exit_option.png"
START_OPTION = "Images/start_option.png"

DELAY = 5

menu_obj = Menu(Constants.SCREEN.value)
menu_mode = False
start_menu_mode = True


def check_end_game(player1_score: int, player2_score: int):
    global menu_obj, menu_mode
    if player1_score == 3 or player2_score == 3:
        if player1_score == 3:
            clear_screen()
            text.text_to_screen(Constants.SCREEN.value, f"GAME OVER", Constants.WIDTH.value // 2 - 260,
                                Constants.HEIGHT.value // 2 - 100)
            text.text_to_screen(Constants.SCREEN.value, f"Player 1 has won!", Constants.WIDTH.value // 2 - 375,
                                Constants.HEIGHT.value // 2)
            pygame.display.update()
            time.sleep(DELAY)
        else:
            clear_screen()
            text.text_to_screen(Constants.SCREEN.value, f"GAME OVER", Constants.WIDTH.value // 2 - 260,
                                Constants.HEIGHT.value // 2 - 100)
            text.text_to_screen(Constants.SCREEN.value, f"Player 2 has won!", Constants.WIDTH.value // 2 - 375,
                                Constants.HEIGHT.value // 2)
            pygame.display.update()
            time.sleep(DELAY)

        menu_obj.display_image(img_path=RETRY_OPTION_IMAGE, pos_x=0, pos_y=0)
        menu_mode = True


def display_start_menu() -> None:
    clear_screen()
    menu_obj.display_image(img_path=START_OPTION, pos_x=0, pos_y=0)


def handle_chosen_option():
    global menu_mode, start_menu_mode
    option = menu_obj.get_option()
    match option:
        case 0:
            menu_mode = False
            clear_screen()
            main()
        case 2:
            start_menu_mode = False
            clear_screen()
            main()
        case _:
            exit(0)


def clear_screen() -> None:
    Constants.SCREEN.value.fill(Constants.BLACK.value)


def main() -> None:
    player_1, player_2, players, ball_obj, player1_score, player2_score, player1_status, player2_status = None, None,\
                                                                                                          None, None,\
                                                                                                          None, None,\
                                                                                                          None, None
    if start_menu_mode is False:
        player_1 = player.Player(10, Constants.WHITE.value, 100, 0, 15, 125)
        player_2 = player.Player(10, Constants.WHITE.value, Constants.WIDTH.value - 125, 0, 15, 125)
        ball_obj = ball.Ball(7, Constants.WIDTH.value // 2, Constants.HEIGHT.value // 2, 6, Constants.WHITE.value)

        # The two players are not moving at the beginning (0 for standing, 1 for moving down and -1 for moving up).
        player1_status, player2_status = 0, 0

        # The two players' scores
        player1_score, player2_score = 0, 0

        # List of players for the collision detection.
        players = [player_1, player_2]

        text.text_to_screen(Constants.SCREEN.value, f"{player2_score}", Constants.WIDTH.value - 60, 0)
        text.text_to_screen(Constants.SCREEN.value, f"{player1_score}", 20, 0)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_w:
                        if start_menu_mode is False:
                            if menu_mode is True:
                                menu_obj.display_image(img_path=RETRY_OPTION_IMAGE, pos_x=0, pos_y=0)
                            else:
                                player1_status = -1
                        else:
                            menu_obj.display_image(img_path=START_OPTION, pos_x=0, pos_y=0)
                    case pygame.K_s:
                        if start_menu_mode is False:
                            if menu_mode is True:
                                menu_obj.display_image(img_path=EXIT_OPTION, pos_x=0, pos_y=0)
                            else:
                                player1_status = 1
                        else:
                            menu_obj.display_image(img_path=EXIT_AT_START_MENU, pos_x=0, pos_y=0)
                    case pygame.K_UP:
                        if start_menu_mode is False:
                            if menu_mode is True:
                                menu_obj.display_image(img_path=RETRY_OPTION_IMAGE, pos_x=0, pos_y=0)
                            else:
                                player2_status = -1
                        else:
                            menu_obj.display_image(img_path=START_OPTION, pos_x=0, pos_y=0)
                    case pygame.K_DOWN:
                        if start_menu_mode is False:
                            if menu_mode is True:
                                menu_obj.display_image(img_path=EXIT_OPTION, pos_x=0, pos_y=0)
                            else:
                                player2_status = 1
                        else:
                            menu_obj.display_image(img_path=EXIT_AT_START_MENU, pos_x=0, pos_y=0)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1_status = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2_status = 0
                if event.key == pygame.K_RETURN:
                    handle_chosen_option()

        if menu_mode is False and start_menu_mode is False:
            for player_i in players:
                if pygame.Rect.colliderect(ball_obj.get_rect(), player_i.get_rect()):
                    ball_obj.collision()

            score = ball_obj.move()
            player_1.move(player1_status)
            player_2.move(player2_status)

            if score == -1:
                player1_score += 1
            elif score == 1:
                player2_score += 1

            if score:
                clear_screen()
                text.text_to_screen(Constants.SCREEN.value, f"{player2_score}", Constants.WIDTH.value - 60, 0)
                text.text_to_screen(Constants.SCREEN.value, f"{player1_score}", 20, 0)
                ball_obj.restart()
                check_end_game(player1_score, player2_score)

            if menu_mode is False:
                ball_obj.draw()
                player_1.draw()
                player_2.draw()

        pygame.display.update()

        Constants.CLOCK.value.tick(Constants.FPS.value)


if __name__ == '__main__':
    Audio.play_music()
    display_start_menu()
    main()
