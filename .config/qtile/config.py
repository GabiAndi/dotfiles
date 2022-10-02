# Importaciones
import subprocess

from os import path
from libqtile import hook

# Configuraciones
from settings.keys import keys
from settings.groups import groups
from settings.layouts import layouts
from settings.screens import screens
from settings.mouse import mouse
from settings.widgets import widget_defaults, extension_defaults
from settings.path import qtile_path


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
wmname = "LG3D"
