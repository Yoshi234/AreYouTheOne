import unittest
from MatchingAlgorithm1 import Character, CharacterCollection, generate_match_collection

class TestCharacter(unittest.TestCase):
    def test_init(self):
        character1 = Character('John','man')
        self.assertEqual(character1.name,'John')
        self.assertEqual(character1.gender, 'man')
    
class TestCharacterCollection(unittest.TestCase):
    def setUp(self):
        self.character1 = Character('John','man')
        self.character1.set_kindness(30)
        self.character1.set_physical_attractiveness(34)
        self.character1.set_intelligence(36)
        self.character1.set_psychological_stability(25)
        self.character1.set_body_count(35)
        self.character1.set_stable_relationships(20)
        self.character1.set_wealth(35)
        self.character1.set_social_clout(25)
        self.character1.set_loyalty(30)

        self.character2 = Character('Alex','man')
        self.character2.set_kindness(40)
        self.character2.set_physical_attractiveness(40)
        self.character2.set_intelligence(40)
        self.character2.set_psychological_stability(30)
        self.character2.set_body_count(45)
        self.character2.set_stable_relationships(39)
        self.character2.set_wealth(5)
        self.character2.set_social_clout(25)
        self.character2.set_loyalty(40)

        self.character3 = Character('Josh','man')
        self.character3.set_kindness(30)
        self.character3.set_physical_attractiveness(30)
        self.character3.set_intelligence(40)
        self.character3.set_psychological_stability(30)
        self.character3.set_body_count(40)
        self.character3.set_stable_relationships(39)
        self.character3.set_wealth(5)
        self.character3.set_social_clout(25) 
        self.character1.set_loyalty(40)      

# character values: kindness, physical_attractiveness, intelligence, psychological_stability, body_count, stable_relationships, wealth, social_clout
        self.w3 = Character('Kitagawa','woman')
        self.w3.set_kindness(45)
        self.w3.set_physical_attractiveness(50)
        self.w3.set_intelligence(35)
        self.w3.set_psychological_stability(30)
        self.w3.set_body_count(50)
        self.w3.set_stable_relationships(25)
        self.w3.set_wealth(20)
        self.w3.set_social_clout(40)
        self.w3.set_loyalty(45)

        self.w1 = Character('Alexis','woman')
        self.w1.set_kindness(25)
        self.w1.set_physical_attractiveness(32.5)
        self.w1.set_intelligence(37)
        self.w1.set_psychological_stability(24)
        self.w1.set_body_count(36)
        self.w1.set_stable_relationships(20)
        self.w1.set_wealth(40)
        self.w1.set_social_clout(40)
        self.w1.set_loyalty(25)

        self.w2 = Character('Jen','woman')
        self.w2.set_kindness(30)
        self.w2.set_physical_attractiveness(30)
        self.w2.set_intelligence(30)
        self.w2.set_psychological_stability(30)
        self.w2.set_body_count(30)
        self.w2.set_stable_relationships(30)
        self.w2.set_wealth(30)
        self.w2.set_social_clout(40)
        self.w2.set_loyalty(30)
        
        self.Character_Collection1 = CharacterCollection()
        self.Character_Collection1.add_character(self.character1)
        self.Character_Collection1.add_character(self.character2)
        self.Character_Collection1.add_character(self.character3)

        self.Women_Collection1 = CharacterCollection()
        self.Women_Collection1.add_character(self.w1)
        self.Women_Collection1.add_character(self.w2)
        self.Women_Collection1.add_character(self.w3)

    def test_init(self):
        self.assertEqual(self.Character_Collection1.character_collection, {'John': self.character1, 'Alex': self.character2, 'Josh': self.character3})

    def test_getitem(self):
        self.assertEqual(self.Character_Collection1['John'],self.character1)

    def test_generate_match_collection(self):
        print(generate_match_collection(self.Character_Collection1, self.Women_Collection1))
        self.assertEqual(generate_match_collection(self.Character_Collection1, self.Women_Collection1), [(self.character1,self.w1),(self.character3,self.w2),(self.character2,self.w3)])


unittest.main()