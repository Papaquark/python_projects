import random

class Hole:
    def __init__(self, nr, par, length):
        self.nr = nr
        self.par = par
        self.length = length

def get_hole_description(hole):
    hole_header = "\n\tHOLE {}    PAR {}     {} M".format(hole.nr,hole.par,hole.length)
    hole_description = "\n\tA {} {} hole.".format(random.choice(["stunning",
                                                                 "breathtaking",
                                                                 "simple",
                                                                 "beautiful",
                                                                 "unique",
                                                                 "subtle",
                                                                 "agressive",
                                                                 "mediocre"]),
                                                 random.choice(["dogleg",
                                                                "signature",
                                                                "challenging",
                                                                "tricky",
                                                                "tretiorous",
                                                                "mysterious",
                                                                "ravine",
                                                                "abyss",
                                                                "beach",
                                                                "coastline",
                                                                "seaside"]))
    hole_description = hole_header + "\n" + hole_description

    return hole_description
