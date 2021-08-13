from enum import Flag
from os import PathLike, link
import time
from tkinter.constants import NO
from typing_extensions import IntVar
# from tkinter.constants import FALSE
import pyperclip
import requests
import json
import re
import tkinter as tk
from tkinter import ttk
import webbrowser
from datetime import datetime, timezone
from itemModifier import ItemModifier, ItemModifierType
from gui.windows import (priceInformation, notEnoughInformation)
from gui.advSearch import advancedSearch
from gui.tips import ToolTip
league = 'S15赛季'
leagueTupe = ['选择服务器更新赛季']





try:
    with open('mods.json', 'r', encoding='utf8') as fp:
        d_mods = json.load(fp)
        print('读取mods文件完成：', type(d_mods))
except:
    print("缺少mods文件，请重新下载")


try:
    update_exe = requests.get("https://api.github.com/repos/Migflyway/PoeTips_Cn/releases/latest")
    print("当前版本号为："+update_exe.json()["tag_name"])
except:
    print("获取版本号异常，请手动确定")
    
print("下载地址1: https://github.com/Migflyway/PoeTips_Cn/releases/")
print('下载地址2: https://wwr.lanzoui.com/b02i8ypra  密码:grp6')

jewl_enchant = [
    "斧类攻击造成的击中和异常状态伤害提高12%",
    "长杖攻击造成的击中和异常状态伤害提高12%",
    "爪类攻击造成的击中和异常状态伤害提高12%",
    "弓类的伤害提高12%",
    "法杖攻击造成的击中和异常状态伤害提高12%",
    "双手武器的攻击伤害提高12%",
    "双持武器时，攻击伤害提高12%",
    "持盾牌时造成的攻击伤害提高12%",
    "攻击伤害提高10%",
    "法术伤害提高10%",
    "元素伤害提高10%",
    "物理伤害提高12%",
    "火焰伤害提高12%",
    "闪电伤害提高12%",
    "冰霜伤害提高12%",
    "混沌伤害提高12%",
    "召唤生物的伤害提高10%",
    "+4%火焰持续伤害加成",
    "+4%混沌持续伤害加成",
    "+4%物理持续伤害加成",
    "+4%冰霜持续伤害加成",
    "+4%持续伤害加成",
    "非伤害型异常状态效果提高10%",
    "你技能的非诅咒类光环效果提高3%",
    "你所施放诅咒的效果提高3%",
    "受捷影响时，伤害提高10%",
    "你受捷影响时，召唤生物的伤害提高10%",
    "增助攻击的伤害提高20%",
    "攻击与法术暴击率提高15%",
    "召唤生物的最大生命提高12%",
    "范围伤害提高10%",
    "投射物伤害提高10%",
    "陷阱伤害提高12%",
    "地雷伤害提高12%",
    "图腾伤害提高12%",
    "烙印伤害提高12%",
    "持续吟唱技能伤害提高12%",
    "药剂效果的持续时间延长6%",
    "药剂回复的生命提高10%",
    "药剂回复的魔力提高10%",
    "最大生命提高4%",
    "最大能量护盾提高6%",
    "最大魔力提高6%",
    "护甲提高15%",
    "闪避值提高15%",
    "1%攻击伤害格挡率",
    "1%法术伤害格挡几率",
    "+15%火焰抗性",
    "+15%冰霜抗性",
    "+15%闪电抗性",
    "+12%混沌抗性",
    "1%的几率躲避攻击击中",
]

map_liejie = [
    "该地图被【裂界守卫：奴役】占据 (implicit)",
    "该地图被【裂界守卫：寂灭】占据 (implicit)",
    "该地图被【裂界守卫：约束】占据 (implicit)",
    "该地图被【裂界守卫：净世】占据 (implicit)",
]


all_item_list = [
    "爪",
    "匕首",
    "法杖",
    "单手剑",
    "细剑",
    "单手斧",
    "单手锤",
    "短杖",
    "符文匕首",
    "弓",
    "长杖",
    "双手剑",
    "双手斧",
    "双手锤",
    "战杖",
    "盾",
    "箭袋", 
    "项链",
    "戒指",
    "腰带",
    "饰品", 
    "手套",
    "鞋子",
    "胸甲",
    "头部",
]

weapon_list = [
    "爪",
    "匕首",
    "法杖",
    "单手剑",
    "细剑",
    "单手斧",
    "单手锤",
    "短杖",
    "符文匕首",
    "弓",
    "长杖",
    "双手剑",
    "双手斧",
    "双手锤",
    "战杖",
    "盾",
    "箭袋",
]

ring_list = [
    "项链",
    "戒指",
    "腰带",
    "饰品",
]

armor_list = [
    "手套",
    "鞋子",
    "胸甲",
    "头部",
]
def getNum(str):
    return str.split(': ')[1]


def mountNum(str):
    return str.split(': ')[1].split('/')[0]


def cleanWord(str):
    return str.replace('精良的', '').replace('菌潮', '').replace('忆境', '').strip()


def removeEnchant(str):
    return re.sub('\[(.*?)\]|\(.*?\)|增加的小天赋获得：|[/▲\s]','',str)


def getAmount(str):
    str = str.split('/')[0]
    return int(str[5:])

def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

def remove_chinese(str):
    if is_contains_chinese(str):
        str = str.replace('(辅)','')
        return re.findall('[\(](.*?)[\)]',str)[0].replace('(','').replace(')','')
    else:
        return str

def remove_english(str):
    return re.sub('[\(](.*?)[\)]','',str)

def pretty_currency(curr):
    currency = curr
    # TODO: Add more currency types
    if "mir" in currency:
        currency = "镜子"
    elif "exa" in currency:
        currency = "崇高石"
    elif "chaos" in currency:
        currency = "混沌石"
    elif "alch" in currency:
        currency = "点金石"
    elif "alt" in currency:
        currency = "改造石"
    elif "fuse" in currency:
        currency = "链接石"
    elif "divine" in currency:
        currency = '神圣石'
    elif "fusing" in currency:
        currency = '链接石'
    elif "scour" in currency:
        currency = '重铸石'
    return currency


def getNameAndType(clipboard):
    if clipboard.startswith('物品类别:') == False:
        return None, None
    try:
        if clipboard.splitlines()[3].startswith('--------'):
            return None, clipboard.splitlines()[2]
        else:
            return clipboard.splitlines()[2], clipboard.splitlines()[3]
    except:
        return None


