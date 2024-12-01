import random

class Hole:
    def __init__(self, nr, par, length):
        self.nr = nr
        self.par = par
        self.length = length

def get_hole_description(hole):
    hole_header = "\tHOLE {}    PAR {}     {} M".format(hole.nr,hole.par,hole.length)
    hole_description = "\tA {} {} hole.".format(random.choice(["stunning",
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
    hole_description_additional = "{}".format(random.choice(["The left side is lined with pinetrees.",
                                                               "There is an old church in the far distance.",
                                                               "The hole is surrounded by an azure blue lake.",
                                                               "Situated on a hill you can see very far.",
                                                               "There is deep forest surrounding the hole.",
                                                               "The rigth side is lined with posh vacation homes.",
                                                               "Two huge trees make up a great gate for aming.",
                                                               "There is a lake with lillypads behind the green",
                                                               "A small creek runs across the fairway.",
                                                               "You can see the clubhouse from here."]))
    hole_description = hole_header + "\n" + hole_description +" "+ hole_description_additional

    return hole_description
