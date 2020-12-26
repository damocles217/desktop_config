# Qtile Settings

# Qtile import 

from typing import List  # noqa: F401
from libqtile import hook
import subprocess

# Settings imports

# from settings.env import home
from settings.key import keys
from settings.groups import groups
from settings.screens import screens, widget_defaults, extension_defaults
from settings.layouts import layouts, floating_layout
from settings.mouse import mouse


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"


wmname = "LG3D"