def find_special_content(str, keyword):
    for content in str:
        if content.find(keyword) != -1:
            return content


def get_socks_link(str):
    str = str.replace('插槽: ', '')
    sockets = str.lower()
    r_sockets = sockets.count("r")
    b_sockets = sockets.count("b")
    g_sockets = sockets.count("g")
    w_sockets = sockets.count("w")
    a_sockets = sockets.count("a")

    links = 0
    counter = 0
    for c in sockets:
        if c == " ":
            if counter > links:
                links = counter
                counter = 0
        elif c == "-":
            counter += 1
    if counter > links:
        links = counter
    links = links + 1
    sockets = r_sockets + b_sockets + g_sockets + w_sockets + a_sockets
    print(sockets, links)
    return sockets, links


mod_list = []
mod_list_org = []
mod_list_dict_id = {}
mod_list_dict_text = {}

# contains all mods there exist more than 1 off
dup_mod_list_text = {}


def build_from_json(blob: dict) -> ItemModifier:
    """From the stats API construct ItemModifier objects for given entry

    :param blob: A modifier found in the stats API
    :return: ItemModifier object for the given modifier
    """
    if "option" in blob:
        # If the given modifier has an option section, add it.
        # This is necessary for the "Allocates #" modifier that
        # is present on Annointed items
        if "options" in blob["option"]:
            options = {}
            for i in blob["option"]["options"]:
                options[i["text"]] = i["id"]

            t = blob["text"].rstrip()
            t = re.sub(r'(\d+)','#',t)
            t = t.rstrip()
            return ItemModifier(
                id=blob["id"],
                text=t,
                options=options,
                classid = blob["type"].lower(),
                type=ItemModifierType(blob["type"].lower()),
            )

    t = blob["text"].rstrip()
    t = re.sub(r'(\d+)','#',t)
    t = t.rstrip()

    return ItemModifier(
        id=blob["id"],
        text=t,
        classid = blob["type"].lower(),
        type=ItemModifierType(blob["type"].lower()),
        options={},
    )


def build_from_json_org(blob: dict) -> ItemModifier:
    """From the stats API construct ItemModifier objects for given entry

    :param blob: A modifier found in the stats API
    :return: ItemModifier object for the given modifier
    """
    if "option" in blob:
        # If the given modifier has an option section, add it.
        # This is necessary for the "Allocates #" modifier that
        # is present on Annointed items
        if "options" in blob["option"]:
            options = {}
            for i in blob["option"]["options"]:
                options[i["text"]] = i["id"]

            t = blob["text"].rstrip()
            # t = re.sub(r'(\d+)','#',t)
            t = t.rstrip()
            return ItemModifier(
                id=blob["id"],
                text=t,
                options=options,
                classid = blob["type"].lower(),
                type=ItemModifierType(blob["type"].lower()),

            )

    t = blob["text"].rstrip()
    # t = re.sub(r'(\d+)','#',t)
    t = t.rstrip()

    return ItemModifier(
        id=blob["id"],
        text=t,
        classid = blob["type"].lower(),
        type=ItemModifierType(blob["type"].lower()),
        options={},
    )


def get_item_modifiers() -> tuple:
    """Query the stats API to retrieve all current stats

    :return: tuple of all available modifiers
    """
    global mod_list
    global mod_list_org
    if mod_list:
        return mod_list
    else:
        json_blob = requests.get("http://poe.game.qq.com/api/trade/data/stats").json()
        for modType in json_blob["result"]:
            for mod in modType["entries"]:
                mod_list.append(build_from_json(mod))
                mod_list_org.append(build_from_json_org(mod))

        print(f"[*] Loaded {len(mod_list)} item mods.")
        return mod_list

        # try:
        #     for modType in json_blob["result"]:
        #         for mod in modType["entries"]:
        #             mod_list.append(build_from_json(mod))

        #     print(f"[*] Loaded {len(mod_list)} item mods.")
        #     return mod_list
        # except Exception:
        #     print(f"[!] Something went wrong getting item mods!")
        #     return None

def get_item_modifiers_org() -> tuple:
    """Query the stats API to retrieve all current stats

    :return: tuple of all available modifiers
    """
    global mod_list_org
    if mod_list_org:
        return mod_list_org
    else:
        json_blob = requests.get("http://poe.game.qq.com/api/trade/data/stats").json()
        for modType in json_blob["result"]:
            for mod in modType["entries"]:
                mod_list_org.append(build_from_json_org(mod))

        print(f"[*] Loaded {len(mod_list_org)} item mods.")
        return mod_list_org

def get_item_modifiers_by_id(element: str) -> ItemModifier:
    """Search all available ItemModifier objects by their id attribute.

    If this is the first time being used, construct a cache so that we
    can search faster on subsequent versions

    :param element: id of the requested ItemModifier
    :return: ItemModifier that matches
    """
    global mod_list_dict_id
    if len(mod_list_dict_id) == 0:
        item_modifiers = get_item_modifiers_org()
        mod_list_dict_id = {e.id: e for e in item_modifiers}
    if element in mod_list_dict_id:
        return mod_list_dict_id[element]


def get_item_modifiers_by_text(element: tuple) -> ItemModifier:
    """Search all available ItemModifier objects by their text attribute.

    If this is the first time being used, construct a cache so that we
    can search faster on subsequent versions

    :param element: (text, type) of the requested ItemModifier
    :return: ItemModifier that matches
    """
    global mod_list_dict_text
    global dup_mod_list_text
    if len(mod_list_dict_text) == 0:
        item_modifiers = get_item_modifiers()
        found = {}
        for mod in item_modifiers:
            if "Allocates # (Additional)" in mod.text:  # Gives no results ATM
                continue
            if (mod.text, mod.type) in mod_list_dict_text:
                if not (mod.text, mod.type) in found:
                    found[(mod.text, mod.type)] = {}
                found[(mod.text, mod.type)][mod.id] = ""
                found[(mod.text, mod.type)][mod_list_dict_text[(mod.text, mod.type)].id] = ""
            mod_list_dict_text[(mod.text, mod.type)] = mod

        for key, value in found.items():
            dup_mod_list_text[key] = ""

    if element in mod_list_dict_text:
        return get_item_modifiers_by_id(mod_list_dict_text[element].id)


prev_mod = ""

class ModInfo:
    def __init__(self, mod, m_min, m_max, option, can_reduce=True):
        self.mod = mod
        self.min = m_min
        self.max = m_max
        self.option = option
        self.can_reduce = can_reduce

