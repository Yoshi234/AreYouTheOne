from MatchSelection import Selection_Screen

class OutputScreen(Selection_Screen):
    def __init__(self, game):
        self.game = game
        Selection_Screen.__init__(self, game)
    
        self.run_display = True

        self.mid_W, self.mid_H = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2

    def display_output_screen(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()

            self.game.display.fill(self.game.ORANGE)
            self.game.display.blit(self.game.BG_IMG, self.game.BG_Rect)

            self.game.draw_text(f"You selected {self.game.correct_matches()} matches correctly", 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2)

            self.blit_screen()

    def check_inputs(self):
        if self.game.ENTER_KEY == True:
            self.run_display = False
    



        