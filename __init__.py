#!/usr/bin/env python3

import sqlite3
import logging
import datetime as DT
from telethon import *

logging.basicConfig(level=logging.INFO)
uptime = DT.datetime.now()

exec(open("BotPanel/data.txt","r").read())
bot = TelegramClient("BotPanel","25539536","d5baaf04257d0a51c940ddf89f4cbe29").start(bot_token=BOT_TOKEN)
try:
	open("BotPanel/database.db")
except:
	x = sqlite3.connect("BotPanel/database.db")
	c = x.cursor()
	c.execute("CREATE TABLE admin (user_id)")
	c.execute("INSERT INTO admin (user_id) VALUES (?)",(ADMIN,))
	x.commit()

def get_db():
	x = sqlite3.connect("BotPanel/database.db")
	x.row_factory = sqlite3.Row
	return x

def valid(id):
	db = get_db()
	x = db.execute("SELECT user_id FROM admin").fetchall()
	a = [v[0] for v in x]
	
	if id in a:
		return "true"
	else:
		return "false"