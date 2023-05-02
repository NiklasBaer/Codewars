def beeramid(bonus, preis):
    Bier = bonus // preis
    level = 0
    while Bier >= (level+1)**2:
        level += 1
        Bier -= level**2
    return level

