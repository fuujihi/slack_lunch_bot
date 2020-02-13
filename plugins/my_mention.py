# coding: utf-8
import requests
import json
import random

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

apikey = "";
shinjukugyoen = "AREAS2117"; # 一旦はベタ書き
api = "https://api.gnavi.co.jp/RestSearchAPI/v3?keyid={key}&areacode_s={areacode_s}&freeword={word}"

@listen_to('^今日のランチ')
def lunch_func(message):
    text = message.body['text']
    freeword = text.replace('今日のランチ', '')
    
    url = api.format(key=apikey, areacode_s=shinjukugyoen, word=freeword+",ランチ")
    r = requests.get(url)
    data = json.loads(r.text)
    if "error" in data:
        message.send("見つかりませんでした...:ぴえん:\nもう少し一般的なワードで検索してみてください！")
    else:
        rest = random.choice(data["rest"])
        message.send('こちらはいかがでしょう:knife_fork_plate: \n\n*'+rest["name"]+'*  -'+rest["category"]+'\n```'+rest["url"]+'\n\n'+rest["address"]+'\n'+rest["opentime"]+'\n\n'+rest["pr"]["pr_short"]+'``` '+rest["image_url"]["shop_image1"]);

@listen_to('クレップ')
def creppe_func(message):
    message.send(':たつろう::たつろう::たつろう:')
    message.react('たつろう')

@listen_to('クレープ')
def crepe_func(message):
    message.reply('クレップです！！:rage::rage:')
