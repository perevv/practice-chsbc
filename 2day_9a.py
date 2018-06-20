import random

article = ["the", "a", "one", "some", "any"]
noun = ["boy", "girl", "dog", "town", "car"]
verb = ["drove", "jumped", "ran", "walked", "skipped"]
preposition = ["to", "from", "over", "under", "on"]

def random_int():
  return random.randint(0,4)

def random_sentence():
    return ("{} {} {} {} {} {}"
                .format(article[random_int()]
                        ,noun[random_int()]
                        ,verb[random_int()]
                        ,preposition[random_int()]
                        , article[random_int()]
                        ,noun[random_int()])).capitalize()

for sentence in list(map(lambda x: random_sentence(), range(0, 20))):
  print(sentence)
  
print("\n")

history = (". ").join(list(map(lambda x: random_sentence(), range(0, 20))))

print("{}.".format(history))