def parse_mod(mod_text: str, category: str):
    """Given the text of the mod, find the appropriate ItemModifier object

    :param mod_text: Text of the mod
    :param mod_values: Value of the referenced mod
    :param category: Specific category of mods to check

    """
    global prev_mod

    mod = None
    mod_type = ItemModifierType.EXPLICIT

    mod_text = mod_text.rstrip()


    if mod_text.endswith("(implicit)"):
        mod_text = mod_text[:-11]
        mod_type = ItemModifierType.IMPLICIT
    elif mod_text.endswith("(crafted)"):
        mod_text = mod_text[:-10]
        mod_type = ItemModifierType.CRAFTED
    elif mod_text.endswith("(enchant)"):
        mod_text = mod_text.replace(" (enchant)", "")
        mod_type = ItemModifierType.ENCHANT
    elif mod_text.endswith('(fractured)'):
        mod_text = mod_text.replace(" (fractured)", "")
        mod_type = ItemModifierType.FRACTURED        

    if category in weapon_list:
        if (
            "附加 # - #" in mod_text
            and "法术附加" not in mod_text
            or "命中值" in mod_text
            or "攻击速度提高" in mod_text
            or '物理攻击伤害的' in mod_text
        ):
            mod = get_item_modifiers_by_text((mod_text + " (区域)", mod_type))
        elif (
            "几率使目标中毒" in mod_text and '召唤' not in mod_text and '攻击' not in mod_text
        ):
            mod = get_item_modifiers_by_text((mod_text + " (区域)", mod_type))

    if category in armor_list:
        if (
            "护甲" in mod_text
            or "闪避值" in mod_text
            or "能量护盾" in mod_text
        ):
            mod = get_item_modifiers_by_text((mod_text + " (区域)", mod_type))

    if not mod and mod_type == ItemModifierType.CRAFTED:
        mod = get_item_modifiers_by_text((mod_text, ItemModifierType.PSEUDO))

    if not mod:
        mod = get_item_modifiers_by_text((mod_text, mod_type))

    if not mod:
        mod = get_item_modifiers_by_text((mod_text + " (区域)", mod_type))

    if not mod:
        mod = get_item_modifiers_by_text((mod_text, ItemModifierType.ENCHANT))

    try:
        if not mod:
            if "降低" in mod_text:
                mod_text = mod_text.replace("降低", "提高")
            elif "提高" in mod_text:
                mod_text = mod_text.replace("提高", "降低")
            mod = get_item_modifiers_by_text((mod_text, mod_type))
    except ValueError:
        pass
    if not mod:
        return None


    prev_mod = mod_text
    # m = ModInfo(mod, m_min, m_max, option, can_reduce)
    return mod

def read_info(text, category):
    mods = []
    regions = text.split("--------\r\n")

    for i in regions:
        for line in i.splitlines():
            print(line)
            mod_text = re.sub(r"[+-]?\d+\.?\d?\d?", "#", line)
            mod = None
            if not mod_text:
                mod_text = line
            mod = parse_mod(mod_text, category)
            if mod:
                mods.append(mod)
            else:
                pass
                # print(f"Unable to find mod: {line}")
    return mods







