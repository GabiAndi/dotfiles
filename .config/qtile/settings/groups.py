from libqtile.config import Key, Group
from libqtile.command import lazy

from .keys import mod, keys


groups = [Group(group) for group in [
    "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
]]

for i in range(len(groups)):
    actual_key = str(i + 1)
    
    keys.extend([Key(key[0], key[1], *key[2:]) for key in [
        (
            [mod],
            actual_key,
            lazy.group[groups[i].name].toscreen()
        ),
        (
            [mod, "shift"],
            actual_key,
            lazy.window.togroup(groups[i].name, switch_group=True)
        ),
    ]])
