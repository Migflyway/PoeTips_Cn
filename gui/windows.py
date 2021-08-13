from math import floor
import webbrowser
import pyperclip
from gui.gui import DisplayWindow




def open_trade_site():
    """Open up the web browser to the site we search

    :param rid: Unique ID given from the POST response
    :param league: League to search
    """
    if 'http' in pyperclip.paste():
        webbrowser.open(pyperclip.paste())

def send_item_info():
    """Open up the web browser to the site we search

    :param rid: Unique ID given from the POST response
    :param league: League to search
    """
    if 'http' in pyperclip.paste():
        webbrowser.open(pyperclip.paste())

class NotEnoughInformation(DisplayWindow):
    """Window to display when we determine there is not enough information to accurately price"""

    def __init__(self):
        super().__init__()

    def add_components(self):
        self.create_label_header("没有找到您想找到的装备信息，请手动查找", 0, 0, "WE")
        self.create_button('打开网站',open_trade_site, 1,'WE')


class SendInformation(DisplayWindow):
    """Window to display when we determine there is not enough information to accurately price"""

    def __init__(self):
        super().__init__()

    def add_components(self):
        self.create_label_header("程序当前无匹配，请发送装备信息到【开黑啦】", 0, 0, "WE")
        self.create_button('发送装备信息',send_item_info, 1,'WE')


class PriceInformation(DisplayWindow):
    """Window to display prices of found items"""

    def __init__(self):
        super().__init__()
        self.data = None
        self.itemName = None

    def add_price_information(self, data, itemName,itemimg,itemContent):
        self.data = data
        self.itemName = itemName
        self.itemimg = itemimg
        self.itemContent = itemContent

    def add_components(self):
        """
        Assemble the simple pricing window. Will overhaul this to get a better GUI in a future update.
        """
        self.create_label_header2("装备名称  ", 0, 0, "E")
        self.create_label_header2(self.itemName, 1, 0, "E", 2)
        
        self.create_icon_header(self.itemimg,self.itemContent, 0, 1)

        self.create_label_header("", 0, 2, "WE", 4)
        self.create_label_header("价格  ", 0, 2, "E")
        self.create_label_header("数量", 1, 2, "E", 2)

        counter = 2
        count = 0
        # dict{price: [count , time]}
        for price, values in self.data.items():
            count += values[0]
            if counter % 2:
                self.create_label_BG1("", 0, counter + 2, "WE", 3)
                self.create_label_BG1(price + "  ", 0, counter + 2, "E")
                self.create_label_BG1(
                    " (" + str(values[0]) + ")", 1, counter + 2, "E", 2
                )
            else:
                self.create_label_BG2("", 0, counter + 2, "WE", 3)
                self.create_label_BG2(price + "  ", 0, counter + 2, "E")
                self.create_label_BG2(
                    " (" + str(values[0]) + ")", 1, counter + 2, "E", 2
                )
            counter += 1
        counter = counter + 4
        self.create_button('打开网站',open_trade_site, counter+1,'WE')
        if count < 10:
            self.create_label_header(
                "查询结果小于10", 0, counter, "WE", 3
        )

        self.data = None
        self.itemName = None




priceInformation = PriceInformation()
notEnoughInformation = NotEnoughInformation()