#!/usr/bin/env python3
# Author: Erton Silva
# -*- coding: utf-8 -*-

import argparse
import sys
import requests
import json
from requests.exceptions import HTTPError
import pokeparser

#arguments
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
api_link = ('https://pokeapi.co/api/v2/')

arguments = {}

if len(sys.argv)==1:
     parser.print_help(sys.stderr)
     sys.exit(1)

if args.author == True:
    arguments['Author'] = 'True'
    authorcredits = open('credits.txt', 'r')
    print(authorcredits.read())
    sys.exit(1)
else:
    arguments['Author'] = False
    if args.name != None:	
        arguments['Nameid'] = args.name
    else:
    	arguments['Nameid'] = 'None'
    if args.verbose != None:
        arguments['Verbose'] = args.verbose
    else:
    	arguments['Verbose'] = 'None'
    if args.berry != None:
	    arguments['Berry'] = args.berry
    else:
	    arguments['Berry'] = 'None'
    if args.generation != None:
	    arguments['Generation'] = args.generation
    else:
	    arguments['Generation'] = 'None'
    if args.type != None:
	    arguments['Type'] = args.type
    else:
	    arguments['Type'] = 'None'
    if args.item != None:
	    arguments['Item'] = args.item
    else:
	    arguments['Item'] = 'None'

def get_raw_data(request_link):
    try:
        response = requests.get(request_link)
        response.raise_for_status()
    except HTTPError as http_err:
        print('An HTTP error as occurred {http_err}')
    except Exception as err:
        print ('Other error occurred: {err}')
    else:
        raw_data = json.loads(response.content)
        return raw_data


#print (get_pokemon_raw_data(api_link, args.name))

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