from bs4 import BeautifulSoup
import re, requests
import urllib
import pandas

heroDict = {'Abaddon': 102,
 'Alchemist': 73,
 'Ancient Apparition': 68,
 'Anti-Mage': 1,
 'Arc Warden': 113,
 'Axe': 2,
 'Bane': 3,
 'Batrider': 65,
 'Beastmaster': 38,
 'Bloodseeker': 4,
 'Bounty Hunter': 62,
 'Brewmaster': 78,
 'Bristleback': 99,
 'Broodmother': 61,
 'Centaur Warrunner': 96,
 'Chaos Knight': 81,
 'Chen': 66,
 'Clinkz': 56,
 'Clockwerk': 51,
 'Crystal Maiden': 5,
 'Dark Seer': 55,
 'Dazzle': 50,
 'Death Prophet': 43,
 'Disruptor': 87,
 'Doom': 69,
 'Dragon Knight': 49,
 'Drow Ranger': 6,
 'Earth Spirit': 107,
 'Earthshaker': 7,
 'Elder Titan': 103,
 'Ember Spirit': 106,
 'Enchantress': 58,
 'Enigma': 33,
 'Faceless Void': 41,
 'Gyrocopter': 72,
 'Huskar': 59,
 'Invoker': 74,
 'Io': 91,
 'Jakiro': 64,
 'Juggernaut': 8,
 'Keeper of the Light': 90,
 'Kunkka': 23,
 'Legion Commander': 104,
 'Leshrac': 52,
 'Lich': 31,
 'Lifestealer': 54,
 'Lina': 25,
 'Lion': 26,
 'Lone Druid': 80,
 'Luna': 48,
 'Lycan': 77,
 'Magnus': 97,
 'Medusa': 94,
 'Meepo': 82,
 'Mirana': 9,
 'Monkey King': 114,
 'Morphling': 10,
 'Naga Siren': 89,
 "Natures Prophet": 53,
 'Necrophos': 36,
 'Night Stalker': 60,
 'Nyx Assassin': 88,
 'Ogre Magi': 84,
 'Omniknight': 57,
 'Oracle': 111,
 'Outworld Devourer': 76,
 'Phantom Assassin': 44,
 'Phantom Lancer': 12,
 'Phoenix': 110,
 'Puck': 13,
 'Pudge': 14,
 'Pugna': 45,
 'Queen of Pain': 39,
 'Razor': 15,
 'Riki': 32,
 'Rubick': 86,
 'Sand King': 16,
 'Shadow Demon': 79,
 'Shadow Fiend': 11,
 'Shadow Shaman': 27,
 'Silencer': 75,
 'Skywrath Mage': 101,
 'Slardar': 28,
 'Slark': 93,
 'Sniper': 35,
 'Spectre': 67,
 'Spirit Breaker': 71,
 'Storm Spirit': 17,
 'Sven': 18,
 'Techies': 105,
 'Templar Assassin': 46,
 'Terrorblade': 109,
 'Tidehunter': 29,
 'Timbersaw': 98,
 'Tinker': 34,
 'Tiny': 19,
 'Treant Protector': 83,
 'Troll Warlord': 95,
 'Tusk': 100,
 'Underlord': 108,
 'Undying': 85,
 'Ursa': 70,
 'Vengeful Spirit': 20,
 'Venomancer': 40,
 'Viper': 47,
 'Visage': 92,
 'Warlock': 37,
 'Weaver': 63,
 'Windranger': 21,
 'Winter Wyvern': 112,
 'Witch Doctor': 30,
 'Wraith King': 42,
 'Zeus': 22
 # 'Dark Willow': 114,
 # 'Pangolier': 115
 }

heroes = heroDict.keys()
heroes = list(heroes)
formattedHeroes = []

for i in range(0, len(heroes)):
    hero = list(heroes[i].lower())

    if ' ' in hero:
        for i in range(len(hero)):
            if hero[i] == ' ':
                hero[i] = '-'

    hero = "".join(hero)
    formattedHeroes.append(hero)

baseUrl = "http://www.dotabuff.com/heroes/"

ind = 0
outFile = open('michael.csv', 'a')
for hero in heroes:
    heroUrl = baseUrl + formattedHeroes[ind] + "/matchups?date=year"

    header = {'User-Agent': 'test header'}
    r = requests.get(heroUrl, headers=header)
    data = r.text
    # print(data)
    soup = BeautifulSoup(data, "html.parser")

    table = soup('table')[1]
    fuckingpanda = pandas.read_html(str(table))

    df = fuckingpanda[0]

    kappa = list(zip([hero]*len(df.iloc[:,1]), df.iloc[:,1], df.iloc[:,2]))
    for k in kappa:
        if k[1] == 'Pangolier' or k[1] == 'Dark Willow':
            continue
        s = k[0] + ', ' + k[1] + ', ' + k[2]
        outFile.write(s)
        outFile.write('\n')

    ind = ind + 1

outFile.close()


# fuckingpanda = fuckingpanda.iloc[:,2]
# print(fuckingpanda)
