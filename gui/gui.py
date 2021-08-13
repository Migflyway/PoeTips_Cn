import io
import time
import tkinter
import traceback
import screeninfo
from urllib.request import urlopen
from PIL import Image, ImageTk
from gui.tips import ToolTip

USE_GUI = True
TIMEOUT_GUI = 4
GUI_BG1 = '#1a1a1a'
GUI_BG2 = '#1f1f1f'
GUI_FONT = 'Courier'
GUI_FONT_SIZE = 12
GUI_FONT_COLOR = '#e6b800'
GUI_HEADER_COLOR = '#0d0d0d'
GUI_HEADER_COLOR2 = '#BB5E00'
GUI_FONT_COLOR2 = '#FFDCB9'


components = []


def init_gui():
    if USE_GUI:
        pass
        # tkinter.Tk().withdraw()


def close_all_windows():
    if USE_GUI:
        for x in components:
                x.close()

def close_display_windows():
    if USE_GUI:
        for x in components:
            if not isinstance(x, ActiveWindow):
                x.close()


def check_timeout_gui():
    if USE_GUI:
        for x in components:
            if not isinstance(x, ActiveWindow):
                x.should_close()

if USE_GUI:

    class DisplayWindow:
        """Base window to display and information"""

        def __init__(self):
            self.frame = None
            self.created = False
            self.opened = time.time()  # When the window was created
            self.elapsed = 0  # Used to see how long the window was open

            components.append(self)

        def create_label_BG2(
            self, text, column=0, row=0, sticky="E", columnspan=1
        ):

            label = tkinter.Label(
                self.frame, text="", bg=GUI_BG2, fg=GUI_FONT_COLOR
            )
            label.grid(
                column=column, row=row, sticky="WE", columnspan=columnspan
            )

            label = tkinter.Label(
                self.frame, text=text, bg=GUI_BG2, fg=GUI_FONT_COLOR
            )
            label.grid(
                column=column, row=row, sticky=sticky, columnspan=columnspan
            )
            label.config(font=(GUI_FONT, GUI_FONT_SIZE))

        def create_label_BG1(
            self, text, column=0, row=0, sticky="E", columnspan=1
        ):
            label = tkinter.Label(
                self.frame, text="", bg=GUI_BG1, fg=GUI_FONT_COLOR
            )
            label.grid(
                column=column, row=row, sticky="WE", columnspan=columnspan
            )

            label = tkinter.Label(
                self.frame, text=text, bg=GUI_BG1, fg=GUI_FONT_COLOR
            )
            label.grid(
                column=column, row=row, sticky=sticky, columnspan=columnspan
            )
            label.config(font=(GUI_FONT, GUI_FONT_SIZE))

            

        def create_label_header(
            self, text, column=0, row=0, sticky="E", columnspan=1
        ):

            label = tkinter.Label(
                self.frame, text="", bg=GUI_HEADER_COLOR, fg=GUI_FONT_COLOR
            )
            label.grid(
                column=column, row=row, sticky="WE", columnspan=columnspan
            )

            label = tkinter.Label(
                self.frame, text=text, bg=GUI_HEADER_COLOR, fg=GUI_FONT_COLOR
            )
            label.grid(
                column=column, row=row, sticky=sticky, columnspan=columnspan
            )
            label.config(font=(GUI_FONT, GUI_FONT_SIZE))

        def create_icon_header(self, img_path,itemContent, column=0, row=0
        ):
            u = urlopen(img_path)
            my_picture = io.BytesIO(u.read())
            u.close()
            pil_img = Image.open(my_picture)
            self.tk_img = ImageTk.PhotoImage(pil_img)
            label = tkinter.Label(
                self.frame, image=self.tk_img,bg='#BEBEBE'
            )
            label.grid(
                column=column, row=row, sticky="WENS", columnspan=4, padx=5, pady=5
            )
            ToolTip(label,itemContent)

        def create_label_header2(
            self, text, column=0, row=0, sticky="E", columnspan=1
        ):

            label = tkinter.Label(
                self.frame, text="", bg=GUI_HEADER_COLOR2, fg=GUI_FONT_COLOR2
            )
            label.grid(
                column=column, row=row, sticky="WE", columnspan=columnspan
            )

            label = tkinter.Label(
                self.frame, text=text, bg=GUI_HEADER_COLOR2, fg=GUI_FONT_COLOR2
            )
            label.grid(
                column=column, row=row, sticky=sticky, columnspan=columnspan
            )
            label.config(font=(GUI_FONT, GUI_FONT_SIZE))
        
        def create_button(self, text, command, row=0, sticky="WE"):
            s = tkinter.Button(
                self.frame, text=text, command=command, bg=GUI_BG1, fg=GUI_FONT_COLOR,
            )
            s.grid(row=row, sticky=sticky, columnspan=3)
            s.config(font=(GUI_FONT, GUI_FONT_SIZE)
            )
        def prepare_window(self):
            frame = tkinter.Tk()
            # frame = tkinter.Toplevel()
            frame.wm_attributes("-topmost", 1)
            frame.overrideredirect(False)
            frame.option_add("*Font", "courier 12")
            frame.withdraw()
            frame.title("查询结果")
            frame.bind('<Escape>', lambda e: frame.destroy())
            self.frame = frame

        def close(self, event=None):
            if self.frame and self.created:
                self.frame.unbind("<Escape>")
                self.frame.withdraw()
                self.frame.destroy()
                self.frame = None
                self.created = False


        def should_close(self):
            if self.frame and self.created:
                self.elapsed = time.time() - self.opened
                if self.elapsed >= int(TIMEOUT_GUI):
                    self.elapsed = 0
                    self.close()

        def add_callbacks(self):
            pass

        def add_components(self):
            pass

        def create(self, x_cord, y_cord):
            self.prepare_window()
            self.add_components()
            self.finalize(x_cord, y_cord)

        def create_at_cursor(self):
            self.prepare_window()
            self.add_components()
            self.frame.deiconify()
            self.frame.update()
            # self.frame.bind("<FocusOut>", self.close)
            m_x = self.frame.winfo_pointerx()
            m_y = self.frame.winfo_pointery() + 10

            def get_monitor_from_coord(x, y):
                monitors = screeninfo.get_monitors()
                for m in reversed(monitors):
                    if m.x <= x <= m.width + m.x and m.y <= y <= m.height + m.y:
                        return m
                return monitors[0]

            # Get the screen which contains top
            width = 0
            height = 0
            try:
                current_screen = get_monitor_from_coord(
                    self.frame.winfo_x(), self.frame.winfo_y()
                )
                width = current_screen.width
                height = current_screen.height
            except screeninfo.common.ScreenInfoError:
                exception = traceback.format_exc()
                print("====== TRACEBACK =====")
                print(exception)
                self.close()
                return
            # Get the window's size
            root_w = self.frame.winfo_width()
            root_h = self.frame.winfo_height()

            if m_x + root_w >= width:
                m_x = width - root_w - 5

            if m_y + root_h >= height:
                m_y = height - root_h - 5

            self.finalize(m_x, m_y)

        def create_at_cursor_left(self):
            self.prepare_window()
            self.add_components()
            self.frame.deiconify()
            self.frame.update()
            m_x = self.frame.winfo_pointerx()
            m_y = self.frame.winfo_pointery() + 10

            def get_monitor_from_coord(x, y):
                monitors = screeninfo.get_monitors()
                for m in reversed(monitors):
                    if m.x <= x <= m.width + m.x and m.y <= y <= m.height + m.y:
                        return m
                return monitors[0]

            # Get the screen which contains top
            width = 0
            height = 0
            try:
                current_screen = get_monitor_from_coord(
                    self.frame.winfo_x(), self.frame.winfo_y()
                )
                width = current_screen.width
                height = current_screen.height
            except screeninfo.common.ScreenInfoError:
                exception = traceback.format_exc()
                print("====== TRACEBACK =====")
                print(exception)
                self.close()
                return
            # Get the window size
            root_w = self.frame.winfo_width()
            root_h = self.frame.winfo_height()

            m_x -= root_w + 10

            if m_x + root_w >= width:
                m_x = width - root_w - 5

            if m_y + root_h >= height:
                m_y = height - root_h - 5

            self.finalize(m_x, m_y)

        def finalize(self, x_cord, y_cord):
            self.frame.deiconify()
            self.frame.lift()
            self.frame.focus_force()
            self.frame.geometry(f"+{x_cord}+{y_cord}")
            self.frame.resizable(False, False)
            self.has_focus = True
            self.frame.update()
            self.add_callbacks()
            self.opened = time.time()
            self.created = True
            # self.should_close()
            self.frame.mainloop()


    class ActiveWindow(DisplayWindow):
        """Base window for setting up the overlay"""

        def __init__(self):
            self.frame = None
            self.opened = time.time()  # When the window was created
            self.elapsed = 0  # Used to see how long the window was open
            self.created = False
            components.append(self)

        def close(self, event=None):
            if self.frame:
                self.frame.unbind("<Escape>")
                self.frame.update()
                self.frame.withdraw()
                self.frame.quit()
                self.frame.destroy()
                self.frame = None
                self.created = False

        def run(self):
            pass
            # self.frame.mainloop()

        def create_at_cursor(self):
            super().create_at_cursor()
            self.run()

else:

    class DisplayWindow:
        def __init__(self):
            pass
        def create_label_BG2(
            self, text, column=0, row=0, sticky="E", columnspan=1
        ):
            pass
        def create_label_BG1(
            self, text, column=0, row=0, sticky="E", columnspan=1
        ):
            pass
        def create_label_header(
            self, text, column=0, row=0, sticky="E", columnspan=1
        ):
            pass
        def create_label_header2(
            self, text, column=0, row=0, sticky="E", columnspan=1
        ):        
            pass
        def prepare_window(self):
            pass
        def close(self, event=None):
            pass
        def should_close(self):
            pass
        def add_callbacks(self):
            pass
        def add_components(self):
            pass
        def create(self, x_cord, y_cord):
            pass
        def create_at_cursor(self):
            pass
        def finalize(self, x_cord, y_cord):
            pass


    class ActiveWindow(DisplayWindow):
        """Base window for setting up the overlay"""

        def close(self, event=None):
            pass
        def run(self):
            pass
        def create_at_cursor(self):
            pass
        def lost_focus(self, event=None):
            pass
        def add_callbacks(self):
            pass
