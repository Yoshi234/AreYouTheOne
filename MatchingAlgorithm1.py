# matches individuals by creating a set of characters with randomized default characteristics (10 characteristics)

# individuals are given an overall rank score, and matched with the corresponding individual who in the reverse ranked list for the opposite gender

import random

def generate_random_score():
    return random.randint(1,50)

class Character():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.kindness = generate_random_score()
        self.intelligence = generate_random_score()
        self.physical_attractiveness = generate_random_score() 
        # the higher the score, more mentally stable
        self.psychological_stability = generate_random_score()
        # the higher this score, the lower the body count
        self.body_count = generate_random_score()
        # stable relationship history, higher score means better relationship history
        self.stable_relationships = generate_random_score()
        self.wealth = generate_random_score()
        self.social_clout = generate_random_score()
        self.loyalty = generate_random_score()
    
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)

    # if desired, can set specific scores

    def set_loyalty(self, value):
        self.loyalty = value

    def set_kindness(self, value): 
        self.kindness = value

    def set_intelligence(self, value):
        self.intelligence = value

    def set_physical_attractiveness(self, value):
        self.physical_attractiveness = value

    def set_psychological_stability(self, value):
        self.psychological_stability = value

    def set_body_count(self, value):
        self.body_count = value

    def set_stable_relationships(self, value):
        self.stable_relationships = value

    def set_wealth(self, value):
        self.wealth = value

    def set_social_clout(self, value):
        self.social_clout = value

    def generate_overall_score(self, gender):
        if gender == "man":
            personality_score = 2*self.kindness + 4*self.intelligence + 5*self.psychological_stability
            external_score = 3*self.physical_attractiveness + 4*self.wealth + 4*self.social_clout
            relationship_history = 2*self.body_count + 2*self.stable_relationships + 4*self.loyalty

            return personality_score + external_score + relationship_history
        elif gender == "woman":
            personality_score = 3*self.kindness + 2*self.intelligence + 5*self.psychological_stability
            external_score = 4*self.physical_attractiveness + 1*self.wealth + 1*self.social_clout
            relationship_history = 3*self.body_count + 3*self.stable_relationships + 4*self.loyalty

            return personality_score + external_score + relationship_history
            

class CharacterCollection():
    def __init__(self):
        self.character_collection = dict()
    
    def __getitem__(self, name):
        return self.character_collection[name]

    def add_character(self, character):
        self.character_collection[character.name] = character

    def remove_character(self, character):
        del self.character_collection[character]

    # sorts using the bubble sort algorithm
    def bubble_sort(self, ranks):
        n = len(ranks)
        for i in range(n):
            sorted_flag = True
            for j in range(n-1-i):
                # compare the value of their given scores
                if ranks[j][1] > ranks[j+1][1]:
                    sorted_flag = False
                    ranks[j], ranks[j+1] = ranks[j+1], ranks[j]
            if sorted_flag: return

     # each person is a character class object
    def generate_ranks(self, gender): 
        ranks = []
        # person is the index used for iteration
        for person in self.character_collection:
            x = (self.character_collection[person].name, self.character_collection[person].generate_overall_score(gender))
            ranks.append(x)
        
        self.bubble_sort(ranks)
        return ranks

def generate_match_collection(Men, Women):
    match_collection = []
    men_ranks = Men.generate_ranks('man')
    women_ranks = Women.generate_ranks('woman')

    # men_ranks and women_ranks are a list of tuples
    for person in range(len(men_ranks)):
        match_collection.append((Men[men_ranks[person][0]], Women[women_ranks[person][0]]))
    return match_collection

if __name__ == "__main__":

    M = [Character('John','man'), Character('Jack','man'), Character('Jeff','man'), Character('Alan','man'), Character('Max','man'), Character('Henry','man'), Character('Patrick','man'), Character('Ryan','man')]

    W = [Character('Amy','woman'), Character('Audrey','woman'), Character('Amanda','woman'), Character('Jennifer','woman'), Character('Sophie','woman'), Character('Melissa','woman'), Character('Danielle','woman'), Character('katherine','woman')]

    Men = CharacterCollection()
    Women = CharacterCollection()

    for i in M:
        Men.add_character(i)
    for j in W:
        Women.add_character(j)

    match_collection = generate_match_collection(Men, Women)
    print(match_collection)

