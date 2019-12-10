# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

@listen_to('^今日のランチ')
def lunch_func(message):
    
    message.send('めちゃくちゃ美味しいものを食べましょう！')
