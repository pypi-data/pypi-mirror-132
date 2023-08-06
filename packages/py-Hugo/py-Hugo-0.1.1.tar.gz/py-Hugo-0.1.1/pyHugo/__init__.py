# Hugo - UserBot
# Copyright (C) 2021 TeamHugoX
#
# This file is a part of < https://github.com/TeamHugoX/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamHugoX/pyHugo/blob/main/LICENSE>.


import time

from .configs import Var
from .startup import *
from .startup.BaseClient import HugoClient
from .startup.connections import (
    RedisConnection,
    session_file,
    vc_connection,
    where_hosted,
)
from .startup.exceptions import RedisError
from .startup.funcs import autobot

start_time = time.time()

HOSTED_ON = where_hosted()

udB = RedisConnection(
    host=Var.REDIS_URI or Var.REDISHOST,
    password=Var.REDIS_PASSWORD or Var.REDISPASSWORD,
    port=Var.REDISPORT,
    platform=HOSTED_ON,
    decode_responses=True,
    socket_timeout=5,
    retry_on_timeout=True,
)
if udB.ping():
    LOGS.info("Connected to Redis Database")


hugo_bot = HugoClient(
    session_file(),
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    udB=udB,
    base_logger=TeleLogger,
)

hugo_bot.run_in_loop(autobot())

asst = HugoClient(
    None,
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=udB.get("BOT_TOKEN"),
    udB=udB,
    base_logger=TeleLogger,
)

vcClient = vc_connection(udB, hugo_bot)

if not udB.get("SUDO"):
    udB.set("SUDO", "False")

if not udB.get("SUDOS"):
    udB.set("SUDOS", "")

if not udB.get("BLACKLIST_CHATS"):
    udB.set("BLACKLIST_CHATS", "[]")

HNDLR = udB.get("HNDLR") or "."
DUAL_HNDLR = udB.get("DUAL_HNDLR") or "/"
SUDO_HNDLR = udB.get("SUDO_HNDLR") or HNDLR
