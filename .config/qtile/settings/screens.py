"""Pantallas."""

import subprocess
from libqtile import bar
from libqtile.config import Screen
from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets
from .config import (status_bar_size, status_bar_opacity,
                     primary_wallpaper_file, primary_wallpaper_mode,
                     secondary_wallpaper_file, secondary_wallpaper_mode)
from .path import qtile_path


def status_bar(widgets):
    '''Barra de estado.'''
    return bar.Bar(widgets, status_bar_size, opacity=status_bar_opacity)


def wallpaper(wallpaper_file, wallpaper_mode):
    '''Fondo de pantalla.'''
    return {
        'wallpaper': qtile_path + '/' + wallpaper_file,
        'wallpaper_mode': wallpaper_mode
    }


screens = [
    Screen(
        top=status_bar(primary_widgets),
        **wallpaper(primary_wallpaper_file, primary_wallpaper_mode)
    )
]

XRAND_COMMAND = 'xrandr | grep -w \'connected\' | cut -d \' \' -f 2 | wc -l'

command = subprocess.run(
    XRAND_COMMAND,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    check=False,
)

if command.returncode != 0:
    error = command.stderr.decode('utf-8')
    connected_monitors = 1
    logger.error('Error en el comando %s: %s', XRAND_COMMAND, error)
else:
    connected_monitors = int(command.stdout.decode('utf-8'))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(
            top=status_bar(secondary_widgets),
            **wallpaper(secondary_wallpaper_file, secondary_wallpaper_mode)
        ))
