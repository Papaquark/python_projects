import time
import random
import math
import pandas as pd
from tabulate import tabulate
from faker import Faker
from printer import tprint
from printer import aprint
from golfer import Golfer
from course import *
from hole import *
from country import Country



#region ascii_art
world_map = "               ,_   .  ._. _.  .\n           , _-\','|~\~      ~/      ;-'_   _-'     ,;_;_,    ~~-\n  /~~-\_/-'~'--' \~~| ',    ,'      /  / ~|-_\_/~/~      ~~--~~~~'--_\n  /              ,/'-/~ '\ ,' _  , '|,'|~                   ._/-, /~\n  ~/-'~\_,       '-,| '|. '   ~  ,\ /'~                /    /_  /~\n.-~      '|        '',\~|\       _\~     ,_  ,               /|\n          '\        /'~          |_/~\\,-,~  \ \"         ,_,/ |\n           |       /            ._-~'\_ _~|              \ ) /\n            \   __-\           '/      ~ |\  \_          /  ~\n  .,         '\ |,  ~-_      - |          \\_' ~|  /\  \~ ,\n               ~-_'  _;       '\           '-,   \,' /\/  |\n                 '\_,~'\_       \_ _,       /'    '  |, /|'\n                   /     \_       ~ |      /         \  ~'; -,_.\n                   |       ~\        |    |  ,        '-_, ,; ~ ~\ \n                    \,      /        \    / /|            ,-, ,   -,\n                     |    ,/          |  |' |/          ,-   ~ \   '.\n                    ,|   ,/           \ ,/              \       |\n                    /    |             ~                 -~~-, /   _\n                    |  ,-'                                    ~    /\n                    / ,'                                      ~\n                    ',|  ~\n                      ~'"
#endregion

#Countries
countries = []
countries.append(Country("Norway","no-NO", "NOR"))
countries.append(Country("Sweden","sv-SE", "SWE"))
countries.append(Country("Finland","fi-FI", "FIN"))
countries.append(Country("Denmark","dk-DK", "DAN"))
countries.append(Country("France","fr-FR", "FRA"))
countries.append(Country("Spain","es-ES", "ESP"))
countries.append(Country("Germany","de-DE", "GER"))
countries.append(Country("Italy","it-IT", "IT"))
countries.append(Country("United Kingdom","en-UK", "UK"))
countries.append(Country("Australia","en-AU", "AUS"))
countries.append(Country("USA","en-US", "USA"))
countries.append(Country("India","en-IN", "IND"))
countries.append(Country("Canada","en-CA", "CAN"))
countries.append(Country("Mexico","es-MX", "MEX"))


#region = ["uno-NO","sv_SE","fi_FI","dk_DK","fr-FR","es-ES","de_DE","it_IT","en_UK","en-AU","en_US","en-IN","en-CA","es-MX"]



#print(world_map)
aprint("assets/beach.ascii")

i=1
for country in countries:
    print("{}.\t {}".format(i, country.name))
    i+=1

#print("\n\n---WHERE DO YOU WANT TO PLAY?---\n\n 1. Norway\n 2. Sweden\n 3. Finland\n 4. Denmark\n 5. France\n 6. Spain\n 7. Germany\n 8. Italy\n 9. Great Britan\n 10. Australia\n 11. USA\n 12. India\n 13. Canada\n 14. Mexico\n")

selection = 0

while selection < 1 or selection > len(countries):
    selection = int(input(": "))

locale = countries[selection-1].region

print(locale)
fake = Faker(locale)

#calculate power affected by wind
def sweetspot(power, wind):
        return (power+math.floor(power/100*wind))
        
  
