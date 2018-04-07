#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
# http://zwindr.blogspot.tw/2016/08/python-logging.html
# https://docs.python.org/3/library/logging.html
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
# 基礎設定
logging.basicConfig(level=logging.DEBUG,
                    format ='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt ='%m-%d %H:%M',
                    handlers = [logging.FileHandler('my.log', 'w', 'utf-8'),])
 
# 定義 handler 輸出 sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 設定輸出格式
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# handler 設定輸出格式
console.setFormatter(formatter)
# 加入 hander 到 root logger
logging.getLogger('').addHandler(console)
 
# root 輸出
logging.info('道可道非常道')
 
# 定義另兩個 logger
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')
 
logger1.debug('天高地遠')
logger1.info('天龍地虎')
logger2.warning('天發殺機')
logger2.error('地動天搖')


# https://docs.python.org/3/library/logging.html#logging-levels
# Level	Numeric value
# CRITICAL	50
# ERROR	40
# WARNING	30
# INFO	20
# DEBUG	10
# NOTSET	0


# http://stackoverflow.max-everyday.com/2017/10/python-logging/

# 4、Formatters

# Formatter對象設置日誌信息最後的規則、結構和內容，默認的時間格式為%Y-%m-%d %H:%M:%S，下面是Formatter常用的一些信息

# %(name)s	Logger的名字
# %(levelno)s	數字形式的日誌級別
# %(levelname)s	文本形式的日誌級別
# %(pathname)s	調用日誌輸出函數的模塊的完整路徑名，可能沒有
# %(filename)s	調用日誌輸出函數的模塊的文件名
# %(module)s	調用日誌輸出函數的模塊名
# %(funcName)s	調用日誌輸出函數的函數名
# %(lineno)d	調用日誌輸出函數的語句所在的代碼行
# %(created)f	當前時間，用UNIX標準的表示時間的浮 點數表示
# %(relativeCreated)d	輸出日誌信息時的，自Logger創建以 來的毫秒數
# %(asctime)s	字符串形式的當前時間。默認格式是 “2003-07-08 16:49:45,896″。逗號後面的是毫秒
# %(thread)d	線程ID。可能沒有
# %(threadName)s	線程名。可能沒有
# %(process)d	進程ID。可能沒有
# %(message)s	用戶輸出的消息