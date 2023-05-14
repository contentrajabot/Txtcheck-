#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5849984859:AAHTBxoM6A0eMU3yvOpy0eOT5HxitYIKPRA")
    API_ID = int(os.environ.get("API_ID", "818663"))
    API_HASH = os.environ.get("API_HASH", "b31cf04c3cc21aa600eca3a991085702")
    AUTH_USERS = ""