skill = []
#region skill_definitions
skill.append([0,0,0,2,0,-1,0,0,1,1,2,0,0,-1,0,-1,0,1])
skill.append([0,-1,0,1,0,0,1,0,1,0,2,0,0,-1,1,-1,0,-1])
skill.append([0,1,0,0,0,-1,1,0,-1,0,2,2,0,-1,0,-1,0,-1])
skill.append([-1,1,0,2,0,0,0,0,0,0,2,-1,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,0,0,2,0,0,0,0,0,0,0])
skill.append([0,-1,0,0,0,0,0,0,1,1,2,0,-1,0,0,0,0,1])
skill.append([0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,0,0,2,0,-1,0,0,1,0,0,-1,0,0,0,0,0,-1])

skill.append([0,0,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,0,0,0,1,0,2,0,0,0,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,1,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,0,0,0,1,0,-1,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,-1,0,2,0,-1,0,1,1,0,2,-2,0,-1,0,-1,0,-1])

skill.append([0,-1,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-2,0,-1])
skill.append([-1,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,-2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,-1,0])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-2,0,-1,0,-2,0,-2])

skill.append([0,0,0,2,0,-1,0,0,1,1,2,0,0,-1,0,-1,0,1])
skill.append([0,-1,0,1,0,0,1,0,1,0,2,0,0,-1,1,-1,0,-1])
skill.append([0,1,0,0,0,-1,1,0,-1,0,2,2,0,-1,0,-1,0,-1])
skill.append([-1,1,0,2,0,0,0,0,0,0,2,-1,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,0,0,2,0,0,0,0,0,0,0])
skill.append([0,-1,0,0,0,0,0,0,1,1,2,0,-1,0,0,0,0,1])
skill.append([0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,0,0,2,0,-1,0,0,1,0,0,-1,0,0,0,0,0,-1])

skill.append([0,0,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,0,0,0,1,0,2,0,0,0,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,1,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,0,0,0,1,0,-1,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,-1,0,2,0,-1,0,1,1,0,2,-2,0,-1,0,-1,0,-1])

skill.append([0,-1,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-2,0,-1])
skill.append([-1,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,-2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,-1,0])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-2,0,-1,0,-2,0,-2])

skill.append([0,0,0,2,0,-1,0,0,1,1,2,0,0,-1,0,-1,0,1])
skill.append([0,-1,0,1,0,0,1,0,1,0,2,0,0,-1,1,-1,0,-1])
skill.append([0,1,0,0,0,-1,1,0,-1,0,2,2,0,-1,0,-1,0,-1])
skill.append([-1,1,0,2,0,0,0,0,0,0,2,-1,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,0,0,2,0,0,0,0,0,0,0])
skill.append([0,-1,0,0,0,0,0,0,1,1,2,0,-1,0,0,0,0,1])
skill.append([0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,0,0,2,0,-1,0,0,1,0,0,-1,0,0,0,0,0,-1])

skill.append([0,0,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,0,0,0,1,0,2,0,0,0,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,1,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,0,0,0,1,0,-1,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,-1,0,2,0,-1,0,1,1,0,2,-2,0,-1,0,-1,0,-1])

skill.append([0,-1,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-2,0,-1])
skill.append([-1,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,-2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,-1,0])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-2,0,-1,0,-2,0,-2])

skill.append([0,0,0,2,0,-1,0,0,1,1,2,0,0,-1,0,-1,0,1])
skill.append([0,-1,0,1,0,0,1,0,1,0,2,0,0,-1,1,-1,0,-1])
skill.append([0,1,0,0,0,-1,1,0,-1,0,2,2,0,-1,0,-1,0,-1])
skill.append([-1,1,0,2,0,0,0,0,0,0,2,-1,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,0,0,2,0,0,0,0,0,0,0])
skill.append([0,-1,0,0,0,0,0,0,1,1,2,0,-1,0,0,0,0,1])
skill.append([0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,0,0,2,0,-1,0,0,1,0,0,-1,0,0,0,0,0,-1])

skill.append([0,0,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,0,0,0,1,0,2,0,0,0,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,1,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,0,0,0,1,0,-1,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,-1,0,2,0,-1,0,1,1,0,2,-2,0,-1,0,-1,0,-1])

skill.append([0,-1,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-2,0,-1])
skill.append([-1,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,-2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,-1,0])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-2,0,-1,0,-2,0,-2])

