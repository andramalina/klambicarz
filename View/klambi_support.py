#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    May 02, 2019 11:46:24 PM EEST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global che100
    che100 = tk.StringVar()

def backToAdminMainPage(p1, canvas1, canvas2):
    print('klambi_support.backToAdminMainPage')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas1)
    tk.Misc.lift(canvas2)
    sys.stdout.flush()

def backToUserMainPage(p1, canvas1, canvas2):
    print('klambi_support.backToUserMainPage')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas1)
    tk.Misc.lift(canvas2)
    sys.stdout.flush()

def changePakingStatus(p1, canvas1, canvas2):
    print('klambi_support.changePakingStatus')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas1)
    tk.Misc.lift(canvas2)
    sys.stdout.flush()

def checkAvailability(p1, canvas):
    print('klambi_support.checkAvailability')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas)
    sys.stdout.flush()

def checkParkings(p1, canvas):
    print('klambi_support.checkParkings')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas)
    sys.stdout.flush()

def confirmNewReservation(p1, canvas1, canvas2):
    print('klambi_support.confirmNewReservation')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas1)
    tk.Misc.lift(canvas2)
    sys.stdout.flush()

def login(p1, canvas):
    print('klambi_support.login')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas)
    sys.stdout.flush()

def logout(p1, canvas1, canvas2):
    print('klambi_support.logout')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas1)
    tk.Misc.lift(canvas2)
    sys.stdout.flush()

def manageParking(p1, canvas):
    print('klambi_support.manageParking')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas)
    sys.stdout.flush()

def newReservation(p1, canvas):
    print('klambi_support.newReservation')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas)
    sys.stdout.flush()

def profitByDay(p1):
    print('klambi_support.profitByDay')
    print('p1 = {0}'.format(p1))
    sys.stdout.flush()

def profitByMonth(p1):
    print('klambi_support.profitByMonth')
    print('p1 = {0}'.format(p1))
    sys.stdout.flush()

def profitByWeek(p1):
    print('klambi_support.profitByWeek')
    print('p1 = {0}'.format(p1))
    sys.stdout.flush()

def selectAdminDate(p1, canvas):
    print('klambi_support.selectAdminDate')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas)
    sys.stdout.flush()

def selectUserDate(p1, canvas):
    print('klambi_support.selectUserDate')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas)
    sys.stdout.flush()

def viewProfit(p1, canvas):
    print('klambi_support.viewProfit')
    print('p1 = {0}'.format(p1))
    tk.Misc.lift(canvas)
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import gui
    gui.vp_start_gui()




