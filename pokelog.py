#!/usr/bin/env python3
# Author: Erton Silva
# -*- coding: utf-8 -*-

import logging
import os

script_path = (os.getcwd())

def debug():
    logging.basicConfig(filename=script_path+ '/.log', filemode='a', format='%(process)d - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

debug()