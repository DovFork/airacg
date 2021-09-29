#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# 0.3 版本开始不再区分ql、V3、V4。运行日志：log/bot/run.log
# author：   https://github.com/SuMaiKaDe

import json
from . import jdbot, chat_id, logger, _JdbotDir, _LogDir, _botset, _set, mybot
from .utils import load_diy
import os
from .bot.update import version, botlog
_botuplog = f'{_LogDir}/bot/up.log'
botpath = f'{_JdbotDir}/bot/'
diypath = f'{_JdbotDir}/diy/'
logger.info('loading bot module...')
load_diy('bot', botpath)
logger.info('loading diy module...')
load_diy('diy', diypath)


async def new():
    info = '[项目地址](https://github.com/SuMaiKaDe/) \t| \t[交流频道](https://t.me/tiangongtong) '
    if os.path.exists(_botuplog):
        isnew = False
        with open(_botuplog, 'r', encoding='utf-8') as f:
            logs = f.readlines()
        for log in logs:
            if version in log:
                isnew = True
                return
        if not isnew:
            with open(_botuplog, 'a', encoding='utf-8') as f:
                f.writelines([version, botlog])
            await jdbot.send_message(chat_id, f'[机器人上新了](https://github.com/SuMaiKaDe/jddockerbot/tree/master)\n{botlog}\n运行日志为log/bot/run.log\n\n\t{info}', link_preview=False)
    else:
        with open(_botuplog, 'w+', encoding='utf-8') as f:
            f.writelines([version, botlog])
        await jdbot.send_message(chat_id, f'[机器人上新了](https://github.com/SuMaiKaDe/jddockerbot/tree/master)\n{botlog}\n运行日志为log/bot/run.log\n\n\t{info}', link_preview=False)


async def mysetting():
    try:
        with open(_set, 'r', encoding='utf-8') as f:
            botset = json.load(f)
        if os.path.exists(_botset):
            with open(_botset, 'r', encoding='utf-8') as f:
                myset = json.load(f)
            if myset['版本'] != botset['版本']:
                for i in myset:
                    if '版本' not in i and not isinstance(myset[i],dict):
                        botset[i] = myset[i]
                    elif isinstance(myset[i],dict):
                        for j in myset[i]:
                            botset[i][j] = myset[i][j]
                    else:
                        continue
                with open(_botset, 'w+', encoding='utf-8') as f:
                    json.dump(botset, f)
        else:
            with open(_botset, 'w+', encoding='utf-8') as f:
                json.dump(botset, f)
    except Exception as e:
        logger.info(str(e))


async def hello():
    if '启动问候' in mybot.keys() and mybot['启动问候'].lower() == 'true':
        info = '原机器人\t-->\t[项目地址](https://github.com/SuMaiKaDe/) \t| \t[交流频道](https://t.me/tiangongtong) \ndiy机器人\t-->\t[项目地址](https://github.com/chiupam/JD_Diy) \t| \t[通知频道](https://t.me/JD_Diy_Channel)'
        await jdbot.send_message(chat_id, f'{str(mybot["启动问候语"])}\n\n\t{info}', link_preview=False)


if __name__ == "__main__":
    with jdbot:
        jdbot.loop.create_task(new())
        jdbot.loop.create_task(mysetting())
        jdbot.loop.create_task(hello())
        jdbot.loop.run_forever()