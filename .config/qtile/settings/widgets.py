"""Widgets."""
from libqtile.widget.sep import Sep
from libqtile.widget.textbox import TextBox
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.windowname import WindowName
from libqtile.widget.systray import Systray
#from libqtile.widget.pulse_volume import PulseVolume
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.currentlayout import CurrentLayoutIcon, CurrentLayout
from libqtile.widget.clock import Clock
# from libqtile.widget.battery import Battery
# from libqtile.widget.backlight import Backlight
from .config import font_family, font_size, icon_size, theme


def separator(foreground, background, padding=6):
    """Separador."""
    return Sep(
        foreground=foreground,
        background=background,
        padding=padding,
        linewidth=0,
    )


def icon(text_icon: str, foreground: str, background: str, size=icon_size, padding=4):
    """Icono."""
    return TextBox(
        foreground=foreground,
        background=background,
        font=font_family,
        fontsize=size,
        text=text_icon,
        padding=padding,
    )


def workspaces(foreground, background):
    """Definición de espacios de trabajo."""
    return [
        GroupBox(
            foreground=foreground,
            background=background,
            active=theme['active'],
            inactive=theme['inactive'],
            urgent_border=theme['urgent'],
            this_current_screen_border=theme['focus'],
            this_screen_border=theme['grey'],
            other_current_screen_border=theme['dark'],
            other_screen_border=theme['dark'],
            font=font_family,
            fontsize=icon_size,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            disable_drag=True,
        ),
        separator(
            foreground=foreground,
            background=background,
        ),
        WindowName(
            foreground=theme['focus'],
            background=background,
            font=font_family,
            fontsize=font_size,
            padding=6,
        ),
        separator(
            foreground=foreground,
            background=background,
        ),
    ]


def systray(foreground, background):
    """Bandeja del sistema."""
    return [
        separator(
            foreground=foreground,
            background=background,
            padding=14,
        ),
        Systray(
            foreground=foreground,
            background=background,
            icon_size=icon_size,
            padding=6,
        ),
        separator(
            foreground=foreground,
            background=background,
            padding=14,
        ),
    ]


def control(color, color_end, color_font):
    """Control de audio, brillo, bateria, etc."""
    return [
        # separator(
        #     foreground=color_end,
        #     background=color,
        # ),
        # icon(
        #     text_icon='󰕾',
        #     foreground=color_font,
        #     background=color,
        # ),
        # separator(
        #     foreground=color,
        #     background=color,
        # ),
        # PulseVolume(
        #     foreground=color_font,
        #     background=color,
        #     font=font_family,
        #     fontsize=font_size,
        # ),
        # separator(
        #     foreground=color,
        #     background=color,
        # ),
        # icon(
        #     text_icon='󰌵',
        #     foreground=color_font,
        #     background=color,
        # ),
        # separator(
        #     foreground=color,
        #     background=color,
        # ),
        # Backlight(
        #     foreground=color_font,
        #     background=color,
        #     backlight_name='intel_backlight',
        #     font=font_family,
        #     fontsize=font_size,
        # ),
        # separator(
        #     foreground=color,
        #     background=color,
        # ),
        # icon(
        #     text_icon='󰁹',
        #     foreground=color_font,
        #     background=color,
        # ),
        # separator(
        #     foreground=color,
        #     background=color,
        # ),
        # Battery(
        #     foreground=color_font,
        #     background=color,
        #     low_foreground=theme['focus'],
        #     font=font_family,
        #     fontsize=font_size,
        #     format='{char} {percent:2.0%}',
        #     notify_below=True,
        # ),
        # separator(
        #     foreground=color,
        #     background=color,
        # ),
    ]


def usage(color, color_end, color_font):
    """Uso de memoria y procesador."""
    return [
        separator(
            foreground=color_end,
            background=color,
        ),
        CPU(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            format='CPU:{load_percent}%',
            update_interval=5.0,
        ),
        separator(
            foreground=color,
            background=color,
        ),
        Memory(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            format='RAM:{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
            update_interval=5.0,
        ),
        separator(
            foreground=color,
            background=color,
        ),
    ]


def layout(color, color_end, color_font):
    """Modo de layout actual."""
    return [
        separator(
            foreground=color_end,
            background=color,
        ),
        CurrentLayoutIcon(
            foreground=color_font,
            background=color,
            scale=0.5,
            font=font_family,
            fontsize=icon_size,
        ),
        CurrentLayout(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            padding=4,
        ),
        separator(
            foreground=color,
            background=color,
        ),
    ]


def clock(color, color_end, color_font):
    """Reloj del sistema."""
    return [
        separator(
            foreground=color_end,
            background=color,
        ),
        icon(
            text_icon='󰸗',
            foreground=color_font,
            background=color,
        ),
        separator(
            foreground=color,
            background=color,
        ),
        Clock(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            format='%d/%m/%Y-%H:%M:%S',
        ),
        separator(
            foreground=color,
            background=color,
        ),
    ]


primary_widgets = [
    *workspaces(
        foreground=theme['text'],
        background=theme['dark'],
    ),
    *systray(
        foreground=theme['text'],
        background=theme['dark'],
    ),
    *control(
        color=theme['color5'],
        color_end=theme['dark'],
        color_font=theme['text'],
    ),
    *usage(
        color=theme['color4'],
        color_end=theme['color5'],
        color_font=theme['text'],
    ),
    # *update(
    #     color=theme['color3'],
    #     color_end=theme['color4'],
    #     color_font=theme['text'],
    # ),
    # *layout(
    #     color=theme['color2'],
    #     color_end=theme['color3'],
    #     color_font=theme['text'],
    # ),
    *clock(
        color=theme['color1'],
        color_end=theme['color4'],
        color_font=theme['text'],
    )
]

secondary_widgets = [
    *workspaces(
        foreground=theme['text'],
        background=theme['dark'],
    ),
    # *layout(
    #     color=theme['color2'],
    #     color_end=theme['dark'],
    #     color_font=theme['text'],
    # ),
    *clock(
        color=theme['color1'],
        color_end=theme['dark'],
        color_font=theme['text'],
    )
]

widget_defaults = {
    'font': font_family,
    'fontsize': font_size,
    'padding': 4,
}

extension_defaults = widget_defaults.copy()
