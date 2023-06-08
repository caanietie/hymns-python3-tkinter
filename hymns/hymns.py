import util
import tkinter
from tkinter import font


def hello_grace():
    print('Hello Grace')


def generic_container(tk_obj, text, width):
    _gen_con = tkinter.Frame(tk_obj, borderwidth=20)
    tkinter.Label(
        tk_obj, text=text, justify='left', width=width, anchor='w',
        font=font.Font(size=13)
    ).pack(padx=20, pady=5)
    return _gen_con


def display_hymn(id):
    if current_hymn.get() != id:
        current_hymn.set(id)
        _hymn = util.hashify_hymn(id)
        container.nametowidget('body').destroy()
        _widget = body_container(container)
        _display = tkinter.Frame(_widget)
        tkinter.Label(
            _display, text=_hymn['title'], anchor='w', width=45,
            font=font.Font(size=16)
        ).pack()
        for ind in range(len(_hymn['stanza'])):
            generic_container(_display, _hymn['stanza'][ind], 60).pack()
            if _hymn['chorus_type'] == 1:
                generic_container(_display, _hymn['chorus'], 57).pack()
            elif _hymn['chorus_type'] == 2:
                generic_container(_display, _hymn['chorus'][ind], 57).pack()
        _display.pack(anchor='e')
        _widget.pack(side='right', anchor='n', padx=10)


def get_hymn(id):
    return lambda: display_hymn(id)


def title_frame(tk_obj, id, title, cmd):
    _title_frame = tkinter.Frame(tk_obj)
    tkinter.Button(
        tk_obj, text=f'{id} {title}', width=40, command=cmd,
        font=font.Font(size=12)
    ).pack()
    return _title_frame


def title_container(tk_obj):
    _nav_var = nav_var.get()
    _titles_frame = tkinter.Frame(tk_obj, name='title')
    for id, title in util.get_titles(_nav_var, _nav_var+step-1):
        title_frame(_titles_frame, id, title, get_hymn(id)).pack()
    return _titles_frame


def nav_container(tk_obj):
    _title_nav = tkinter.Frame(tk_obj, name='nav')
    tkinter.Button(
        _title_nav, text='Previous', width=10,
        command=decrease_nav_var, font=font.Font(size=13)
    ).pack(side='left', padx=(0, 40))
    tkinter.Button(
        _title_nav, text='Next', width=10,
        command=increase_nav_var, font=font.Font(size=12)
    ).pack(side='right', padx=(40, 0))
    return _title_nav


def titles_nav_container(tk_obj):
    _nav = tkinter.Frame(tk_obj, name='title_nav')
    title_container(_nav).pack()
    nav_container(_nav).pack()
    return _nav


def body_container(tk_obj):
    _body_cont = tkinter.Frame(
        tk_obj, name='body', width=600, height=800,
        relief='raised', borderwidth=1
    )
    return _body_cont


def increase_nav_var():
    _nav_var = nav_var.get()
    if _nav_var + step < util.hymn_count:
        nav_var.set(_nav_var+step)
        container.nametowidget('title_nav').destroy()
        titles_nav_container(container).pack(side='left', anchor='n')


def decrease_nav_var():
    _nav_var = nav_var.get()
    if _nav_var - step > 0:
        nav_var.set(_nav_var-step)
        container.nametowidget('title_nav').destroy()
        titles_nav_container(container).pack(side='left', anchor='n')


step = 25
tk = tkinter.Tk(className='Hymns')
tk.resizable(width=False, height=False)
tk.minsize(width=600, height=500)
tk.title('Hymns')
nav_var = tkinter.IntVar()
nav_var.initialize(1)
current_hymn = tkinter.IntVar()
container = tkinter.Frame(tk, borderwidth=10)
titles_nav_container(container).pack(side='left', anchor='n')
body_container(container).pack(side='right', anchor='n', padx=10)
container.pack(padx=10, pady=10)
tk.mainloop()
