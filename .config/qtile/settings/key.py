from libqtile.config import Key
from libqtile.lazy import lazy
from settings.env import mod, terminal

keys = [


    # Change language keymap

    Key([mod, "shift"],"e", lazy.spawn("setxkbmap latam")),

    Key([mod, "shift"],"u", lazy.spawn("setxkbmap us")),

    # Menu synapse open

    Key([mod],"o", lazy.spawn("synapse")),

    # Make floating a window

    Key([mod], "f", lazy.window.toggle_floating()),

    # Red Screen light

    Key([mod],"a",lazy.spawn("redshift -l 19.03793:-98.20346 -O 4500")),


    Key([mod,"shift"],"a",lazy.spawn("redshift -x")),

    # Brightness atachment keys

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),

    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),

    # Floating Layout

    Key([mod],"f", lazy.window.toggle_floating()),

    # Volume atachment keys

    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),

    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Switch into all windows

    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Change principal window

    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]
