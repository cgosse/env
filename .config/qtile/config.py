# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
import os
import subprocess


class Commands(object):
    menu = 'dmenu_run -i -b -p "»" -fn "-*-14-*-" -nb "#000" -nf "#fff" -sb "#15181a" -sf "#fff"'
    browser = 'chromium-browser'
    terminal = 'gnome-terminal'
    lock = 'gnome-screensaver-command --lock'
    skype = 'skype'
    files = 'thunar'

    autostart = [browser, terminal, files]


mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("gnome-terminal")),

    # TODO cycle through screens
    #Key([mod], "Tab", lazy.

    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # Audio Volume Keys
    Key([], "XF86AudioMute", lazy.spawn("amixer -q -D pulse sset Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Touchpad
    Key([], "XF86TouchpadToggle", lazy.spawn("toggleTouchpad.sh")),

    # Lock Screen, not sure who is starting gnome-screensaver
    Key([], "XF86Eject", lazy.spawn(Commands.lock))

    # find more uch keys wth xbindkey -k
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

layouts = [
    layout.Max(),
    layout.MonadTall(ratio = 0.67),
    layout.Matrix(),
    layout.VerticalTile()
]

widget_defaults = dict(
    font='HelveticaNeueCondensedBold',
    fontsize=14,
    padding=1,
    background='#073642',
    foreground='#586e75'
)

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(padding=1),
                widget.Prompt(),
                #widget.WindowName(),
                widget.TaskList(padding=1),
                widget.TextBox('  '),
                widget.Notify(fontsize=10),
                widget.TextBox('  '),
                widget.Systray(),
                widget.TextBox(' vol'),
                widget.Volume(),
                widget.TextBox(' bat'),
                widget.Battery(),
                widget.TextBox(' bk'),
                widget.Backlight(backlight_name="intel_backlight"),
                widget.Clock(format=' %Y-%m-%d %a %I:%M %p '),
                widget.TextBox(' cpu'),
                widget.CPUGraph(),
                widget.TextBox(' mem'),
                widget.MemoryGraph(),
                widget.TextBox(' net'),
                widget.NetGraph(),
            ],
            size=22
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    #Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod, "shift"], "Button1", lazy.window.toggle_floating())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#def is_running(process):
#    s = subprocess.Popen(["ps", "axuw"], stdout=subprocess.PIPE)
#    for x in s.stdout:
#        if re.search(process, x):
#            return True
#    return False
#
#
#def execute_once(process):
#    if not is_running(process):
#        return subprocess.Popen(process.split())
#
#
# start the applications at Qtile startup
@hook.subscribe.startup_once
def startupFirst():
    subprocess.Popen("nm-applet")


@hook.subscribe.startup
def allStart():
    resPath = os.path.expanduser('xrdb -load .Xresources')
    subprocess.call(resPath.split())
