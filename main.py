from pprint import pprint

import requests



url = 'https://superheroapi.com/api/2619421814940190'


class SuperHero:
    url = 'https://superheroapi.com/api/2619421814940190'
    # heroes_list = []

    def __init__(self, name):
        self.name = name
        self.id = int()
        self.intelligence = int()


    def find_intelligence(self):
        res = requests.get(url + '/search/' + self.name).json()
        # pprint(res)
        res_list = res['results']
        # print(res_list)
        for new_dict in res_list:
            new_dict = res_list[0]
            # pprint(new_dict)
            powers = new_dict['powerstats']['intelligence']
            # print(new_dict['id'])
            self.intelligence = powers
        # print(self.powers)

def find_the_best(list1):
    new_dict = {}
    for el in list1:
        new_dict[el.name] = int(el.intelligence)

    return f'Самый умный: {max(new_dict)}'






superhero1 = SuperHero('Hulk')

superhero2 = SuperHero('Captain America')

superhero3 = SuperHero('Thanos')

superhero1.find_intelligence()
# print(superhero1.intelligence)
superhero2.find_intelligence()
superhero3.find_intelligence()
SH_list = [superhero1, superhero2, superhero3]

print(find_the_best(SH_list))
