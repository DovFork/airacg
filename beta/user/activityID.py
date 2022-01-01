#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import re
import traceback

from telethon import events

from .login import user
from .utils import execute
from .. import chat_id, jdbot, logger, TOKEN
from ..bot.utils import TASK_CMD
from ..diy.utils import myzdjr_chatIds

bot_id = int(TOKEN.split(":")[0])
client = user


@client.on(events.NewMessage(chats=myzdjr_chatIds, pattern=r'export\s(jd_zdjr_activity|jd_joinTeam_activity|FAV|OPEN_CARD|addCart|luckDraw).*=(".*"|\'.*\')'))
async def activity(event):
    """
    监控运行变量
    """
    try:
        msg = await jdbot.send_message(chat_id, '监控到活动变量')
        group = f'[{event.chat.title}](https://t.me/c/{event.chat.id}/{event.message.id})'
        if "jd_zdjr_activity" in event.message.text:
            name = '组队瓜分京豆'
            from ..diy.diy import smiek_jd_zdjr
            await smiek_jd_zdjr()
            cmd = f'{TASK_CMD} /jd/own/gua_zdjr.js now'
        elif "joinTeam" in event.message.text:
            name = '组队瓜分京豆2'
            cmd = f'{TASK_CMD} /jd/own/gua_joinTeam.js now'
        elif "FAV" in event.message.text:
            name = '收藏有礼'
            cmd = f'{TASK_CMD} /jd/own/jd_fav_shop_gift.js now'
        elif "ISV" in event.message.text:
            name = '特效关注有礼'
            cmd = f'{TASK_CMD} /jd/own/jd_follow_wxshop_gift.js now'
        elif "OPEN_CARD" in event.message.text:
            name = '会员开卡'
            cmd = f'{TASK_CMD} /jd/own/jd_open_card_by_shopid.js now'
        elif "addCart" in event.message.text:
            name = '加购有礼'
            cmd = f'{TASK_CMD} /jd/own/gua_addCart.js now'
        elif "luckDraw" in event.message.text:
            name = '抽奖有礼'
            cmd = f'{TASK_CMD} /jd/own/gua_luckDraw.js now'
        else:
            return
        messages = event.message.raw_text.split("\n")
        invalid, unchange = False, True
        for message in messages:
            if "export " not in message:
                continue
            kv = re.sub(r'.*export ', '', message)
            key = kv.split("=")[0]
            value = re.findall(r'"([^"]*)"', kv)[0]
            if "zdjr" in key and len(value) != 32:
                invalid = True
            elif os.environ.get(key) != value:
                os.environ[key] = value
                unchange = False
        if invalid:
            await msg.edit(f"监控到 {group} 的 **{name}** 活动，变量不正确停止运行……")
            return
        elif unchange:
            await msg.edit(f"监控到 {group} 的 **{name}** 活动，变量已重复停止运行……")
            return
        else:
            info = f"监控到 {group} 的 **{name}** 活动"
            await execute(msg, info, cmd)
    except Exception as e:
        title = "【💥错误💥】"
        name = "文件名：" + os.path.split(__file__)[-1].split(".")[0]
        function = "函数名：" + e.__traceback__.tb_frame.f_code.co_name
        details = "错误详情：第 " + str(e.__traceback__.tb_lineno) + " 行"
        tip = '建议百度/谷歌进行查询'
        await jdbot.send_message(chat_id, f"{title}\n\n{name}\n{function}\n错误原因：{str(e)}\n{details}\n{traceback.format_exc()}\n{tip}")
        logger.error(f"错误--->{str(e)}")