import random
persons = ['Champ,', 'Fact,', 'Everybody says,', 'Dang,', 'Check it:', 'Just saying...', 'Superstar,', 'Tiger,', 'Know this:', 'Self, ', 'News alert:' ,'Excuse me but', 'Experts agree:', 'Okay, listen up']
starts = [' the mere idea of you ', ' your soul ', ' your hair today ', ' everything you do ', ' your personal style ', ' every thought you have ', ' that sparkle in your eye ', ' your presence here ', ' your DNA ', ' that brain of yours ', ' your choice of attire ', 'whatever your secret is ']
descriptions = ['has serious game, ', 'rains magic, ', 'deserves the Nobel Prize, ', 'raises the roof, ', 'breeds miracles, ', 'shows mad skills, ', 'just shimmers, ', 'gets the party hopping, ', 'is the next big thing, ', 'roars like a lion, ', 'is a rainbow factory, ', 'makes birds sing, ', 'should be taught in school, ', 'is 100% legit, ' ]
endings = ['24/7.', 'and thats a fact.', 'so treat yourself.', 'thats just science. ', 'would I lie?', 'for reals.', 'mic drop.', 'you hidden gem.', 'now lets dance.', 'high five.', 'say it again!', 'according to CNN.', 'so get used to it.']

def msg():
    person = random.choice(persons)
    start = random.choice(starts)
    description = random.choice(descriptions)
    ending = random.choice(endings)
    x = (f"{person}{start}{description}{ending}")
    return x
