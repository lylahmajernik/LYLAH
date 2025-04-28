# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import sqlite3
import logging
import  logging.config

logging.config.fileConfig('config.ini')

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(filename= 'teambattle.log', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

@app.route('/')
def main():
    logger.debug('on main')
    return 'main'
#
 #
  # POKEMON
 #
#
@app.route("/pokemon", methods=['GET','POST'])

#
 #
  # TRAINER
 #
#
@app.route("/trainer", methods=['GET','POST', 'DELETE'])

#
 #
  # TEAM
 #
#
@app.route("/team", methods=['GET','POST', 'DELETE'])


#
 #
  # MEMBERSHIP
 #
#
@app.route("/membership", methods=['POST', 'DELETE'])

#
 #
  # RANKING
 #
#
@app.route("/ranking", methods=['GET'])

#
 #
  # BATTLE
 #
#
@app.route("/battle", methods=['POST'])

#
 #
  #
 #
#