from datetime import datetime, timezone
from math import floor

import timeago
from timeago import locales
from timeago.locales import en

from gui.gui import DisplayWindow







class PriceInformation(DisplayWindow):
    """Window to display prices of found items"""

    def __init__(self):
        super().__init__()
        self.data = None
        self.itemName = None

    def add_price_information(self, data, itemName):
        self.data = data
        self.itemName = itemName

    def add_components(self):
        """
        Assemble the simple pricing window. Will overhaul this to get a better GUI in a future update.
        """
        self.create_label_header2("装备名称  ", 0, 0, "E")
        self.create_label_header2(self.itemName, 1, 0, "E", 2)
        
        self.create_label_header("", 0, 1, "WE", 4)
        self.create_label_header("价格  ", 0, 1, "E")
        self.create_label_header("挂标时间 | 数量", 1, 1, "E", 2)

        counter = 1
        count = 0
        # dict{price: [count , time]}
        for price, values in self.data.items():
            date = datetime.now().replace(tzinfo=timezone.utc)
            now = values[1]
            time = timeago.format(now, date)
            count += values[0]
            if counter % 2:
                self.create_label_BG1("", 0, counter + 2, "WE", 3)
                self.create_label_BG1(price + "  ", 0, counter + 2, "E")
                self.create_label_BG1(
                    time + " (" + str(values[0]) + ")", 1, counter + 2, "E", 2
                )
            else:
                self.create_label_BG2("", 0, counter + 2, "WE", 3)
                self.create_label_BG2(price + "  ", 0, counter + 2, "E")
                self.create_label_BG2(
                    time + " (" + str(values[0]) + ")", 1, counter + 2, "E", 2
                )
            counter += 1
        counter = counter + 4
        self.data = None
        self.itemName = None


priceInformation = PriceInformation()
