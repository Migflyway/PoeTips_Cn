from os import rmdir
import tkinter
import time
from gui.gui import ActiveWindow, close_all_windows, close_display_windows



GUI_BG1 = '#1a1a1a'
GUI_BG2 = '#1f1f1f'
GUI_FONT = 'Courier'
GUI_FONT_SIZE = 12
GUI_FONT_COLOR = '#e6b800'

def pretty_xiushi(xiushici):
    # TODO: Add more currency types
    if "pseudo" in xiushici:
        xiushici = "综合"
    elif "ultimatum" in xiushici:
        xiushici = "致命贪婪"
    elif "delve" in xiushici:
        xiushici = "地心"
    elif "veiled" in xiushici:
        xiushici = "影匿"
    elif "crafted" in xiushici:
        xiushici = "工艺的"
    elif "enchant" in xiushici:
        xiushici = "附魔"
    elif "fractured" in xiushici:
        xiushici = '分裂的'
    elif "implicit" in xiushici:
        xiushici = '基底'
    elif "explicit" in xiushici:
        xiushici = '外延'
    elif 'monster' in xiushici:
        xiushici = '怪物'
    return xiushici


class AdvancedSearch(ActiveWindow):
    """Advanced Search Window"""

    def __init__(self):
        super().__init__()
        self.item = None
        self.selected = []
        self.searchable_mods = []
        self.entries = {}

    def add_item(self, item):
        self.item = item
        self.selected = []
        self.searchable_mods = []
        self.entries = {}

    def edit_item(self):
        nMods = []
        for mod in self.searchable_mods:
            if self.selected[mod.id].get():
                nMods.append(mod)
                min_val = self.entries_min[mod.id].get()
                max_val = self.entires_max[mod.id].get()
                self.entries[mod.id] = [min_val, max_val]
        
        # print(self.entries)
        self.item = nMods

    def search(self):
        try:
            self.edit_item()
            self.close()
        except Exception:
            self.close()

    def get_select(self):
        return self.item, self.entries

    def open_trade(self):
        pass

    def close_windows(self):
        self.item = None
        self.close()

    def add_components(self):
        """
        Add all of the components necessary for the GUI to display information.
        """

        masterFrame = tkinter.Frame(self.frame, bg=GUI_BG1)
        masterFrame.place(relwidth=1, relheight=1)

        self.create_label_header("词  缀", 0, 0, "WE", 6)
        # self.create_label_header(self.item.name, 0, 1, "WE", 6)
        j = 0
        self.selected = {}
        self.entries_min = {}
        self.entires_max = {}
        for mod in self.item:
            self.searchable_mods.append(mod)
            self.selected[mod.id] = tkinter.IntVar()

            # CheckButton
            bgColor = GUI_BG2 if j % 2 else GUI_BG1
            cb = tkinter.Checkbutton(
                self.frame,
                text="【"+pretty_xiushi(str(mod.classid))+"】"+mod.text,
                variable=self.selected[mod.id],
                bg=bgColor,
                fg=GUI_FONT_COLOR,
                activebackground=bgColor,
                activeforeground=GUI_FONT_COLOR,
                selectcolor = bgColor,
                highlightcolor = '#FF8000',
            )
            cb.select()
            cb.grid(row=j + 2, sticky="W", columnspan=3)
            cb.config(font=(GUI_FONT, GUI_FONT_SIZE))
            
            val = tkinter.StringVar()
            # val.set("Min")
            self.entries_min[mod.id] = tkinter.Entry(
                self.frame,
                bg=bgColor,
                fg=GUI_FONT_COLOR,
                width=5,
                textvariable=val,
                exportselection=0,
            )
            self.entries_min[mod.id].grid(row=j + 2, column=4, sticky="E", columnspan=1)
            val2 = tkinter.StringVar()
            # val2.set("Max")
            self.entires_max[mod.id] = tkinter.Entry(
                self.frame,
                bg=bgColor,
                fg=GUI_FONT_COLOR,
                width=5,
                textvariable=val2,
                exportselection=0,
            )
            self.entires_max[mod.id].grid(row=j + 2, column=5, sticky="E", columnspan=1)

            j += 1

        s = tkinter.Button(
            self.frame,
            text="搜索",
            command=self.search,
            bg=GUI_BG1,
            fg=GUI_FONT_COLOR,
        )
        s.grid(column=0, row=j + 2, columnspan=2, sticky="WE")
        s.config(font=(GUI_FONT, GUI_FONT_SIZE))
        s = tkinter.Button(
            self.frame,
            text="关闭",
            command=self.close_windows,
            bg=GUI_BG1,
            fg=GUI_FONT_COLOR,
        )
        s.grid(column=4, row=j + 2, columnspan=2, sticky="WE")
        s.config(font=(GUI_FONT, GUI_FONT_SIZE))


advancedSearch = AdvancedSearch()