skill.append([0,0,0,2,0,-1,0,0,1,1,2,0,0,-1,0,-1,0,1])
skill.append([0,-1,0,1,0,0,1,0,1,0,2,0,0,-1,1,-1,0,-1])
skill.append([0,1,0,0,0,-1,1,0,-1,0,2,2,0,-1,0,-1,0,-1])
skill.append([-1,1,0,2,0,0,0,0,0,0,2,-1,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,0,0,2,0,0,0,0,0,0,0])
skill.append([0,-1,0,0,0,0,0,0,1,1,2,0,-1,0,0,0,0,1])
skill.append([0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,0,0,2,0,-1,0,0,1,0,0,-1,0,0,0,0,0,-1])

skill.append([0,0,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-1,0,-1])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,0,0,0,1,0,2,0,0,0,0,-1,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,1,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,0,0,0,1,0,-1,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-1,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-1,-1,0])
skill.append([0,-1,0,2,0,-1,0,1,1,0,2,-2,0,-1,0,-1,0,-1])

skill.append([0,-1,0,2,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,-1,0,2,0,0,-1,0,-2,0,-1])
skill.append([-1,-1,0,2,0,-1,0,0,1,0,2,-1,0,-1,0,-2,0,-1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,0,0,1,0,2,0,-1,-1,0,0,0,1])
skill.append([0,-1,0,0,0,-1,0,0,1,0,-2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,0,0,-1,1,0,1,0,2,0,0,-1,0,-2,0,0])
skill.append([0,-1,0,1,0,-1,1,0,1,0,2,0,0,-1,0,-2,-1,0])
skill.append([0,-1,0,2,0,-1,0,0,1,0,2,-2,0,-1,0,-2,0,-2])
#endregion

def ai_score(skill):
        return skill[random.randint(0,17)]


#Tournament Leaderboard.
golfers = []

_rank = []
_names = []
_nationality = []
_score = []
_progress = []

for i in range(20):
    golfers.append(Golfer(fake.name().upper(), fake.current_country_code(), 0, skill[random.randint((selection-1)*9,((selection-1)*9)+9)]))
    _rank.append(0)
    _names.append(golfers[i].name)
    _nationality.append(golfers[i].nationality)
    _score.append(golfers[i].score)
    _progress.append("^")

df = pd.DataFrame({'Rank' : _rank,
                    'Name': _names,
                   'Nationality':  _nationality,
                    'Score' : _score,
                    'Progress' : _progress })




# appending
# df.loc[3] = [golfers[0].name,golfers[0].nationality, golfers[0].score]

def ai_play_holes(numberofholes, data):
    for x in range(numberofholes):
        for index, element in enumerate(golfers):
            new_score = ai_score(element.skillprofile) 
            
            if new_score < 0:  
                data.at[index,'Progress'] = '^'
            elif new_score == 0:
                data.at[index,'Progress'] = ' '
            else:   
                data.at[index,'Progress'] = 'v'
                
            element.score += new_score 
            
            data.at[index,'Score'] = element.score 

            

    # sorting
    df = data.sort_values(['Score', 'Name'], ascending=[1, 0])
    df['Rank'] = df['Score'].rank(axis=0, method='min', ascending=True)
    return df



    
df = ai_play_holes(1, df)

#print(df.loc[2])
df['Rank'] = df['Score'].rank(axis=0, method='min', ascending=True)

#print(df)

def get_club(percentage):
    if percentage > 90:
        if shot == 1:
            return "drive"
        else:
            return "spoon"
    elif percentage > 80:
        return "spoon"
    elif percentage > 70:
        return "3 iron"
    elif percentage > 60:
        return "5 iron"
    elif percentage > 50:
        return "7 iron"
    elif percentage > 40:
        return "9 iron"
    elif percentage > 30:
        return "pitch"
    elif percentage > 20:
        return "wedge"
    elif percentage > 9:
        return "flop"
    elif percentage > 5:
        return "chip"
    elif percentage > 1:
        return "putt"
    elif percentage > 0:
        return "tap in"

