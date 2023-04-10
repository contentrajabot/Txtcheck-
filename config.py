#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6004318151:AAGGtBQ2Dwd3AWDny_Dfz5wgdbtToSHJ2wc")
    API_ID = int(os.environ.get("API_ID", "13407681")
    API_HASH = os.environ.get("API_HASH", "26eca59cf75d56bff2b67aea2b783df0")
    AUTH_USERS = "1943226651"

