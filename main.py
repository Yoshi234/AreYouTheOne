# actually runs the game components in the proper order

# pseudo code

# g = Game()

# while running:
#       display main menu()
#       run_game()

from game import Game

g = Game()

# the running variable is imported from the Game class
while g.running:
    g.main_menu.display_menu()
    g.run_game()

