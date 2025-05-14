#!/usr/bin/env python3

from BotPanel import *
from importlib import import_module
from BotPanel.modules import ALL_MODULES

for module_name in ALL_MODULES:
        imported_module = import_module("BotPanel.modules." + module_name)
bot.run_until_disconnected()