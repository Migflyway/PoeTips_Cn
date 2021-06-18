from os import PathLike, link
import time
# from tkinter.constants import FALSE
import pyperclip
import requests
import json
import re
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timezone
from gui.windows import (
    priceInformation, )

league = 'S15赛季'
leagueTupe = []


def get_league():
    global leagueTupe
    try:
        print("获取赛季中...")
        url = 'https://poe.game.qq.com/api/trade/data/leagues'
        res = requests.get(url).text
        unicode2str = res
        unicode2str_dict = eval(unicode2str)
        leagueList = unicode2str_dict['result']
        print("获取赛季完成")
        for i in leagueList:
            leagueTupe.append(i['id'])
    except:
        print("获取赛季信息错误")
        leagueTupe = ['S15赛季', 'S15赛季']


get_league()



try:
    with open('mods.json', 'r', encoding='utf8') as fp:
        mods = json.load(fp)
        print('读取mods文件完成：', type(mods))
except:
    print("缺少mods文件，请重新下载")


try:
    update_exe = requests.get("https://api.github.com/repos/Migflyway/PoeTips_Cn/releases/latest")
    print("当前版本号为："+update_exe.json()["tag_name"])
except:
    print("获取版本号异常，请手动确定")
    
print("新版下载地址: https://github.com/Migflyway/PoeTips_Cn/releases/")

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


def getNum(str):
    return str.split(': ')[1]


def mountNum(str):
    return str.split(': ')[1].split('/')[0]


def cleanWord(str):
    return str.replace('精良的', '').replace('菌潮', '').strip()


def removeEnchant(str):
    return re.sub('\[(.*?)\]|\(.*?\)|增加的小天赋获得：|[/▲\s]','',str)


def getAmount(str):
    str = str.split('/')[0]
    return int(str[5:])


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
    itemClass = splitedstr[0].splitlines()[0].split(': ')[1]
    itemRairty = splitedstr[0].splitlines()[1].split(': ')[1]
    print(itemClass, itemRairty)
    itemName = ''
    itemBaseType = ''
    #传奇优先一切
    if itemRairty == '传奇':
        if itemClass != '灾变样本':
            itemName = splitedstr[0].splitlines()[2]
            itemBaseType = cleanWord(splitedstr[0].splitlines()[3])
            if itemClass == '异界地图':
                mapTier = int(getNum(splitedstr[1].splitlines()[0]))
                itemName = splitedstr[0].splitlines()[2]
                itemBaseType = cleanWord(splitedstr[0].splitlines()[3])
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
                
    if itemClass == '地图碎片':
        itemName = splitedstr[0].splitlines()[2]
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
        itemName = splitedstr[0].splitlines()[2]
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
        itemName = splitedstr[0].splitlines()[2]
        itemMount = getAmount(splitedstr[1].splitlines()[0])
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
            itemName = splitedstr[0].splitlines()[3]
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
            itemName = splitedstr[0].splitlines()[2]
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
            itemName = cleanWord(splitedstr[0].splitlines()[2])
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

    elif itemClass == '珠宝':
        jewl = {'skillnum': 4, 'hole': 1, 'enchant': 1}
        if clipboard.find('星团珠宝') != -1:
            print("find jw")
            if itemRairty == '稀有':
                itemName = splitedstr[0].splitlines()[3]
            elif itemRairty == '魔法':
                if splitedstr[0].splitlines()[2].find('的') != -1:
                    itemName = splitedstr[0].splitlines()[2].split('的')[1]
                elif splitedstr[0].splitlines()[2].find('之') != -1:
                    itemName = splitedstr[0].splitlines()[2].split('之')[1]
            elif itemRairty == '普通':
                itemName = cleanWord(splitedstr[0].splitlines()[2])
            elif itemRairty == '传奇':
                itemName = splitedstr[0].splitlines()[2]
                itemBaseType = cleanWord(splitedstr[0].splitlines()[3])

            if itemRairty == '传奇':
                if itemBaseType == '中型星团珠宝':
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
                            for result_content in mods['result']:
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
                elif itemBaseType == '小型星团珠宝':
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
                elif itemBaseType == '大型星团珠宝':
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
                            "天神之音",
                            "type":
                            "大型星团珠宝",
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
                        skillCont = splitedstr[index + 1]
                        break
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
                            for result_content in mods['result']:
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
    elif itemClass == '辅助技能宝石' or itemClass == '主动技能宝石':
        print('技能宝石')
        skill_item_lvl = re.findall(r'\d+', splitedstr[1].splitlines()[1])[0]
        skill_item_quality = 0
        skill_alt_quality = 0
        itemName = splitedstr[0].splitlines()[2]
        if itemName.find('诡异的') != -1:
            itemName = itemName.replace('诡异的 ', '')
            skill_alt_quality = 1
        elif itemName.find('分歧') != -1:
            itemName = itemName.replace('分歧 ', '')
            skill_alt_quality = 2
        elif itemName.find('魅影') != -1:
            itemName = itemName.replace('魅影 ', '')
            skill_alt_quality = 3

        if splitedstr[1].find('品质') != -1:
            for each_content in splitedstr[1].splitlines():
                if each_content.find('品质') != -1:
                    skill_item_quality = re.findall(r'\d+', each_content)[0]

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
        itemName = splitedstr[0].splitlines()[2]
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
    # 设置重连次数
    url = "https://poe.game.qq.com/api/trade/search/" + league
    payload = loadpayLoad(clipboard)
    name, itemtype = getNameAndType(clipboard)
    if itemtype == None:
        return None, None, None
    if payload == None:
        return None, None, None
    if player_option.get() == 'online':
        payload['query']['status']['option'] = 'online'
    elif player_option.get() == 'onlineleague':
        payload['query']['status']['option'] = 'onlineleague'
    elif player_option.get() == 'any':
        payload['query']['status']['option'] = 'any'

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    # response = requests.post(url, data=json.dumps(payload))
    if response.status_code != 200:
        print('post error ' + str(response.status_code))
        return
    response_json = json.loads(response.text)
    # response_json = demjson.decode(response.text)
    itemid = response_json['id']
    print('装备网址：https://poe.game.qq.com/trade/search/' + league + '/' + itemid)
    pyperclip.copy('https://poe.game.qq.com/trade/search/' + league + '/' +
                   itemid)
    list = response_json['result']
    url = 'https://poe.game.qq.com/api/trade/fetch/'
    maxCount = 10
    step = int(len(list) / maxCount) + 1
    for i in range(0, len(list), step):
        url = url + list[i] + ','
    url = url[:-1]
    url = url + '?query=' + itemid

    result = requests.get(url)
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
        for trade in trade_info:  # Stop price fixers
            if trade["listing"]["price"]:
                if trade["listing"]["account"]["name"] != prev_account_name:
                    price = (
                        str(trade["listing"]["price"]["amount"]) + " " +
                        pretty_currency(trade["listing"]["price"]["currency"]))
                    prices.append(price)
                    times.append(
                        datetime.strptime(trade["listing"]["indexed"],
                                          "%Y-%m-%dT%H:%M:%SZ"))
                prev_account_name = trade["listing"]["account"]["name"]

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
        return merged, len(prices), temName


