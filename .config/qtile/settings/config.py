"""Configuración de qtile."""
from .theme import my_theme


# Teclas
mod = 'mod4'
# Tema
theme = my_theme
# Fondo de pantalla de monitor principal
primary_wallpaper_file = 'wallpaper.jpg'
primary_wallpaper_mode = 'fill'
# Fondo de pantalla de monitores secundarios
secondary_wallpaper_file = 'wallpaper.jpg'
secondary_wallpaper_mode = 'fill'
# Barra
status_bar_size = 30
status_bar_opacity = 1.0
# Fuentes
font_family = 'JetBrainsMono Nerd Font'
font_size = 18
icon_size = 22
# Aplicaciones
terminal = 'alacritty'
web_browser = 'firefox'
file_explorer = 'thunar'
