from bs4 import BeautifulSoup
import requests
from abc import ABC, abstractmethod
from dict_client import *
import json


def simple_cache(func): #FIFO with limit 10
    with open('cache.json', 'r') as json_file:
        cache = json.load(json_file)
    def wrapper(self, word):
        if word in cache:
            return cache[word]
        result = func(self, word)
        if len(cache) == 10:
            del cache[str(list(cache.keys())[0])]
            cache[word] = result
        else:
            cache[word] = result
        json_object = json.dumps(cache, indent = 4)
        with open('cache.json', 'w') as json_file:
            json_file.write(json_object)
        return result
    return wrapper


def LRU_cache(func): #limit 10
    with open('lru_cache.json', 'r') as json_file:
        cache = json.load(json_file)
    def wrapper(self, word):
        if word in cache:
            temp = cache[word]
            del cache[word]
            cache[word] = temp
            json_object = json.dumps(cache, indent = 4)
            with open('lru_cache.json', 'w') as json_file:
                json_file.write(json_object)
            return cache[word]
        result = func(self, word)
        if len(cache) == 10:
            del cache[str(list(cache.keys())[0])]
            cache[word] = result
        else:
            cache[word] = result
        json_object = json.dumps(cache, indent = 4)
        with open('lru_cache.json', 'w') as json_file:
            json_file.write(json_object)
        return result
    return wrapper



class Dictionary(ABC):
    @abstractmethod
    def find(self):
        pass


class CambridgeDictionaryService(Dictionary):
    """ An online dictionary service with the cambridge dictionary """

    def find(self, word):
        f = requests.get('https://dictionary.cambridge.org/dictionary/english/' + word, 
                         headers={'user-agent': 'Mozilla/Firefox'})
        soup = BeautifulSoup(f.content, "html.parser")
        hits = soup.findAll('div', attrs={'class': 'def'})

        defs = []
        for h in hits:
            defs.append(h.text)
        return defs
    
    
class dict_protocol_dictionary_1(Dictionary):
    @simple_cache
    def find(self, word):
        con = Connection("dict.org") 
        db = Database(con, "wn") #specify database here
        def_list = db.define(word) 
        for x in def_list:
            s = (x.getdefstr() + '\n')
        return s
    

class dict_protocol_dictionary_2(Dictionary):
    @LRU_cache
    def find(self, word):
        con = Connection("dict.org") 
        db = Database(con, "wn") #specify database here
        def_list = db.define(word) 
        for x in def_list:
            s = (x.getdefstr() + '\n')
        return s
    



def menu():
    obj = dict_protocol_dictionary_1()
    obj2 = dict_protocol_dictionary_2()
    while True:  
        print("\nMAIN MENU")  
        print("1. Word lookup though simple caching")  
        print("2. Word lookup through LRU caching")
        print("3. Exit") 
        choice = int(input("Enter Choice: ")) 
        if choice == 1:
            word = input("Enter word to find meaning and synonyms for: ")
            print("\n" + obj.find(word))
        elif choice == 2:
            word = input("Enter word to find meaning and synonyms for: ")
            print("\n" + obj2.find(word))
        elif choice == 3:
            break
        else:
            print("Enter a valid choice")







