#word_generator.py
import random

# List of words to use in sentences
nouns = ["dog", "cat", "bird", "fish", "computer", "book", "building", "house", "car", "tree", "flower", "mountain", "river", "ocean", "beach", "city", "country", "planet", "universe", "galaxy", "star", "moon", "sun", "light", "darkness", "life", "death", "love", "hate", "friend", "enemy", "teacher", "student", "parent", "child", "sibling", "cousin", "aunt", "uncle", "grandparent", "grandchild", "niece", "nephew", "doctor", "nurse", "police officer", "firefighter", "soldier", "sailor", "pirate", "king", "queen", "prince", "princess", "president", "dictator", "captain", "chef", "farmer", "artist", "musician", "singer", "actor", "dancer", "writer", "poet", "scientist", "inventor", "astronaut", "alien", "robot", "monster", "ghost", "zombie", "vampire", "witch", "wizard", "dwarf", "elf", "orc", "goblin", "fairy", "mermaid", "merman", "dragon", "dinosaur", "unicorn", "centaur", "phoenix", "griffin", "pegasus", "hydra", "minotaur", "sphinx", "chimera", "hippogriff", "wyvern", "basilisk", "kraken", "giant", "troll", "ogre", "leprechaun", "gargoyle", "werewolf", "yeti", "sasquatch", "mothman", "chupacabra", "jackalope", "thunderbird", "mothman", "jersey devil", "banshee", "krampus"]
verbs = ["runs", "jumps", "eats", "sleeps", "reads", "drives", "talks", "walks", "flies", "swims", "plays", "works", "sings", "dances", "climbs", "hikes", "bikes", "rides", "draws", "paints", "writes", "types", "codes", "programs", "builds", "makes", "creates", "destroys", "fights", "battles", "attacks", "defends", "hunts", "hides", "seeks", "finds", "loses", "wins", "loses", "cries", "laughs", "smiles", "frowns", "screams", "yells", "whispers", "talks", "speaks", "listens", "hears", "sees", "looks", "watches", "stares", "touches", "feels", "tastes", "smells", "kicks", "punches", "hits", "stabs", "shoots", "kills", "murders", "saves", "helps", "hurts", "harms", "heals", "fixes", "repairs", "builds", "creates", "destroys", "fights", "battles", "attacks", "defends", "hunts", "hides", "seeks", "finds", "loses", "wins", "loses", "cries", "laughs", "smiles", "frowns", "screams", "yells", "whispers", "talks", "speaks", "listens", "hears", "sees", "looks", "watches", "stares", "touches", "feels", "tastes", "smells", "kicks", "punches", "hits", "stabs", "shoots", "kills", "murders", "saves", "helps", "hurts", "harms", "heals", "fixes", "repairs", "builds", "creates", "destroys", "fights", "battles", "attacks", "defends", "hunts", "hides", "seeks", "finds", "loses", "wins", "loses", "cries", "laughs", "smiles", "frowns", "screams", "yells", "whispers", "talks", "speaks", "listens", "hears", "sees"]
adjectives = ["happy", "sad", "angry", "funny", "silly", "serious", "tall", "short", "big", "small", "fast", "slow", "loud", "quiet", "hot", "cold", "warm", "cool", "dark", "light", "bright", "shiny", "dull", "sharp", "blunt", "hard", "soft", "rough", "smooth", "wet", "dry", "clean", "dirty", "messy", "neat", "tidy", "strong", "weak", "powerful", "weak", "powerful", "smart", "dumb", "stupid", "brave", "cowardly", "kind", "mean", "nice", "mean", "nice", "friendly", "unfriendly", "good", "bad", "evil", "honest", "dishonest", "loyal", "disloyal", "faithful", "unfaithful", "trustworthy", "untrustworthy", "beautiful", "ugly", "pretty", "handsome", "attractive", "repulsive", "repugnant", "disgusting", "delicious", "tasty", "yummy", "gross", "disgusting", "delicious", "tasty", "yummy", "gross", "healthy", "unhealthy", "sick", "ill", "diseased", "infected", "contagious", "deadly", "fatal", "safe", "dangerous", "risky", "harmless", "harmful", "helpful", "useful", "useless", "worthless", "valuable", "precious", "priceless", "cheap", "expensive", "rich", "poor", "wealthy", "broke", "boring", "interesting", "exciting", "fun", "bored", "interested", "excited", "funny", "silly", "serious", "tall", "short", "big", "small", "fast", "slow", "loud", "quiet", "hot", "cold", "warm", "cool", "dark", "light", "bright", "shiny", "dull", "sharp", "blunt", "hard", "soft", "rough", "smooth", "wet", "dry", "clean", "dirty", "messy", "neat", "tidy", "strong", "weak", "powerful", "weak", "powerful", "smart"]
adverbs = ["quickly", "slowly", "easily", "hardly", "happily", "sadly", "angrily", "loudly", "quietly", "suddenly", "finally", "secretly", "safely", "quickly", "slowly"]
articles = ["the", "a", "an"]
pronouns = ["he", "she", "it", "they", "we", "you", "I"]

# Function to generate a random sentence
def generate_sentence():
    sentence = []
    sentence.append(pronouns[random.randint(0, len(pronouns) - 1)])
    sentence.append(verbs[random.randint(0, len(verbs) - 1)])
    sentence.append(articles[random.randint(0, len(articles) - 1)])
    sentence.append(adjectives[random.randint(0, len(adjectives) - 1)])
    sentence.append(nouns[random.randint(0, len(nouns) - 1)])
    sentence.append(adverbs[random.randint(0, len(adverbs) - 1)])
    return " ".join(sentence)


# Test the function by generating 5 random sentences
for i in range(5):
    print(f"Sentence {i}: {generate_sentence()}")
