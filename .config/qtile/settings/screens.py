import subprocess

from libqtile import bar
from libqtile.config import Screen
from libqtile.log_utils import logger

from .widgets import primary_widgets, secondary_widgets
from .config import status_bar_size, status_bar_opacity
from .path import qtile_path


def status_bar(widgets):
    return bar.Bar(widgets, status_bar_size, opacity=status_bar_opacity)


screens = [
    Screen(
        top=status_bar(primary_widgets),
        wallpaper=qtile_path + "/wallpaper.jpg",
        wallpaper_mode="fill"
    )
]

xrandr = "xrandr | grep -w \"connected\" | cut -d \" \" -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("utf-8")
    connected_monitors = 1
    logger.error(f"Error en el comando {xrandr}: {error}")
else:
    connected_monitors = int(command.stdout.decode("utf-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(
            top=status_bar(secondary_widgets),
            wallpaper=qtile_path + "/wallpaper.jpg",
            wallpaper_mode="fill"
        ))
