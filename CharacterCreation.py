import pygame
# cannot figure out how to implement the inputs correctly, so for now it will be just a series of default names

# need something to handle saving the inputs to a list of names that should be fed into the generate perfect matches function once and no more

# then ,it needs to return the perfect matches to a variable that's available to the game for the entire run of the loop

class Create_Character_Names_Page():
    def __init__(self, game): 
        # gets the game attributes
        self.game = game

        self.run_display = True
        # sets a user_text value (empty string initially)
        self.user_text = ''

        self.mid_W, self.mid_H = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        
        self.user_text_x, self.user_text_y = self.mid_W, self.mid_H + 30

        

        # just need the rect values for drawing text to the screen
        # "Create 8 Female Character Names"
        # "Create 8 Male Character Names"

        # parse the string of all the names. Create a limited box for the string text to exist in
        # and then just parse it once the text writing is finished to get the name strings

        # then implement the name strings into the generate matches function with random values
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


    def display_page(self):
        self.run_display = True

        while self.run_display:

            self.game.check_events()
            self.check_events_on_page()

            self.game.draw_text(self.user_text, 34, self.user_text_x, self.user_text_y)
            
            self.blit_screen()


    def check_events_on_page(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.user_text += event.unicode
            
        



        


