"""Pestañas."""
from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys

screen_keys = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('0', '0'),
]
groups = [Group(group[0]) for group in screen_keys]

for i in range(len(screen_keys)):
    actual_key = screen_keys[i][1]
    keys.extend([Key(key[0], key[1], *key[2:]) for key in [
        ([mod], actual_key, lazy.group[groups[i].name].toscreen()),
        ([mod, 'shift'], actual_key, lazy.window.togroup(groups[i].name, switch_group=True)),
    ]])
