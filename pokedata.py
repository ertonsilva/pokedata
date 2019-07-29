#!/usr/bin/env python3
# Autor: Erton Silva
# -*- coding: utf-8 -*-

import argparse
import sys
import requests
import json

#argumentos
parser = argparse.ArgumentParser(description='Script to request pokemon info from "pokeapi.co", enjoy!',
    usage='%(prog)s [options]',
    epilog='If you have any questions please use the option --author and get in contact'
    )
parser.add_argument('-n', '--name', help='Search all info about this pokemon name')
parser.add_argument('-t', '--type', help='Search all info about this pokemon type')
parser.add_argument('-b', '--berry', help='Search all info about this berry')
parser.add_argument('-i', '--item', help='Search the item name')
parser.add_argument('-g', '--generation', type=int, choices=range(9) ,help='Choose the generation')
parser.add_argument('-v', '--verbose', action='count', help='Get the verbose output')
parser.add_argument('--version', action='version', version='%(prog)s 0.1', help='Show this script version')
parser.add_argument('--author', action='store_true', help='Get the author name and contacts')
args = parser.parse_args()

#link da API
api_link = ('https://pokeapi.co/api/v2/')

if args.name != None:
    pokename = ('pokemon/' + args.name)

def apirequest(api, pokename):
    teste = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    return teste.content

if len(sys.argv)==1:
     parser.print_help(sys.stderr)
     sys.exit(1)

if args.verbose == 1:
    print ('verbosinho')

elif args.verbose == 2:
    print ('verboso')

elif args.verbose == 3:
    if args.name != None:
        print (apirequest(api, pokename))
    elif args.berry != None:
        print ('testado')
    elif args.generation != None:
        print ('testado')
    elif args.type != None:
        print ('testado')
    elif args.item != None:
        print ('testado')
    else:
        print ('\nPlease inform something to do the search, valid options are \'-n\' \'-g\' \'-t\' \'-i\'\n')
        parser.print_help(sys.stderr)
        sys.exit(1)

elif args.verbose == None:
    if args.author == True:
        print ('\nIf you have a problem or questions, get in touch:')
        print ('Erton Silva\nTelegram: @ertonsilva\nGit: https://github.com/ertonsilva/ \nE-mail: erton.silva14@gmail.com\n')

elif args.verbose >= 4:
    print ('The maximum verbosity is 3')




def get_pokemon_raw_data(api_link, name):
    api_link = (api_link + 'pokemon/' + name)
    json_raw_request = requests.get(api_link)
    raw_request = json.loads(json_raw_request.content)
    return raw_request

print (get_pokemon_raw_data(api_link, args.name))

#funcões para pokemon
#podem ser chamadas com nome ou ID
#get_abilities
#get_forms
#get_game_indicies
#get_held_items
#get_moves
#get_species
#get_sprites
#get_stats
#get_type
#   get_type_weakness
#   get_type_strong
#   get_type_pokemons
#
#