def get_hole_result_text(shot, par):
    hole_result = (shot-1) - par
    
    if hole_result == -3:
        if (shot-1) == 1:
            bird = "a HOLE IN ONE"
        else:
            bird = "an albatross"
        progress = "rockets to"
    elif hole_result == -2:
        if (shot-1) == 1:
            bird = "a HOLE IN ONE"
        else:
            bird = "an eagle"
        progress = "dropped to"
    elif hole_result == -1:
        bird = "a birdie"
        progress = "went to"
    elif hole_result == 0:
        bird = "a par"
        progress = "stayed at"
    elif hole_result == 1:
        bird = "a bogey" 
        progress = "went to"
    elif hole_result == 2:
        bird = "a double bogey"  
        progress = "went to a dissapointing"
    elif hole_result == 3:
        bird = "a triple bogey"
        progress = "went to a devastating"        
    elif hole_result > 3:
        bird = shot-1

    return bird

def get_hole_progress_text(shot, par):
    hole_result = (shot-1) - par
    
    if hole_result == -3:
        progress = "rockets to"
    elif hole_result == -2:
        progress = "dropped to"
    elif hole_result == -1:
        progress = "went to"
    elif hole_result == 0:
        progress = "stayed at"
    elif hole_result == 1:
        progress = "went to"
    elif hole_result == 2: 
        progress = "went to a dissapointing"
    elif hole_result == 3:
        progress = "went to a devastating"        
    elif hole_result > 3:
        progress = "makes a disastrous" 

    return progress

#Welcome screen
#print("\n"+logo)
aprint("assets/logo.ascii")
aprint("assets/golfer.ascii")
#print("\n"+image)
 
print("***PITCH BLACK GOLF version 1.6 (c) PAPA QUARK  -  MAKING DEEP STUFF SINCE 1979***\n\n")
#print(tabulate(df, headers = 'keys', tablefmt='psql', showindex = False))


player = input("Please register your name: ").upper()


    


#generate a tournament
part = []
part.append("OPEN")
part.append("MASTERS")
part.append("INVITATIONAL")
part.append("TOURNAMENT")
part.append("CHALLENGE")
part.append("MIXER")
part.append("BRAWL")
part.append("BATAILLE")
part.append("FEST")
part.append("SHOUTOUT")
part.append("GAMES")

tournament = "{} {}".format(fake.company().upper(), part[random.randint(0,len(part)-1)])

tprint("\n\n\tWELCOME TO THE ANNUAL\n",0.1)

#define course and holes

course = Course(fake)
holes = []

holes.append(Hole(1, 5, 450+random.randint(0,80)))
holes.append(Hole(2, 4, 380+random.randint(0,60)))
holes.append(Hole(3, 3, 170+random.randint(0,40)))
holes.append(Hole(4, 4, 401+random.randint(0,60)))
holes.append(Hole(5, 5, 501+random.randint(0,80)))
holes.append(Hole(6, 3, 111+random.randint(0,40)))
holes.append(Hole(7, 3, 122+random.randint(0,40)))
holes.append(Hole(8, 5, 500+random.randint(0,80)))
holes.append(Hole(9, 3, 178+random.randint(0,40)))
holes.append(Hole(10, 5, 458+random.randint(0,80)))
holes.append(Hole(11, 4, 408+random.randint(0,60)))
holes.append(Hole(12, 3, 160+random.randint(0,40)))
holes.append(Hole(13, 4, 411+random.randint(0,60)))
holes.append(Hole(14, 5, 511+random.randint(0,80)))
holes.append(Hole(15, 3, 121+random.randint(0,40)))
holes.append(Hole(16, 3, 129+random.randint(0,40)))
holes.append(Hole(17, 5, 510+random.randint(0,80)))
holes.append(Hole(18, 3, 178+random.randint(0,40)))


#Init commentary   
commentary = []

