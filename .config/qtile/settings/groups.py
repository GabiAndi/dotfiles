from libqtile.config import Key, Group
from libqtile.command import lazy

from .keys import mod, keys


groups = [Group(group) for group in [
    '\uf303', # Arch
    '\ufa9e', # Web
    '\uf6ed', # Correo
    '\uf68c', # Console
    '\ue796', # Code
    '\uf98a', # Server
    '\uf92a', # Job
    '\ueb7b', # VMs
]]

for i in range(len(groups)):
    keys.extend([Key(key[0], key[1], *key[2:]) for key in [
        (
            [mod],
            f"{i+1}",
            lazy.group[groups[i].name].toscreen()
        ),
        (
            [mod, "shift"],
            f"{i+1}",
            lazy.window.togroup(groups[i].name, switch_group=True)
        ),
    ]])
