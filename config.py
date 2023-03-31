#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6265528725:AAGZz4RCUYeXQZ0fv4Xy8iGHc1MtKZvKeUY")
    API_ID = int(os.environ.get("API_ID", "23365392"))
    API_HASH = os.environ.get("API_HASH", "fffdba007ae9e02207be11b8d8d3f2a8")
    AUTH_USERS = "5757528547"

