# Hugo - UserBot
# Copyright (C) 2021 TeamHugoX
#
# This file is a part of < https://github.com/TeamHugoX/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamHugoX/pyHugo/blob/main/LICENSE>.

from importlib import util
from sys import modules

# for addons


def load_addons(plugin_name):
    if not plugin_name.startswith("__"):
        from .. import HNDLR, LOGS, asst, hugo_bot, udB
        from ..configs import Var
        from ..dB._core import HELP
        from ..misc import _supporter as xxx
        from ..misc._assistant import asst_cmd, callback, in_pattern
        from ..misc._decorators import hugo_cmd
        from ..misc._supporter import Config, admin_cmd, sudo_cmd
        from ..misc._wrappers import eod, eor

        path = "addons/" + plugin_name
        name = path.replace("/", ".")
        spec = util.spec_from_file_location(name, path + ".py")
        mod = util.module_from_spec(spec)
        mod.asst = asst
        mod.tgbot = asst
        mod.hugo_bot = hugo_bot
        mod.ub = hugo_bot
        mod.bot = hugo_bot
        mod.hugo = hugo_bot
        mod.borg = hugo_bot
        mod.telebot = hugo_bot
        mod.jarvis = hugo_bot
        mod.friday = hugo_bot
        mod.eod = eod
        mod.edit_delete = eod
        mod.LOGS = LOGS
        mod.in_pattern = in_pattern
        mod.hndlr = HNDLR
        mod.handler = HNDLR
        mod.HNDLR = HNDLR
        mod.CMD_HNDLR = HNDLR
        mod.Config = Config
        mod.Var = Var
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.asst_cmd = asst_cmd
        mod.hugo_cmd = hugo_cmd
        mod.on_cmd = hugo_cmd
        mod.callback = callback
        mod.Redis = udB.get
        mod.admin_cmd = admin_cmd
        mod.sudo_cmd = sudo_cmd
        modules["ub"] = xxx
        modules["var"] = xxx
        modules["jarvis"] = xxx
        modules["support"] = xxx
        modules["userbot"] = xxx
        modules["telebot"] = xxx
        modules["fridaybot"] = xxx
        modules["jarvis.utils"] = xxx
        modules["uniborg.util"] = xxx
        modules["telebot.utils"] = xxx
        modules["userbot.utils"] = xxx
        modules["userbot.events"] = xxx
        modules["jarvis.jconfig"] = xxx
        modules["userbot.config"] = xxx
        modules["fridaybot.utils"] = xxx
        modules["fridaybot.Config"] = xxx
        modules["userbot.uniborgConfig"] = xxx
        spec.loader.exec_module(mod)
        modules["addons." + plugin_name] = mod
        doc = (
            modules[f"addons.{plugin_name}"].__doc__.format(i=HNDLR)
            if modules[f"addons.{plugin_name}"].__doc__
            else ""
        )
        if "Addons" in HELP.keys():
            update_cmd = HELP["Addons"]
            try:
                update_cmd.update({plugin_name: doc})
            except BaseException:
                pass
        else:
            try:
                HELP.update({"Addons": {plugin_name: doc}})
            except BaseException:
                pass
