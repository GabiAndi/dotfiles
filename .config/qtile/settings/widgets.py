from libqtile import widget

from .config import font_family, font_size, icon_size, theme


def base(fg=theme["text"], bg=theme["dark"]): 
    return {
        "foreground": fg,
        "background": bg
    }
    

def separator(fg=theme["text"], bg=theme["dark"], padding=6):
    return widget.Sep(**base(fg=fg, bg=bg), linewidth=0, padding=padding)


def icon(fg=theme["text"], bg=theme["dark"], fontsize=icon_size, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg=theme["light"], bg=theme["dark"]):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=37,
        padding=-2
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg=theme["light"]),
            font=font_family,
            fontsize=font_size,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=theme["active"],
            inactive=theme["inactive"],
            rounded=False,
            highlight_method="block",
            urgent_alert_method="block",
            urgent_border=theme["urgent"],
            this_current_screen_border=theme["focus"],
            this_screen_border=theme["grey"],
            other_current_screen_border=theme["dark"],
            other_screen_border=theme["dark"],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg=theme["focus"]), fontsize=font_size, padding=6),
    ]


primary_widgets = [
    *workspaces(),
    separator(),
    widget.Systray(background=theme["dark"], padding=6),
    separator(padding=14),
    powerline(theme["color4"], theme["dark"]),
    icon(bg=theme["color4"], fontsize=17, text=""),
    separator(theme["dark"], theme["color4"]),
    widget.PulseVolume(background=theme["color4"], foreground=theme["dark"], font=font_family),
    separator(theme["color3"], theme["color4"]),
    powerline(theme["color3"], theme["color4"]),
    icon(bg=theme["color3"], text=""),
    widget.CheckUpdates(
        background=theme["color3"],
        colour_have_updates=theme["text"],
        colour_no_updates=theme["text"],
        no_update_string="0",
        display_format="{updates}",
        update_interval=1800,
        custom_command="checkupdates",
    ),
    separator(theme["color2"], theme["color3"]),
    powerline(theme["color2"], theme["color3"]),
    widget.CurrentLayoutIcon(**base(bg=theme["color2"]), scale=0.5),
    widget.CurrentLayout(**base(bg=theme["color2"]), padding=5),
    separator(theme["color3"], theme["color2"]),
    powerline(theme["color1"], theme["color2"]),
    icon(bg=theme["color1"], fontsize=17, text=""),
    separator(theme["color2"], theme["color1"]),
    widget.Clock(**base(bg=theme["color1"]), format="%d/%m/%Y - %H:%M:%S"),
    separator(theme["color2"], theme["color1"]),    
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline(theme["color2"], theme["dark"]),
    widget.CurrentLayoutIcon(**base(bg=theme["color2"]), scale=0.5),
    widget.CurrentLayout(**base(bg=theme["color2"]), padding=5),
    separator(theme["color3"], theme["color2"]),
    powerline(theme["color1"], theme["color2"]),
    icon(bg=theme["color1"], fontsize=17, text=""),
    separator(theme["color2"], theme["color1"]),
    widget.Clock(**base(bg=theme["color1"]), format="%d/%m/%Y - %H:%M:%S"),
    separator(theme["color2"], theme["color1"]),
]   

widget_defaults = {
    "font": font_family,
    "fontsize": font_size,
    "padding": 4,
}

extension_defaults = widget_defaults.copy()
