#!/usr/bin/env python3
# Author: Erton Silva
# -*- coding: utf-8 -*-

import argparse
import sys
import requests
import json
from requests.exceptions import HTTPError

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

#link da API
api_link = ('https://pokeapi.co/api/v2/')

def check_args():
    arguments = [""]

    if args.name != None:	
    	if type(args.name) == str:
            pokename = ('pokemon/')
            arguments.append(pokename)
    else:
    	arguments.append('None')
    

    if args.verbose != None:
        arguments.append(args.verbose)
    else:
    	arguments.append('None')

    if args.berry != None:
	    arguments.append(args.berry)
    else:
	    arguments.append('None')

    if args.generation != None:
	    arguments.append(args.generation)
    else:
	    arguments.append('None')

    if args.type != None:
	    arguments.append(args.type)
    else:
	    arguments.append('None')

    if args.item != None:
	    arguments.append(args.type)
    else:
	    arguments.append('None')

    if args.author == True:
	    arguments.append(args.author)
    else:
	    arguments.append('None')
    return arguments


def check_api_connectivity(api_link):
    try:
        response = requests.get(api_link)
        response.raise_for_status()
    except HTTPError as http_err:
        print('An HTTP error as occurred {http_err}')
    except Exception as err:
        print ('Other error occurred: {err}')
    else:
        return True

def get_pokemon_raw_data(api_link, name):
    api_link = (api_link + 'pokemon/' + name)
    json_raw_request = requests.get(api_link)
    raw_request = json.loads(json_raw_request.content)
    return raw_request

check = (check_api_connectivity(api_link))


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