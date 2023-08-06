# py-Hugo Library
A stable Hugo userbot base library, based on Telethon.

[![PyPI - Version](https://img.shields.io/pypi/v/py-Hugo?style=for-the-badge)](https://pypi.org/project/py-Hugo)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/py-Hugo?label=DOWNLOADS&style=for-the-badge)](https://pypi.org/project/py-Hugo)

## Installation
`pip install py-Hugo`

### Creating plugins
- To work everywhere

```python
@hugo_cmd(
    pattern="start",
)   
async def _(e):   
    await eor(e, "Hugo Started")   
```

- To work only in groups

```python
@hugo_cmd(
    pattern="start",
    groups_only=True,
)   
async def _(e):   
    await eor(e, "Hugo Started")   
```

- Assistant Plugins 👇

```python
@asst_cmd("start")   
async def _(e):   
    await e.reply("Hugo Started")   
```

Made with 💕 by [@TeamHugo](https://t.me/TeamHugo). <br />


# License
Hugo is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)