def loadpayLoad(clipboard):
    payload = None
    if clipboard.startswith('物品类别:') == False:
        return
    if clipboard.find('未鉴定') != -1:
        print("请先鉴定您的物品")
        return None
    splitedstr = clipboard.split('--------\r\n')
    if len(splitedstr) < 2:
        return None
    if language_choice.get()=='国服':
        itemClass = splitedstr[0].splitlines()[0].split(': ')[1]
        itemRairty = splitedstr[0].splitlines()[1].split(': ')[1]
    else:
        itemClass = splitedstr[0].splitlines()[0].split(': ')[1]
        itemClass = remove_english(itemClass)
        itemRairty = splitedstr[0].splitlines()[1].split(': ')[1]        
    print(itemClass, itemRairty)
    itemName = ''
    itemBaseType = ''
    #传奇优先一切
    if itemRairty == '传奇':
        if itemClass != '灾变样本':
            if language_choice.get()=='国服':
                itemName = splitedstr[0].splitlines()[2]
                itemBaseType = cleanWord(splitedstr[0].splitlines()[3])
            else:
                itemName = remove_chinese(splitedstr[0].splitlines()[2])
                itemBaseType = remove_chinese(cleanWord(splitedstr[0].splitlines()[3]))
            print(itemBaseType,itemName)                
            if itemClass == '异界地图':
                mapTier = int(getNum(splitedstr[1].splitlines()[0]))
                if language_choice.get()=='国服':
                    itemName = splitedstr[0].splitlines()[2]
                    itemBaseType = cleanWord(splitedstr[0].splitlines()[3])
                else:
                    itemName = remove_chinese(splitedstr[0].splitlines()[2])
                    itemBaseType = remove_chinese(cleanWord(splitedstr[0].splitlines()[3]))                   
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "name": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "type": {
                            "option": itemBaseType,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "map_filters": {
                                "disabled": False,
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            },
                            "type_filters": {
                                "disabled": False,
                                "filters": {
                                    "rarity": {
                                        "option": "unique"
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
            else:
                payload = {
                    "query": {
                        "status": {
                            "option": "any"
                        },
                        "name": itemName,
                        "type": itemBaseType,
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "socket_filters": {
                                "filters": {
                                }
                            },
                            "trade_filters": {
                                "filters": {
                                    "indexed": {
                                        "option": "1day"
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
                if clipboard.find('插槽') != -1:
                    sockets, links = get_socks_link(find_special_content(splitedstr,'插槽'))
                    if sockets == 6 or links >= 5:
                        if sockets == 6:
                            payload["query"]["filters"]["socket_filters"]["filters"]["sockets"] = {"min": 6}
                        if links >= 5:
                            payload["query"]["filters"]["socket_filters"]["filters"]["links"] = {"min": links}
                        print(payload)

    elif itemRairty=='稀有':
        if itemClass in all_item_list:
            if language_choice.get()=='国服':
                itemBaseType = cleanWord(splitedstr[0].splitlines()[3])
            else:
                itemBaseType = remove_chinese(cleanWord(splitedstr[0].splitlines()[3]))
            filt = []
            m = read_info(clipboard,itemClass)
            advancedSearch.add_item(m)
            advancedSearch.create_at_cursor()
            selected_m,selected_value = advancedSearch.get_select()

            if selected_m==None: return None
            value_t = {}
            for t in selected_m:
                if selected_value[t.id][0]!='':
                    value_t['min'] = selected_value[t.id][0]
                if selected_value[t.id][1] !='':
                    value_t['max'] = selected_value[t.id][1]
                filt.append({
                    "id": t.id,
                    'value':value_t,
                    "disabled": False
                })
            payload = {
                        "query": {
                            "status": {
                                "option": "online"
                            },
                            "type": itemBaseType,
                            "stats": [{
                                "type": "and",
                                "filters": []
                            }, {
                                "filters": filt,
                                "type": "and"
                            }],
                            "filters": {
                                "type_filters": {
                                    "filters": {
                                        "rarity": {
                                            "option": "rare"
                                        }
                                    }
                                }
                            }
                        },
                        "sort": {
                            "price": "asc"
                        }
                    }
            
            # print(payload)        

            
    if itemClass == '地图碎片':
        if language_choice.get()==('国服'):
            itemName = splitedstr[0].splitlines()[2]
        else:
            itemName = remove_chinese(splitedstr[0].splitlines()[2])
        payload = {
            "query": {
                "status": {
                    "option": "online"
                },
                "type": itemName,
                "stats": [{
                    "type": "and",
                    "filters": []
                }]
            },
            "filters": {
                "trade_filters": {
                    "filters": {
                        "indexed": {
                            "option": "1day"
                        }
                    },
                    "disabled": False
                }
            },
            "sort": {
                "price": "asc"
            }
        }
    elif itemClass == '命运卡':
        print("注意命运卡有重复名称，请手动确定")
        if language_choice.get()==('国服'):
            itemName = splitedstr[0].splitlines()[2]
        else:
            itemName = remove_chinese(splitedstr[0].splitlines()[2])       
        itemMount = getAmount(splitedstr[1].splitlines()[0])
        payload = {
            "query": {
                "status": {
                    "option": "online"
                },
                "type": itemName,
                "stats": [{
                    "type": "and",
                    "filters": [],
                    "disabled": True
                }],
                "filters": {
                    "misc_filters": {
                        "filters": {
                            "stack_size": {
                                "min": itemMount,
                                "max": itemMount
                            }
                        }
                    }
                }
            },
            "sort": {
                "price": "asc"
            }
        }
        # payload = {"query":{"status":{"option":"online"},"type":itemName,"stats":[{"type":"and","filters":[]}],"filters":{"misc_filters":{"filters":{"stack_size":{"max":itemMount}}}}},"sort":{"price":"asc"}}
    elif itemClass == '可堆叠通货':
        if language_choice.get()==('国服'):
            itemName = splitedstr[0].splitlines()[2]
        else:
            itemName = remove_chinese(splitedstr[0].splitlines()[2])

        if '右键点击后赋予你的角色预言之力' in clipboard:
            itemBaseType = '预言'
            itemMount = 1
        else:
            itemMount = getAmount(splitedstr[1].splitlines()[0])

        if itemBaseType=='预言':
            payload = {"query":{"status":{"option":"online"},"name":itemName,"type":itemBaseType,"stats":[{"type":"and","filters":[]}],"filters":{"misc_filters":{"filters":{"stack_size":{"min":itemMount,"max":itemMount}}}}},"sort":{"price":"asc"}}
        else:   
            if itemName == '崇高石':
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": "崇高石",
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "misc_filters": {
                                "filters": {
                                    "stack_size": {
                                        "min": itemMount,
                                        "max": itemMount
                                    }
                                }
                            },
                            "trade_filters": {
                                "filters": {
                                    "price": {
                                        "option": "chaos"
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
            else:
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": itemName,
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "misc_filters": {
                                "filters": {
                                    "stack_size": {
                                        "min": itemMount,
                                        "max": itemMount
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
    elif itemClass == '异界地图':

        mapTier = int(getNum(splitedstr[1].splitlines()[0]))

        if itemRairty == '稀有':
            if language_choice.get()==('国服'):
                itemName = splitedstr[0].splitlines()[3]
            else:
                itemName = remove_chinese(splitedstr[0].splitlines()[3])
            print(itemName)           
            if clipboard.find('区域被菌潮感染') != -1:
                print('区域被菌潮感染')
                itemName = splitedstr[0].splitlines()[2].replace("菌潮 ", '')
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_blighted": {
                                        "option": "true"
                                    },
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }

            elif clipboard.find('被裂界者影响') != -1:
                print('被裂界者影响')
                keyCont = find_special_content(splitedstr,
                                               '该区域被裂界者影响').splitlines()[1]
                print(keyCont)
                liejie_id = map_liejie.index(keyCont) + 1
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }, {
                            "filters": [{
                                "id": "implicit.stat_1792283443",
                                "value": {
                                    "option": "2"
                                },
                                "disabled": False
                            }, {
                                "id": "implicit.stat_3624393862",
                                "value": {
                                    "option": liejie_id
                                },
                                "disabled": False
                            }],
                            "type":
                            "and"
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
            elif clipboard.find('该区域被塑界者影响') != -1:
                print('该区域被塑界者影响')
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": [],
                            "disabled": False
                        }, {
                            "filters": [{
                                "id": "implicit.stat_1792283443",
                                "value": {
                                    "option": "1"
                                },
                                "disabled": False
                            }],
                            "type":
                            "and"
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
            else:
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "map_filters": {
                                "disabled": False,
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            },
                            "type_filters": {
                                "filters": {
                                    "rarity": {
                                        "option": "nonunique"
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }

        elif itemRairty == '魔法':
            if language_choice.get()==('国服'):
                itemName = splitedstr[0].splitlines()[2]
            else:
                itemName = remove_chinese(splitedstr[0].splitlines()[2])
            if clipboard.find('区域被菌潮感染') != -1:
                print('区域被菌潮感染')
                itemName = splitedstr[0].splitlines()[2].replace("菌潮 ", '')
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_blighted": {
                                        "option": "true"
                                    },
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }

            elif clipboard.find('被裂界者影响') != -1:
                print('被裂界者影响')
                keyCont = find_special_content(splitedstr,
                                               '该区域被裂界者影响').splitlines()[1]
                print(keyCont)
                liejie_id = map_liejie.index(keyCont) + 1
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }, {
                            "filters": [{
                                "id": "implicit.stat_1792283443",
                                "value": {
                                    "option": "2"
                                },
                                "disabled": False
                            }, {
                                "id": "implicit.stat_3624393862",
                                "value": {
                                    "option": liejie_id
                                },
                                "disabled": False
                            }],
                            "type":
                            "and"
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
            elif clipboard.find('该区域被塑界者影响') != -1:
                print('该区域被塑界者影响')
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": [],
                            "disabled": False
                        }, {
                            "filters": [{
                                "id": "implicit.stat_1792283443",
                                "value": {
                                    "option": "1"
                                },
                                "disabled": False
                            }],
                            "type":
                            "and"
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
            else:
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "map_filters": {
                                "disabled": False,
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            },
                            "type_filters": {
                                "filters": {
                                    "rarity": {
                                        "option": "nonunique"
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }

        elif itemRairty == '普通':
            if language_choice.get()==('国服'):
                itemName = cleanWord(splitedstr[0].splitlines()[2])
            else:
                itemName = remove_chinese(cleanWord(splitedstr[0].splitlines()[2]))
            if clipboard.find('区域被菌潮感染') != -1:
                print('区域被菌潮感染')
                itemName = splitedstr[0].splitlines()[2].replace("菌潮 ", '')
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_blighted": {
                                        "option": "true"
                                    },
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }

            elif clipboard.find('被裂界者影响') != -1:
                print('被裂界者影响')
                keyCont = find_special_content(splitedstr,
                                               '该区域被裂界者影响').splitlines()[1]
                print(keyCont)
                liejie_id = map_liejie.index(keyCont) + 1
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }, {
                            "filters": [{
                                "id": "implicit.stat_1792283443",
                                "value": {
                                    "option": "2"
                                },
                                "disabled": False
                            }, {
                                "id": "implicit.stat_3624393862",
                                "value": {
                                    "option": liejie_id
                                },
                                "disabled": False
                            }],
                            "type":
                            "and"
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
            elif clipboard.find('该区域被塑界者影响') != -1:
                print('该区域被塑界者影响')
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": [],
                            "disabled": False
                        }, {
                            "filters": [{
                                "id": "implicit.stat_1792283443",
                                "value": {
                                    "option": "1"
                                },
                                "disabled": False
                            }],
                            "type":
                            "and"
                        }],
                        "filters": {
                            "map_filters": {
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
            else:
                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": {
                            "option": itemName,
                            "discriminator": "warfortheatlas"
                        },
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }],
                        "filters": {
                            "map_filters": {
                                "disabled": False,
                                "filters": {
                                    "map_tier": {
                                        "min": mapTier,
                                        "max": mapTier
                                    }
                                }
                            },
                            "type_filters": {
                                "filters": {
                                    "rarity": {
                                        "option": "nonunique"
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
        print(itemName,mapTier)
    elif itemClass == '珠宝':
        if clipboard.find('星团珠宝') != -1:
            jewl = {'skillnum': 4, 'hole': 1, 'enchant': 1}
            if itemRairty == '稀有':
                if language_choice.get()=='国服':
                    itemName = splitedstr[0].splitlines()[3]
                else:
                    itemName = remove_chinese(splitedstr[0].splitlines()[3])
            elif itemRairty == '魔法':
                if language_choice.get()=='国服':
                    if splitedstr[0].splitlines()[2].find('的') != -1:
                        itemName = splitedstr[0].splitlines()[2].split('的')[1]
                    elif splitedstr[0].splitlines()[2].find('之') != -1:
                        itemName = splitedstr[0].splitlines()[2].split('之')[1]
                else:
                    itemName = remove_chinese(splitedstr[0].splitlines()[2])
            elif itemRairty == '普通':
                if language_choice.get()=='国服':
                    itemName = cleanWord(splitedstr[0].splitlines()[2])
                else:
                    itemName = remove_chinese(splitedstr[0].splitlines()[2])
            elif itemRairty == '传奇':
                if language_choice.get()=='国服':
                    itemName = splitedstr[0].splitlines()[2]
                    itemBaseType = cleanWord(splitedstr[0].splitlines()[3])
                else:
                    itemName = splitedstr[0].splitlines()[2]
                    itemBaseType = remove_chinese(cleanWord(splitedstr[0].splitlines()[3]))


            if itemRairty == '传奇':
                if itemBaseType == '中型星团珠宝' or itemBaseType=='Medium Cluster Jewel':
                    jewl['skillnum'] = re.findall(
                        r"\d+\.?\d*", splitedstr[3].splitlines()[0])[0]
                    filt = [{
                        "id": "explicit.stat_3086156145",
                        "value": {
                            "min": jewl['skillnum'],
                            "max": jewl['skillnum']
                        },
                        "disabled": False
                    }, {
                        "id": "explicit.stat_2557943734",
                        "value": {},
                        "disabled": False
                    }]
                    skilllist = splitedstr[3].splitlines()
                    for each_contant in skilllist:
                        if each_contant.find(r'其中 1 个增加的天赋为') != -1:
                            for result_content in d_mods['result']:
                                for k, v in result_content.items():
                                    if isinstance(v, list):
                                        for i in v:
                                            if i['text'] == each_contant:
                                                print(i['id'])
                                                filt.append({
                                                    "id": i['id'],
                                                    "value": {},
                                                    "disabled": False
                                                })
                    payload = {
                        "query": {
                            "status": {
                                "option": "online"
                            },
                            "name":
                            itemName,
                            "type":
                            itemBaseType,
                            "stats": [{
                                "type": "and",
                                "filters": []
                            }, {
                                "filters": filt,
                                "type": "and"
                            }],
                            "filters": {
                                "type_filters": {
                                    "filters": {
                                        "rarity": {
                                            "option": "unique"
                                        }
                                    }
                                }
                            }
                        },
                        "sort": {
                            "price": "asc"
                        }
                    }
                elif itemBaseType == '小型星团珠宝' or itemBaseType=='Small Cluster Jewel':
                    payload = {
                        "query": {
                            "status": {
                                "option": "online"
                            },
                            "name": itemName,
                            "type": itemBaseType,
                            "stats": [{
                                "type": "and",
                                "filters": []
                            }]
                        },
                        "sort": {
                            "price": "asc"
                        }
                    }
                elif itemBaseType == '大型星团珠宝' or itemBaseType=='Large Cluster Jewel':
                    jewl['skillnum'] = int(
                        re.findall(r"\d+\.?\d*",
                                   splitedstr[2].splitlines()[0])[0])
                    jewl['hole'] = int(
                        re.findall(r"\d+\.?\d*",
                                   splitedstr[2].splitlines()[1])[0])
                    payload = {
                        "query": {
                            "status": {
                                "option": "online"
                            },
                            "name":
                            itemName,
                            "type":
                            itemBaseType,
                            "stats": [{
                                "type": "and",
                                "filters": []
                            }, {
                                "filters": [{
                                    "id": "explicit.stat_247746531",
                                    "value": {
                                        "max": jewl['skillnum'],
                                        "min": jewl['skillnum']
                                    },
                                    "disabled": False
                                }, {
                                    "id": "explicit.stat_1085446536",
                                    "value": {
                                        "max": jewl['hole'],
                                        "min": jewl['hole']
                                    },
                                    "disabled": False
                                }],
                                "type":
                                "and"
                            }]
                        },
                        "sort": {
                            "price": "asc"
                        }
                    }
            else:
                for index, each_contant in enumerate(splitedstr):
                    if each_contant.find('增加的小天赋获得') != -1:
                        keyCont = each_contant
                    elif each_contant.find('增加的天赋跟珠宝范围无关') !=-1:
                        skillCont = splitedstr[index - 1]
                jewl['skillnum'] = int(
                    re.findall(r"\d+\.?\d*",
                               keyCont.splitlines()[0])[0])
                jewl['hole'] = int(
                    re.findall(r"\d+\.?\d*",
                               keyCont.splitlines()[1])[0])
                jewl['enchant'] = int(jewl_enchant.index(removeEnchant(keyCont.splitlines()[2]))) + 1

                print(jewl['skillnum'], jewl['hole'], jewl['enchant'])
                filt = [{
                    "id": "enchant.stat_3086156145",
                    "value": {
                        "max": jewl['skillnum'],
                        "min": jewl['skillnum']
                    },
                    "disabled": False
                }, {
                    "id": "enchant.stat_4079888060",
                    "value": {
                        "min": jewl['hole'],
                        "max": jewl['hole']
                    },
                    "disabled": False
                }, {
                    "id": "enchant.stat_3948993189",
                    "value": {
                        "option": jewl['enchant']
                    },
                    "disabled": False
                }]
                if skillCont.find('加的小天赋还获得') != -1:
                    skilllist = skillCont.splitlines()
                    for each_contant in skilllist:
                        if each_contant.find(r'其中 1 个增加的天赋为') != -1:
                            for result_content in d_mods['result']:
                                for k, v in result_content.items():
                                    if isinstance(v, list):
                                        for i in v:
                                            if i['text'] == each_contant:
                                                print(i['id'])
                                                filt.append({
                                                    "id": i['id'],
                                                    "value": {},
                                                    "disabled": False
                                                })

                payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type":
                        itemName,
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }, {
                            "filters": filt,
                            "type": "and"
                        }]
                    },
                    "sort": {
                        "price": "asc"
                    }
                }
        elif clipboard.find('放置到一个天赋树的珠宝插槽中以产生效果。右键点击以移出插槽。') !=-1:
            region_len = len(splitedstr[0].splitlines())
            if language_choice.get()=='国服':
                if region_len==4:
                    itemBaseType = splitedstr[0].splitlines()[3]
                elif region_len==3:
                    itemBaseType = splitedstr[0].splitlines()[2]
            else:
                if region_len==4:
                    itemBaseType = remove_chinese(splitedstr[0].splitlines()[3])
                elif region_len==3:
                    itemBaseType = remove_chinese(splitedstr[0].splitlines()[2])
            print(itemBaseType)
            filt = []
            m = read_info(clipboard,itemClass)
            for t in m:
                filt.append({
                    "id": t.id,
                    'value':{},
                    "disabled": False
                })
            payload = {"query":{"status":{"option":"online"},"type":itemBaseType,"stats":[{"type":"and","filters":[]},{"filters":filt,"type":"and"}]},"sort":{"price":"asc"}}        

    elif itemClass =='深渊珠宝':
        region_len = len(splitedstr[0].splitlines())
        if language_choice.get()=='国服':
            if region_len==4:
                itemBaseType = splitedstr[0].splitlines()[3]
            elif region_len==3:
                itemBaseType = splitedstr[0].splitlines()[2]
        else:
            if region_len==4:
                itemBaseType = remove_chinese(splitedstr[0].splitlines()[3])
            elif region_len==3:
                itemBaseType = remove_chinese(splitedstr[0].splitlines()[2])
        print(itemBaseType)
        filt = []
        m = read_info(clipboard,itemClass)
        for t in m:
            filt.append({
                "id": t.id,
                'value':{},
                "disabled": False
            })
        payload = {"query":{"status":{"option":"online"},"type":itemBaseType,"stats":[{"type":"and","filters":[]},{"filters":filt,"type":"and"}]},"sort":{"price":"asc"}}        

    elif itemClass == '辅助技能宝石' or itemClass == '主动技能宝石':
        skill_item_lvl = 0
        skill_item_quality = 0
        skill_alt_quality = 0
        print('技能宝石')
        for line in splitedstr[1].splitlines():
            if line.startswith('等级'):
                skill_item_lvl = re.findall(r'\d+', line)[0]       
            elif line.startswith('品质'):
                skill_item_quality = re.findall(r'\d+', line)[0]

        if language_choice.get()=='国服':
            itemName = splitedstr[0].splitlines()[2]
        else:
            itemName = remove_chinese(splitedstr[0].splitlines()[2])

        for region in splitedstr:
            if region.startswith('瓦尔：'):
                itemName = region.replace('\r\n','')
        if itemName.find('诡异的') != -1:
            itemName = itemName.replace('诡异的 ', '')
            skill_alt_quality = 1
        elif itemName.find('分歧') != -1:
            itemName = itemName.replace('分歧 ', '')
            skill_alt_quality = 2
        elif itemName.find('魅影') != -1:
            itemName = itemName.replace('魅影 ', '')
            skill_alt_quality = 3
        elif itemName.find('异常 ') !=-1:
            itemName = itemName.replace('异常 ', '')
            skill_alt_quality = 1


        payload = {
            "query": {
                "status": {
                    "option": "online"
                },
                "type": itemName,
                "stats": [{
                    "type": "and",
                    "filters": []
                }],
                "filters": {
                    "misc_filters": {
                        "filters": {
                            "gem_level": {
                                "min": skill_item_lvl,
                                "max": skill_item_lvl
                            },
                            "quality": {
                                "min": skill_item_quality,
                                "max": skill_item_quality
                            },
                            "gem_alternate_quality": {
                                "option": skill_alt_quality
                            }
                        }
                    }
                }
            },
            "sort": {
                "price": "asc"
            }
        }
    elif itemClass == '地心探索可堆叠可插入通货':
        if language_choice.get()==('国服'):
            itemName = splitedstr[0].splitlines()[2]
        else:
            itemName = remove_chinese(splitedstr[0].splitlines()[2])
        itemMount = getAmount(splitedstr[1].splitlines()[0])
        payload = {
            "query": {
                "status": {
                    "option": "online"
                },
                "type": itemName,
                "stats": [{
                    "type": "and",
                    "filters": []
                }],
                "filters": {
                    "misc_filters": {
                        "filters": {
                            "stack_size": {
                                "min": itemMount,
                                "max": itemMount
                            }
                        }
                    }
                }
            },
            "sort": {
                "price": "asc"
            }
        }
    elif itemClass=='先祖秘藏日志':
        itemName = '先祖秘藏日志'
        filt = []
        m = read_info(clipboard,itemClass)
        advancedSearch.add_item(m)
        advancedSearch.create_at_cursor()
        selected_m,selected_value = advancedSearch.get_select()

        if selected_m==None: return None
        value_t = {}
        for t in selected_m:
            if selected_value[t.id][0]!='':
                value_t['min'] = selected_value[t.id][0]
            if selected_value[t.id][1] !='':
                value_t['max'] = selected_value[t.id][1]
            filt.append({
                "id": t.id,
                'value':value_t,
                "disabled": False
            })
        payload = {
                    "query": {
                        "status": {
                            "option": "online"
                        },
                        "type": itemName,
                        "stats": [{
                            "type": "and",
                            "filters": []
                        }, {
                            "filters": filt,
                            "type": "and"
                        }],
                        "filters": {
                            "type_filters": {
                                "filters": {
                                    "rarity": {
                                        "option": "rare"
                                    }
                                }
                            }
                        }
                    },
                    "sort": {
                        "price": "asc"
                    }
                }        
    if payload == None: return payload
    # print(payload)
    return payload


def process_dict(s):
    if s['price']:
        single_price = s['price']['amount']
        unit = s['price']['currency']
        price_info = str(single_price) + " " + unit
        return price_info
    else:
        return '无定价'


def findTradeInfo(clipboard):
    # 设置重连次数
 
    if language_choice.get()=='国服':
        headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '145',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Host': 'poe.game.qq.com',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }   
        url = "https://poe.game.qq.com/api/trade/search/" + league
        item_url = 'https://poe.game.qq.com/trade/search/'
        fetch_url = 'https://poe.game.qq.com/api/trade/fetch/'
    else:
        headers = {
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
            86.0.4240.198 Safari/537.36"
        }

        url = 'https://www.pathofexile.com/api/trade/search/' + league
        item_url = 'https://pathofexile.com/trade/search/'
        fetch_url = 'https://www.pathofexile.com/api/trade/fetch/'
    payload = loadpayLoad(clipboard)
    name, itemtype = getNameAndType(clipboard)
    if itemtype == None:
        return None, None, None
    if payload == None:
        return None, None, None
    if language_choice.get()=='国际服':
        if name != None:
            name = remove_chinese(name)
        if itemtype != None:
            itemtype = remove_chinese(itemtype)        
    if player_option.get() == 'online':
        payload['query']['status']['option'] = 'online'
    elif player_option.get() == 'onlineleague':
        payload['query']['status']['option'] = 'onlineleague'
    elif player_option.get() == 'any':
        payload['query']['status']['option'] = 'any'
    
    payload.update({"filters":{"trade_filters":{"filters":{"collapse":{"option":"False"}}}}})
    if is_colls_player_id.get() == 0:
        payload['filters']['trade_filters']['filters']['collapse']['option'] = False
    else:
        payload['filters']['trade_filters']['filters']['collapse']['option'] = True

    response = requests.post(url, data=json.dumps(payload),headers=headers)
    if response.status_code != 200:
        print('post error ' + str(response.status_code))
        print(clipboard)
        print(payload)
        return
    response_json = json.loads(response.text)
    itemid = response_json['id']
    print('装备网址：' + item_url + league + '/' + itemid)
    pyperclip.copy(item_url + league + '/' + itemid)


    list = response_json['result']
    url = fetch_url
    maxCount = 10
    step = int(len(list) / maxCount) + 1
    for i in range(0, len(list), step):
        url = url + list[i] + ','
    url = url[:-1]
    url = url + '?query=' + itemid

    if language_choice.get()=='国服':
        result = requests.get(url)
    else:
        result = requests.get(url,headers=headers)
    if result.status_code != 200:
        # print('get error ' + str(response.status_code))
        print("市级缺货")
        return None, None, None
    if name != None:
        temName = name + " " + itemtype
    else:
        temName = itemtype

    trade_info = result.json()['result']

    if trade_info:
        prev_account_name = ""
        # Modify data to usable status.
        times = []
        prices = []
        itemimg = ''
        for trade in trade_info:  # Stop price fixers
            if trade["listing"]["price"]:
                if trade["listing"]["account"]["name"] != prev_account_name:
                    price = (
                        str(trade["listing"]["price"]["amount"]) + " " +
                        pretty_currency(trade["listing"]["price"]["currency"]))
                    prices.append(price)
                    times.append(
                        datetime.strptime(trade["listing"]["indexed"],"%Y-%m-%dT%H:%M:%SZ"))
                prev_account_name = trade["listing"]["account"]["name"]
                itemimg = trade["item"]["icon"]


        merged = {}
        for i in range(len(prices)):
            if prices[i] in merged:
                merged[prices[i]].append(times[i].replace(tzinfo=timezone.utc))
            else:
                merged[prices[i]] = [times[i].replace(tzinfo=timezone.utc)]

        for key, value in merged.items():
            combined = 0
            count = 0
            for t in value:
                combined += t.timestamp()
                count += 1
            combined = combined / count
            merged[key] = [
                count,
                datetime.fromtimestamp(combined, tz=timezone.utc),
            ]
        return merged, temName, itemimg


def main():
    print('将鼠标对准装备，按下复制按钮 【Ctrl+C】')
    pyperclip.copy('')
    recent_value = ''

    while True:
        try:
            time.sleep(0.2)
            clipboard = pyperclip.paste()
            if clipboard != recent_value and clipboard.find('--------') !=-1:
                # read_info(clipboard)
                recent_value = clipboard
                data, temName,itemimg = findTradeInfo(clipboard)
                if data and temName:
                    priceInformation.add_price_information(data, temName,itemimg,clipboard)
                    priceInformation.create_at_cursor()
                else:
                    notEnoughInformation.create_at_cursor()
                    print("无法获得相关数据")
        except BaseException as e:
            if isinstance(e, KeyboardInterrupt):
                print("请将游戏最小化后，再使用管理员模式启动本程序")
            print(e)


def league_choose():
    global window
    global league
    window.state('icon')
    window.iconify()
    league = saiji_value.get()
    window.destroy()
    main()

GUI_BG1 = '#1a1a1a'
GUI_BG2 = '#1f1f1f'
GUI_FONT = 'Courier'
GUI_FONT_SIZE = 12
GUI_FONT_COLOR = '#fff8e1'
GUI_HEADER_COLOR = '#0d0d0d'
GUI_HEADER_COLOR2 = '#BB5E00'
GUI_FONT_COLOR2 = '#FFDCB9'

window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('流放之路查价插件-v1.70')
screenwidth = window.winfo_screenwidth()  # 屏幕宽度
screenheight = window.winfo_screenheight()  # 屏幕高度
width = 300
height = 380
x = int((screenwidth - width) / 2)
y = int((screenheight - height) / 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
window.resizable(width=False, height=False)
window.configure(bg=GUI_BG2)



saiji_lable = tk.Label(window, text='赛季选择：',bg=GUI_BG2, fg=GUI_FONT_COLOR)
saiji_lable.grid(column=1, row=2,padx=10, pady=10)


saiji_value = tk.StringVar()
saiji_combobox = ttk.Combobox(window,
                            width=15,
                            textvariable=saiji_value,
                            state='readonly')
saiji_combobox['values'] = leagueTupe
saiji_combobox.grid(column=2, row=2)
saiji_combobox.current(0)
########################################################################



language = tk.Label(window, text='服务器选择：',bg=GUI_BG2, fg=GUI_FONT_COLOR)
language.grid(column=1, row=1)
hide_msg = ToolTip(language,text='选择服务器，进行赛季更新！')
language_choice = tk.StringVar()

def get_request(addr: str, timeout: int, max_tries: int, stream=False):
    try:
        r = requests.get(addr, timeout=timeout, stream=stream,headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'})

        if r.status_code != 200:
            print(
                f"[!] Trade result retrieval failed: HTTP {r.status_code}! "
                f'Message: {r.json().get("error", "unknown error")}'
            )

        return r.json()
    except Exception:
        site = ""
        x = addr.rfind(".")
        y = addr.find("/", x)
        site += addr[:y]
        if max_tries > 0:
            print(
                site
                + " 服务器无响应，重新尝试 "
                + str(max_tries)
                + " 次"
            )
            return get_request(addr, timeout, max_tries - 1, stream)
        else:
            print("无法连接到: " + site + ".")
            return None

def get_leagues() -> tuple:
    """Query the API to get all current running leagues

    :return: Tuple of league ids
    """
    try:
        leagues = get_request(
            "https://www.pathofexile.com/api/trade/data/leagues", 10, 2
        )
        print('获取国际服赛季完成')
        return tuple(x["id"] for x in leagues["result"])
    except Exception:
        return None

def update_league(event):
    print(language_choice.get())
    global leagueTupe
    leagueTupe  = []
    try:
        print("获取赛季中...")
        if language_choice.get()=='国服':
            url = 'https://poe.game.qq.com/api/trade/data/leagues'
            res = requests.get(url).text
            unicode2str = res
            unicode2str_dict = eval(unicode2str)
            leagueList = unicode2str_dict['result']
            print("获取国服赛季完成")
            for i in leagueList:
                leagueTupe.append(i['id'])    
        elif language_choice.get()=='国际服':
            leagueTupe = get_leagues()
            if leagueTupe==None:
                print('赛季获取错误，请检查网络')
    except:
        print("获取赛季信息错误")
        leagueTupe = ['错误', '错误']
    saiji_combobox['values'] = leagueTupe
    saiji_combobox.current(0)


language_choose = ttk.Combobox(window,
                            width=15,
                            textvariable=language_choice,
                            state='readonly')
language_choose['values'] = ('国服','国际服')
language_choose.grid(column=2, row=1)
language_choose.current(0)
language_choose.bind("<<ComboboxSelected>>", update_league)


###############################################################################
group1 = tk.Label(window, text="是否查询离线玩家",bg=GUI_BG2, fg=GUI_FONT_COLOR)
group1.grid(row=3,column=1)

player_option = tk.StringVar()

player_choose = ttk.Combobox(window,
                            width=15,
                            textvariable=player_option,
                            state='readonly')
player_choose['values'] = ('online','onlineleague','any')
player_choose.grid(column=2, row=3)
player_choose.current(0)



##########################
def is_colls():
    print("玩家选择数据折叠 "+str(is_colls_player_id.get()))
is_colls_player_id = tk.IntVar()
coll_button = tk.Checkbutton(window,text='同一账号数据取一',variable=is_colls_player_id,command=is_colls,bg=GUI_BG2,fg=GUI_FONT_COLOR,selectcolor='red')
coll_button.grid(column=1,row=4,padx=10, pady=10)


start_button = tk.Button(window, text='运行', command=league_choose,bg=GUI_BG2, fg=GUI_FONT_COLOR,width=12)
start_button.grid(column=1,row=5,columnspan=3,padx=10, pady=10)




win_ad = tk.Label(window ,text='我们在一个叫 【开黑啦】的语音频道里\n这里汇集了POE国际服和国服的众多玩家 \n这是一个类似国外Discord的软件\n支持游戏语音和机器人以及常规的聊天\n欢迎自行官网下载，并搜索服务器号：98094725 \n本软件在开黑啦-POE游戏频道首发',bg=GUI_BG2, fg=GUI_FONT_COLOR)
win_ad.grid(row=7,column=1,columnspan=3,rowspan=5,padx=10, pady=10)


win_ad2 = tk.Button(window, text='点我加入',bg=GUI_BG1, fg=GUI_FONT_COLOR)
win_ad2.grid(row=15, column=1,columnspan=3,padx=10, pady=10)

def open_ad(event):
    webbrowser.open("https://kaihei.co/mnMeD1", new=0)

win_ad2.bind('<Button-1>',open_ad)

window.mainloop()