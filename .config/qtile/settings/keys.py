"""Atajos de teclado."""
from libqtile.config import Key
from libqtile.lazy import lazy
from .config import mod, terminal, web_browser, file_explorer


keys = [Key(key[0], key[1], *key[2:]) for key in [
    # Mover el foco de la ventana en un grupo
    ([mod], 'h', lazy.layout.left()),
    ([mod], 'l', lazy.layout.right()),
    ([mod], 'j', lazy.layout.down()),
    ([mod], 'k', lazy.layout.up()),
    # Cambiar foco de pantallas
    ([mod], 'i', lazy.prev_screen()),
    ([mod], 'o', lazy.next_screen()),
    # Mover ventanas en el grupo
    ([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    ([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
    ([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    ([mod, 'shift'], 'k', lazy.layout.shuffle_up()),
    # Cambiar tamaños
    ([mod, 'control'], 'l', lazy.layout.grow()),
    ([mod, 'control'], 'h', lazy.layout.shrink()),
    # Acciones
    ([mod], 'w', lazy.window.kill()),
    ([mod], 'Tab', lazy.next_layout()),
    ([mod, 'shift'], 'Tab', lazy.prev_layout()),
    ([mod, 'control'], 'r', lazy.reload_config()),
    ([mod, 'control'], 'q', lazy.shutdown()),
    ([mod, 'shift'], 'r', lazy.spawn('reboot')),
    ([mod, 'shift'], 'q', lazy.spawn('poweroff')),
    # Volumen
    ([], 'XF86AudioLowerVolume', lazy.spawn('pamixer --decrease 5')),
    ([], 'XF86AudioRaiseVolume', lazy.spawn('pamixer --increase 5')),
    ([], 'XF86AudioMute', lazy.spawn('pamixer --toggle-mute')),
    # Brillo
    ([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +5%')),
    ([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 5%-')),
    # Multimedia
    ([], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
    ([], 'XF86AudioNext', lazy.spawn('playerctl next')),
    ([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
    ([], 'XF86AudioPause', lazy.spawn('playerctl play-pause')),
    # Screenshot
    ([mod], 's', lazy.spawn('scrot')),
    ([mod, 'shift'], 's', lazy.spawn('scrot -s')),
    # Menu
    ([mod], 'm', lazy.spawn('rofi -show drun')),
    ([mod, 'shift'], 'm', lazy.spawn('rofi -show window')),
    # Aplicaciones
    ([mod], 'Return', lazy.spawn(terminal)),
    ([mod], 'e', lazy.spawn(file_explorer)),
    ([mod], 'g', lazy.spawn(web_browser)),
]]
