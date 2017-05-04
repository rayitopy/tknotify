#!/usr/bin/env python3
# Author: Daniel Martin Espinosa

from tkinter import font, Toplevel, CENTER, YES, BOTH, Label, Tk


class Notify(object):
    def __init__(self, **kws):
        """
        Attributes:
            title: the title message (in bold font)
            msg(opt):	the message
            expire_time(opt): how long the message will be showed (default 5000ms). Set to 0 to display forever.
            spacing(opt): the distance to screen border (default 20)
            justify(opt): The title and msg justify (default 'left')
            text_padding(opt): The padding of title or msg (default 50)
            alpha(opt): The alpha of windows (default 1.0)
        """
        title = kws.get("title")
        msg = kws.get("msg", False)
        expire_time = kws.get("expire_time", 5000)
        spacing = kws.get("spacing", 20)
        justify = kws.get("justify", CENTER)
        text_padding = kws.get("text_padding", 50)
        alpha = kws.get("alpha", 0.3)

        self.top = Toplevel()

        TITLE_FONT = font.Font(size=9, family="TkDefaultFont", weight=font.BOLD)
        MSG_FONT = font.Font(size=9, family="TkDefaultFont")
        self.top.withdraw()
        self.top.wm_attributes("-alpha", alpha)
        self.top.attributes("-topmost", 1)
        self.top.overrideredirect(True)
        self.top.config(bd=0, highlightthickness=0, bg="#2a2a2a")
        Label(self.top, text=title, fg="#fff", bd=0,
              highlightthickness=0, justify=justify, font=TITLE_FONT,
              bg=self.top["bg"]).pack(expand=YES, fill=BOTH)
        if msg:
            Label(self.top, text=msg, fg="#fff", bd=0,
                  highlightthickness=0, justify=justify, font=MSG_FONT,
                  bg=self.top["bg"]).pack(expand=YES, fill=BOTH)
        self.top.update_idletasks()
        SW = self.top.winfo_screenwidth()  # screen width
        WW = TITLE_FONT.measure(title)
        if msg and MSG_FONT.measure(msg) > WW:
            WW = MSG_FONT.measure(msg)
        WW += text_padding
        qt_lines_title = len(title.split("\n"))
        WH = qt_lines_title * TITLE_FONT.metrics().get("ascent")
        WH += (qt_lines_title - 1) * TITLE_FONT.metrics().get("linespace")
        if WH < 50:
            WH = 50
        self.top.geometry("%dx%d+%d+%d" % (WW, WH, SW - WW - spacing, spacing))
	if expire_time:
	    self.top.after(expire_time, top.destroy)
	    
    def show(self):
        self.top.deiconify()

    def destroy(self):
        self.top.destroy()
