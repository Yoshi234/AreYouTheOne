# implements the class page which allows for match selection
import pygame

# i can have the truth booth selection screen inherit from the main selection screen
class Selection_Screen():
    def __init__(self, game):
        self.game = game

        self.run_display = True

        self.cursor_rect = pygame.Rect(0, 0, 30, 30)

        self.cursor_offset = -30

        self.left_W, self.mid_H = self.game.DISPLAY_W/9, self.game.DISPLAY_H/3

        self.temp_men = self.game.men
        self.temp_women = self.game.women

        self.states_at_locations = dict()
        # indexale list of the locations where the cursor can land
        self.locations = None # update after generating the actual dictionary

        self.cursor_location = (self.left_W, self.mid_H)
        self.cursor_rect.midtop = (self.cursor_location[0] + self.cursor_offset, self.cursor_location[1])
        # iterator/index to help with moving the cursor
        self.current_name = 0

        self.temp_pair = []

    def create_test_pairs(self, other_person):
        if len(self.temp_pair) == 2:
            self.temp_pair = []
        if len(self.temp_pair) < 2:
            self.temp_pair.append(other_person)
            if len(self.temp_pair) == 2:
                if self.temp_pair[0].gender == "woman":
                    self.temp_pair[0], self.temp_pair[1] = self.temp_pair[1], self.temp_pair[0]
                tuple(self.temp_pair)
                self.game.user_matches.append(self.temp_pair)
 
                # reset the temp_pair object attribute





    def index_adjustment(self):
        if self.current_name >= len(self.locations)-1:
            # once the cursor gets past the last location, reset the cursor position
            self.current_name = -1
            self.cursor_location = self.locations[self.current_name]

    def draw_cursor(self):
        self.game.draw_text('*', 25, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()


    def print_names(self):
        x_pos = 0
        for person in self.temp_men:
            self.game.draw_text(person.name, 18, (self.left_W + x_pos), (self.mid_H), self.game.ORANGE)
            # create a map of characters to their locations
            # the tuples are the keys which map to the character
            self.states_at_locations[(self.left_W + x_pos, self.mid_H)] = person
            x_pos += 110
        x_pos=0
        for person in self.temp_women:
            self.game.draw_text(person.name, 18, self.left_W+ x_pos, self.mid_H + 40, (self.game.ORANGE))

            self.states_at_locations[self.left_W + x_pos, self.mid_H + 40] = person
            x_pos += 110
        self.locations = [key for key in self.states_at_locations]
        self.cursor_lcation = self.locations[0]


    def display_selection_screen(self):
        self.run_display = True
        while self.run_display:
            # if men and women len(L) = 0, then run_display will be set to false
            self.game.check_events()
            # put into the check-inputs() function later
            
            self.check_inputs()
            # self.check_inputs()
            self.game.display.fill(self.game.ORANGE)
            self.game.display.blit(self.game.BG_IMG, self.game.BG_Rect)
            # self.game.draw_text(f"{self.locations}", 30, self.game.DISPLAY_W/4, self.game.DISPLAY_H/1.5)
            self.game.draw_text(f"Round: {self.game.round1}", 30, self.game.DISPLAY_W/2, self.game.DISPLAY_H/5)
            self.print_names()

            self.move_cursor()
            self.game.draw_text(f"{self.temp_pair}", 20, self.game.DISPLAY_W/4, self.game.DISPLAY_H/1.5)
            self.draw_cursor()

            self.blit_screen()

        
    def move_cursor(self):
        if self.game.RIGHT_KEY == True:

            self.index_adjustment()
            self.cursor_location = self.locations[self.current_name+1]
            self.cursor_rect.midtop = (self.cursor_location[0] + self.cursor_offset, self.cursor_location[1])
            self.current_name += 1
            

        # the states here will be the names of the characters.
        # when the state is equal to the first  
        
    def check_inputs(self):
        if self.game.ENTER_KEY == True:
            if len(self.temp_men) == 0 or len(self.temp_women) == 0:
                self.run_display = False
                self.temp_men = self.game.men
                self.temp_women = self.game.women
                return
            item_to_remove = self.states_at_locations[self.cursor_location]
            if item_to_remove.gender == "man":
                self.temp_men.remove(item_to_remove)
                self.create_test_pairs(item_to_remove)
            elif item_to_remove.gender == "woman":
                self.temp_women.remove(item_to_remove)
                self.create_test_pairs(item_to_remove)
        
            


            
            # need to store this, until the matching character is picked
            

            


