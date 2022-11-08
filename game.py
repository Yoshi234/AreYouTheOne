# implements the main game loop:

import sys
import pygame
from menu import Menu
# from CharacterCreation import Create_Character_Names_Page # not yet implemented
from MatchingAlgorithm1 import CharacterCollection, Character, generate_match_collection
from MatchSelection import Selection_Screen
from OutputScreen import OutputScreen



class Game():
    def __init__(self):
        # initialize pygame
        pygame.init()
        
        # initialize all of the attributes of the Game class ...
        # initially, the game is running, but the game is not being played
        self.running, self.playing = True, False

        # just set the boolean values to tell you whether these keys are actually being pressed or not
        self.BACK_KEY, self.ENTER_KEY = False, False
        
        # for the 4 arrow inputs in the bottom right corner
        self.RIGHT_KEY, self.LEFT_KEY, self.UP_KEY, self.DOWN_KEY,  = False, False, False, False

        # generate the dimensions of the window/screen
        self.DISPLAY_W, self.DISPLAY_H = 1000, 500

        # initialize the displayed representation with width = 2000px, height = 1400px
        # right now, the surface object is the display itself
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))

        # initialize the window with width = 2000px, height = 1400px
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))

        # initialize the font, returns reference to the default font object
        self.font_name = pygame.font.get_default_font() 

        # load and create an image rectangle for the background image, it must be scaled though
        self.DEFAULT_IMAGE_SIZE = (1000, 625)
        self.ORANGE  = (195, 88, 23)
        self.BG_IMG = pygame.image.load("img.jpg")
        self.BG_IMG = pygame.transform.scale(self.BG_IMG, self.DEFAULT_IMAGE_SIZE)
        self.BG_Rect = self.BG_IMG.get_rect()

        # gives a game class object to a Menu Object
        self.main_menu = Menu(self)

        # need more time to properly implement this: for now, just a default match selection page
        # self.character_creation_screen = Create_Character_Names_Page(self)

        # a characteristic of the actual game itself
        self.round1 = 0

        self.perfect_matches = None
    
        self.matches_left = self.perfect_matches

        self.women = [Character('Amy','woman'), Character('Audrey','woman'), Character('Amanda','woman'), Character('Jennifer','woman'), Character('Sophie','woman'), Character('Melissa','woman'), Character('Danielle','woman'), Character('katherine','woman')]

        self.men = [Character('John','man'), Character('Jack','man'), Character('Jeff','man'), Character('Alan','man'), Character('Max','man'), Character('Henry','man'), Character('Patrick','man'), Character('Ryan','man')]

         # these are the matches that user selects
        self.user_matches = []

        self.temp_matches = None

        # creates a selection screen object
        self.selection_screen = Selection_Screen(self)

        self.output_screen = OutputScreen(self)


    def correct_matches(self):
        num_matches = 0
        for i in range(len(self.user_matches)):
            if self.user_matches[i] in self.perfect_matches:
                num_matches += 1
        return num_matches


    def generate_default_perfect_matches(self):
        M = [Character('John','man'), Character('Jack','man'), Character('Jeff','man'), Character('Alan','man'), Character('Max','man'), Character('Henry','man'), Character('Patrick','man'), Character('Ryan','man')]

        W = [Character('Amy','woman'), Character('Audrey','woman'), Character('Amanda','woman'), Character('Jennifer','woman'), Character('Sophie','woman'), Character('Melissa','woman'), Character('Danielle','woman'), Character('katherine','woman')]

        # these are NOT iteratbles
        Men = CharacterCollection()
        Women = CharacterCollection()

        for i in M:
            Men.add_character(i)
        for j in W:
            Women.add_character(j)
    
        self.perfect_matches = generate_match_collection(Men, Women)
        # after generating the perfect matches, set round1 = false so 
        self.matches_left = self.perfect_matches

        self.men = M
        self.women = W

        self.round1 += 1
        
    def reset_screen(self):
        self.display.fill(self.ORANGE)
        # blit the surface to the rect() to the screen
        self.display.blit(self.BG_IMG, self.BG_Rect)
        # update the display variable, and then blit the display surface object to the window
        self.window.blit(self.display, (0,0))

    def run_game(self):
        # blit function just puts one surface on top of another surface
        # TODO: Fix this to account for main menu functionality
        # the main game loop should contain the selection screen ... 
        while self.playing:
            self.check_events()

            self.reset_screen()
            
            # if it is the first round, step into the create character_names screen
            if self.round1 == 0:
                # self.character_creation_screen.display_page()
                # not the time to implement this currently: just using default names
                self.generate_default_perfect_matches()
            # this function needs to set self.game.round1 equal to false after the first round has finished.
            self.selection_screen.display_selection_screen()

            self.output_screen.display_output_screen()


            pygame.display.update()
            # reset the key inputs for the next cycle of the loop
            self.reset_keys()
    
    def check_events(self):
        # returns all pygame events for iteration
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # you need to set the variable for the game loop false to break the loop in "main"
                self.running, self.playing = False, False
        
            elif event.type == pygame.KEYDOWN:
                # change the boolean values when a given key is pressed during the loop
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True

                # up, down, left, right arrows
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True

                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True


    def reset_keys(self):
        self.ENTER_KEY, self.BACK_KEY = False, False
        self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False

    def draw_text(self, text, size, x, y, color=None):
        if color == None:
            color = self.ORANGE

        font = pygame.font.Font(self.font_name, size)

        # creates a rectangular image of the text
        text_surface = font.render(text, True, color)

        # a rect() has x, y, width, and height
        text_rect = text_surface.get_rect()

        # this will center the text where you want it
        text_rect.center = (x, y)

        self.display.blit(text_surface, text_rect)
    


# move to a different file

# this page will only be run when the round1 variable is True 

                