commentary.append("Lovley weather here in {}. The sky is {} and we are ready for some more brilliant golf.".format(fake.current_country(),fake.color_name()) )
commentary.append("{} actually made a hole in one at this course last year. The prize was a trip to {}. ".format(df.at[random.randint(0,9), 'Name'],fake.city()) )
commentary.append("{} said '{}' in an interview earlier. I dont know what that means but it seems to be working well today.".format(df.at[2, 'Name'],fake.sentence(nb_words=7)) )
commentary.append("Before joining the pro tour {} was a self employed {} for {} years. ".format(df.at[random.randint(0,9), 'Name'],fake.job(), random.randint(2,11)) )
commentary.append("A word from our sponsor {}. Your nr 1 stop for {}.".format(fake.company() ,fake.catch_phrase()))
commentary.append("If you are looking for {}. {} has got you covered. Call {} today!".format(fake.catch_phrase(),fake.company(), fake.phone_number()))
commentary.append("{} has generously donated a brand new car to the winner of todays tournament. ".format(fake.company()))
commentary.append("We are  looking for the owner of a car with the license plate number {}. Parking on the forgreen is not allowed.".format(fake.license_plate()))
commentary.append("The trees behind the third green is one of only four known habitats of the {} {} {}.".format(fake.color_name(),fake.first_name_female(),random.choice(['bird', 'beetle', 'lizard', 'serpant', 'ant'])))
commentary.append("{} has the worlds eldest active member. {} is {} years old and still going strong.".format(course.name,fake.name_female(),random.randint(86,119)))
commentary.append("{} was a well known {} and thaught random children the value of being able to hit a controlled draw.".format(df.at[random.randint(0,9), 'Name'],fake.job()) )
commentary.append("{} was born in the outskirts of {} in {}. Back then golf was immensly popular and everybody played.".format(df.at[random.randint(0,9), 'Name'],fake.city(),random.randint(1975,2004)) )
commentary.append("Did you know that {} is the home of {} baby kangaroos that were given as a token of friendship from Australia in {}.".format(fake.current_country(),random.randint(2,600),random.randint(2020,2022)) )
commentary.append("A popular {} festival is held annually in the nearby city of {}.".format(random.choice(['cheeze', 'beard', 'knitting', 'fire', 'golf']),fake.city()) )
commentary.append("{} became a legend last season when she played {} rounds without drinking any water. A stunt that led to {} weeks in the hospital.".format(df.at[random.randint(0,9), 'Name'],random.randint(6,12), random.randint(2,5)) )
commentary.append("Do you need {}? E-mail {} and ask for a quote.".format(fake.catch_phrase(),fake.company_email()))
commentary.append("In {} {} was bashed by a huge storm that tore away {}% of all the trees at the {}.".format(random.randint(1955,2000),course.city,random.randint(1,99),course.name) )
commentary.append("The sand in the bunkers at {} was actually shipped here all the way from {}. The quality and color was almost identical to the local sand so no one could tell the difference.".format(course.name,fake.country()) )
commentary.append("{} is famous for having the deepest holes in the world; naturally they also need the tallest flags just to make them normal height. ".format(course.name))

random.shuffle(commentary)

# init game parameters

curr_hole = 1
max_holes = 18

score = 0
shot = 1
left = holes[curr_hole-1].length # How far is it left to the hole.

prefix = "+"

# appending
player_index = df.index.max() + 1
df.loc[player_index] = [1, player + " (YOU)",'SE', score, "^"]



