from libqtile import widget

from .config import font_family, font_size, icon_size, theme


def separator(foreground, background, padding=6):
    return widget.Sep(
        foreground=foreground,
        background=background,
        padding=padding,
        linewidth=0,
    )


def icon(icon, foreground, background, icon_size=icon_size, padding=4):
    return widget.TextBox(
        foreground=foreground,
        background=background,
        font=font_family,
        fontsize=icon_size,
        text=icon,
        padding=padding
    )


def powerline(foreground, background, icon=""):
    return widget.TextBox(
        foreground=foreground,
        background=background,
        text=icon,
        font=font_family,
        fontsize=38,
        padding=-2,
    )


def workspaces(foreground, background):
    return [
        separator(
            foreground=foreground,
            background=background
        ),
        widget.GroupBox(
            foreground=foreground,
            background=background,
            active=theme["active"],
            inactive=theme["inactive"],
            urgent_border=theme["urgent"],
            this_current_screen_border=theme["focus"],
            this_screen_border=theme["grey"],
            other_current_screen_border=theme["dark"],
            other_screen_border=theme["dark"],
            font=font_family,
            fontsize=icon_size,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            rounded=False,
            highlight_method="block",
            urgent_alert_method="block",
            disable_drag=True
        ),
        separator(
            foreground=foreground,
            background=background
        ),
        widget.WindowName(
            foreground=theme["focus"],
            background=background,
            font=font_family,
            fontsize=font_size,
            padding=6
        ),
        separator(
            foreground=foreground,
            background=background
        )
    ]


def systray(foreground, background):
    return [
        separator(
            foreground=foreground,
            background=background,
            padding=14
        ),
        widget.Systray(
            foreground=foreground,
            background=background,
            icon_size=icon_size,
            padding=6
        ),
        separator(
            foreground=foreground,
            background=background,
            padding=14
        ),
    ]


def control(color, color_end, color_font):
    return [
        powerline(
            foreground=color,
            background=color_end
        ),
        icon(
            icon="",
            foreground=color_font,
            background=color
        ),
        separator(
            foreground=color,
            background=color
        ),
        widget.PulseVolume(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size
        ),
        separator(
            foreground=color,
            background=color
        ),
        icon(
            icon="",
            foreground=color_font,
            background=color
        ),
        separator(
            foreground=color,
            background=color
        ),
        widget.Backlight(
            foreground=color_font,
            background=color,
            backlight_name="intel_backlight",
            font=font_family,
            fontsize=font_size
        ),
        separator(
            foreground=color,
            background=color
        ),
        # icon(
        #     icon="",
        #     foreground=color_font,
        #     background=color
        # ),
        # separator(
        #     foreground=color,
        #     background=color
        # ),
        # widget.Battery(
        #     foreground=color_font,
        #     background=color,
        #     low_foreground=theme["focus"],
        #     font=font_family,
        #     fontsize=font_size,
        #     format="{char} {percent:2.0%}",
        #     notify_below=True
        # ),
        # separator(
        #     foreground=color,
        #     background=color
        # ),
    ]


def usage(color, color_end, color_font):
    return [
        powerline(
            foreground=color,
            background=color_end
        ),
        widget.CPU(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            format="CPU: {load_percent}%",
            update_interval=3.0
        ),
        separator(
            foreground=color,
            background=color
        ),
        widget.Memory(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            format="MEM: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
            update_interval=3.0
        ),
        separator(
            foreground=color,
            background=color
        )
    ]


def update(color, color_end, color_font):
    return [
        powerline(
            foreground=color,
            background=color_end
        ),
        icon(
            icon="",
            foreground=color_font,
            background=color
        ),
        separator(
            foreground=color,
            background=color
        ),
        widget.CheckUpdates(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            colour_have_updates=theme["text"],
            colour_no_updates=theme["text"],
            no_update_string="0",
            display_format="{updates}",
            update_interval=1800,
            custom_command="checkupdates",
        ),
        separator(
            foreground=color,
            background=color
        )
    ]


def layout(color, color_end, color_font):
    return [
        powerline(
            foreground=color,
            background=color_end
        ),
        widget.CurrentLayoutIcon(
            foreground=color_font,
            background=color,
            scale=0.5,
            font=font_family,
            fontsize=icon_size
        ),
        widget.CurrentLayout(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            padding=4
        ),
        separator(
            foreground=color,
            background=color
        )
    ]


def clock(color, color_end, color_font):
    return [
        powerline(
            foreground=color,
            background=color_end
        ),
        icon(
            icon="",
            foreground=color_font,
            background=color
        ),
        separator(
            foreground=color,
            background=color
        ),
        widget.Clock(
            foreground=color_font,
            background=color,
            font=font_family,
            fontsize=font_size,
            format="%d/%m/%Y - %H:%M:%S"
        ),
        separator(
            foreground=color,
            background=color
        ),
    ]


primary_widgets = [
    *workspaces(
        foreground=theme["text"],
        background=theme["dark"]
    ),
    *systray(
        foreground=theme["text"],
        background=theme["dark"]
    ),
    *control(
        color=theme["color5"],
        color_end=theme["dark"],
        color_font=theme["text"]
    ),
    *usage(
        color=theme["color4"],
        color_end=theme["color5"],
        color_font=theme["text"]
    ),
    *update(
        color=theme["color3"],
        color_end=theme["color4"],
        color_font=theme["text"]
    ),
    *layout(
        color=theme["color2"],
        color_end=theme["color3"],
        color_font=theme["text"]
    ),
    *clock(
        color=theme["color1"],
        color_end=theme["color2"],
        color_font=theme["text"]
    )
]

secondary_widgets = [
    *workspaces(
        foreground=theme["text"],
        background=theme["dark"]
    ),
    *layout(
        color=theme["color2"],
        color_end=theme["dark"],
        color_font=theme["text"]
    ),
    *clock(
        color=theme["color1"],
        color_end=theme["color2"],
        color_font=theme["text"]
    )
]

widget_defaults = {
    "font": font_family,
    "fontsize": font_size,
    "padding": 4,
}

extension_defaults = widget_defaults.copy()