def main():
    print('将鼠标对准装备，按下复制按钮 【Ctrl+C】')
    pyperclip.copy('')
    recent_value = ''

    while True:
        try:
            time.sleep(0.2)
            clipboard = pyperclip.paste()
            if clipboard != recent_value and clipboard.find('--------') !=-1:
                recent_value = clipboard
                data, results, temName = findTradeInfo(clipboard)
                if data and results and temName:
                    priceInformation.add_price_information(data, temName)
                    priceInformation.create_at_cursor()
                else:
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
    league = numberChosen.get()
    window.destroy()
    main()



window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('流放之路查价插件-v1.55')
screenwidth = window.winfo_screenwidth()  # 屏幕宽度
screenheight = window.winfo_screenheight()  # 屏幕高度
width = 300
height = 300
x = int((screenwidth - width) / 2)
y = int((screenheight - height) / 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

group = tk.LabelFrame(window, text="请选择您的赛季", padx=5, pady=5)
group.pack(padx=10, pady=10)

saiji = tk.Label(group, text='赛季选择：')
saiji.grid(column=1, row=2)


number = tk.StringVar()
numberChosen = ttk.Combobox(group,
                            width=15,
                            textvariable=number,
                            state='readonly')
numberChosen['values'] = leagueTupe
numberChosen.grid(column=2, row=2)
numberChosen.current(0)

group1 = tk.LabelFrame(window, text="是否查询离线玩家", padx=5, pady=5)
group1.pack(padx=10, pady=10)

player_option = tk.StringVar()
player_option.set('online')
r1 = tk.Radiobutton(group1, text='在线', value='online', variable=player_option)
r1.pack()
r2 = tk.Radiobutton(group1,
                    text='赛季在线',
                    value='onlineleague',
                    variable=player_option)
r2.pack()
r3 = tk.Radiobutton(group1, text='任何', value='any', variable=player_option)
r3.pack()

b1 = tk.Button(window, text='运行', command=league_choose)
b1.pack()
window.mainloop()