#Game loop
while curr_hole != max_holes+1:

    # update
    df.at[df.index.max(),'Score'] = score 
    
    df = ai_play_holes(1, df)
    tprint("\n-== "+tournament+" AT THE "+ course.name.upper()+" - "+fake.current_country().upper()+ " ==-\n",0.04)
    print(tabulate(df, headers = 'keys', tablefmt='psql', showindex = False))

    wind = random.randint(-15,15)
    time.sleep(3)

    print("\n")
    print(get_course_name(course))
    print(get_hole_description(holes[curr_hole-1]))
    print("\n")
    
    print("\t[{}] {} {} {}\n".format(str(int(df.at[player_index, 'Rank'])),player, str(prefix), score),
    "\tSHOT {}\n".format(shot),
    "\t{} M TO PIN\n\n".format(left),
    "\tWIND {} m/s\n\n".format(wind) 
     ) 

    in_hole = False
    
    while in_hole != True:
        power = input("\tENTER POWER (0-100): ")
        
        if power.isdigit() == True: #Input validation 100% is default.
            power = int(power)
        else:
            power = 100
        
        if power > 100: 
            power = 100
            
        club = get_club(power)
        power = sweetspot(power, wind)
        
        distance = round((power*250)/100)
        left = abs(left - distance)
        
        shot += 1
        
        print("\t"+str(power)+"%\n")
        
        
        if left <= 2:
            tprint("\tShot " + str(shot-1) + "......it...goes..in..the..hole!",0.1)
            in_hole = True
        elif left < 20:
            tprint("\tShot " + str(shot-1) + " great "+ str(club) +"...." + str(distance)+ "M\n" +"\t*lands on the green*\n" + "\tDistance left: " + str(left) + "M\n",0.1)
            chance = math.floor(100-((left/2)*10))
            dice = random.randint(0,100)
            invisible_chance_boost = 10

            print("\tPutting for {}".format(get_hole_result_text(shot+1, holes[curr_hole-1].par)) )
            putt = str(input("\t{}% chance. Go for the hole?(y/n): ".format(chance)))
            if putt == "y":
                if dice <= (chance+invisible_chance_boost):
                    tprint("\tThe putt goes...in the hole!",0.1)
                    in_hole = True
                    shot +=1
                else:
                    tprint("\tThe putt goes...way past the hole and you make a 3 putt!",0.1)
                    in_hole = True
                    shot +=3 
            else:
                tprint("\tYou putt it close and walk of with a safe 2 putt.",0.1)
                in_hole = True
                shot +=2                
        else:
            tprint("\tShot " + str(shot-1) + " nice "+ str(club) +"...." + str(distance) + "M\n" + "\tDistance left: " + str(left) + "M\n",0.1)
            wind = wind + random.randint(-5,5)
            print("\tWIND {} m/s\n\n".format(wind))
        
        

    
    #it is in the hole 
    
    hole_result = (shot-1)- holes[curr_hole-1].par
    
    score += hole_result
    
       
    if score >0:
        prefix = "+"
    elif score == 0:
        prefix = "+-"
    else:
        prefix = " "
    
    
    print("\n\n.........................................................................................\n")
    print("\t"+player + " made " + get_hole_result_text(shot, holes[curr_hole-1].par) + " on hole " + str(curr_hole) + " and "+ get_hole_progress_text(shot, holes[curr_hole-1].par) +" "+ str(prefix) + str(score)+ "\n") #feedback
    print(".........................................................................................\n\n\n")

    time.sleep(0.5) 
 
    print("## "+commentary[curr_hole-1]+" ##")
    
    time.sleep(2.2)
    
    curr_hole += 1
    if curr_hole <= max_holes:                                #next hole
        left = holes[curr_hole-1].length                      #next hole distance left
        shot = 1                                              #reset shot


df.at[df.index.max(),'Score'] = score 
df = ai_play_holes(0, df) #Just sorting
print(tournament)
print(tabulate(df, headers = 'keys', tablefmt='psql', showindex = False))

time.sleep(0.2)

print(player+" rank: "+str(int(df.at[player_index, 'Rank'])))
if df.at[player_index, 'Rank'] == 1.0:
        aprint("assets/podium_1.ascii")

if df.at[player_index, 'Rank'] == 2.0:
        aprint("assets/podium_2.ascii")
    
if df.at[player_index, 'Rank'] == 3.0:
        aprint("assets/podium_3.ascii")

if df.at[player_index, 'Rank'] > 3.0:
        aprint("assets/podium_4.ascii")


tprint("\n\nGAME OVER THANK YOU FOR PLAYING",0.4)
input(":")
