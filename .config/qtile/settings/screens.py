from libqtile.config import Screen
from libqtile import bar, widget

base = lambda fg='text', bg='dark': {
    'foreground': fg,
    'background': bg
}

powerline = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
    text="", # Icon: nf-oct-triangle_left
    fontsize=50,
    padding=-4.5,
    #margin=25

)

separator = lambda fg="light", bg="dark": widget.TextBox(

    **base(fg, bg),
    padding_x=5,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=['#eeeeee','#eeeeee'],
                    inactive=['#212f3d','#212f3d'],
                    highlight_color=['#f1c40f','#f1c40f'],
                    block_highlight_text_color='#a93226',
                    highlight_method="line",
                    background=['#f39c12','#f39c12'],
                    this_screen_border=['#273746','#273746'],
                    this_current_screen_border=['#273746','#273746'],
                    other_current_screen_border=['#eeeeee','#eeeeee'],
                    other_screen_border=['#273746','#273746'],
                    disable_drag=False,
                    fontsize=23,
                    border_x=9,
                    border_y=6,
                    urgent_alert_method='border',
                    urgent_border='#FF0040',
                    rounded=False,
                ),
                widget.Prompt(
                    fontsize=18,
                    foreground='#273746',
                    prompt='$: ',
                    background=['#f39c12','#f39c12'],
                ),
                separator('#273746','#273746'),
                widget.WindowName(
                    foreground='#f39c12',
                    background='#273746',
                    font="CodeNewRoman, bold",
                    fontsize=16,
                    padding=7,
                ),
                widget.Battery(
                    background='#273746',
                    format='{char} {percent:2.0%}',
                    foreground='#2ecc71',
                    low_percentage=0.2,
                    notify_below=True,
                    low_foreground='#DF0101',
                    fontsize=16,
                    fontwidth=10,
                    font="CodeNewRoman NerdFont, bold"
                ),
                separator('#273746','#273746'),
                powerline('#a569bd','#273746'),
                separator('#a569bd','#a569bd'),
                widget.Systray(
                    background='#a569bd',
                    fontsize=25,
                    margin_x=5,
                    scale=3.5,
                ),
                powerline('#f39c12','#a569bd'),
                widget.Clock(
                    foreground='#273746',
                    font="CodeNewRoman NerdFont, bold",
                    fontwidth=10,
                    background='#f39c12',
                    fontsize=17,
                    format='  %Y-%m-%d %a %I:%M'),
                widget.CurrentLayoutIcon(
                    background='#f1c40f',
                    foreground='#273746',
                    scale=0.65,
                ),
            ],
            30,
            opacity=0.9,
        ),
    ),
]

widget_defaults = dict(
    font='CodeNewRoman Nerd Font',
    fontsize=16,
    padding=4,
)


extension_defaults = widget_defaults.copy()
