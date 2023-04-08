#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6193889967:AAFPPgkuB1eFLRR1rQDsfwJwzmv0opicJy0")
    API_ID = int(os.environ.get("API_ID", "23161785"))
    API_HASH = os.environ.get("API_HASH", "72e2c9ff7f587a134a46fe99708e3194")
    AUTH_USERS = "23161785"

