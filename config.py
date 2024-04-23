#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7134740883:AAHiFTXFocfyOJZb24vf_HwPf36mf---1go")
    API_ID = int(os.environ.get("API_ID", "27464924"))
    API_HASH = os.environ.get("API_HASH", "f28d089001481597f045b70a0daa73e4")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6395950392")
