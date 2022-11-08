# Implements a main menu screen
import pygame

class Menu():
    def __init__(self, game):
        #contains a game class element
        self.game = game

        # need to generate a new surface rectangle which is the same size as the original screen
        self.mid_W, self.mid_H = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2

        # also need to generate a cursor object which is native to the menu
        self.cursor_rect = pygame.Rect(0, 0, 30, 30)

        # boolean which runs the Menu ...
        self.run_display = True

        self.state = "Start"

        # pixel amount to offset cursor value to the left
        self.x_offset = -138

        self.startx, self.starty = self.mid_W, self.mid_H + 50
        self.titlex, self.titley = self.mid_W, self.mid_H - 30

        self.cursor_rect.midtop = self.startx + self.x_offset, self.starty


    def draw_cursor(self):
        self.game.draw_text('*', 25, self.cursor_rect.x, self.cursor_rect.y)


    def blit_menu_to_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
        

    def display_menu(self):
        # run a while loop that keeps the page open while it is running

        # have a mechanism for making this true or adjusting this value
        self.run_display = True
        while self.run_display:
            # check the events which are occurring to decide whether or not to stay on the page
            self.game.check_events()

            self.check_inputs()

            self.game.display.fill(self.game.ORANGE)
            self.game.display.blit(self.game.BG_IMG, self.game.BG_Rect)
           
            self.game.draw_text("Are You The ONE??", 60, self.titlex, self.titley)
            self.game.draw_text("START GAME!", 40, self.startx, self.starty)

            self.draw_cursor()
            self.blit_menu_to_screen()
        # this will only continue on to play the game if the self.game.playing variable is True

    def check_inputs(self):
        # does not need to move the cursor, since it is only in one position
        if self.state == "Start":
            if self.game.ENTER_KEY == True:
                self.game.playing = True
            self.run_display = False
            

    # there is only going to be one option on my Menu Screen

