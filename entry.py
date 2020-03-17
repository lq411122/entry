#!/usr/bin/env python
import os, time
import traceback
import subprocess
from subprocess import Popen
from LoggerHelper import logger
from Configs import BASE_PATH,PROCESS_ID, ROOT_URL, INDEX_URL, PORT, CODE_URL
import webbrowser
import requests
import win32api, win32con


# 检查服务进程是否启动，默认尝试1次
def check_server(retry=1):
    ret = False
    while retry > 0 and not ret:
        try:
            r = requests.get(ROOT_URL, timeout=2)
            ret = (r.status_code == requests.codes.ok)
        except requests.HTTPError as exp:
            logger.error('服务器返回了异常：%s' % exp)
            ret = False
        except (requests.Timeout, requests.ConnectionError) as exp:
            logger.error('网页连接超时或连接失败：%s' % exp)
            ret = False
        except (requests.RequestException, Exception) as exp:
            logger.error('发现未处理的异常：%s' % exp)
            ret = False
        retry = retry - 1
    return ret


# 启动服务进程
def start_server():
    ret = None
    try:
        ret = os.system('netstat -an | find "%d"' % PORT)
        if ret == 0:
            ret = os.system('tasklist | find "%s"' % PROCESS_ID)
            if ret == 0:
                os.system('TASKKILL /F /IM %s' % PROCESS_ID)
                time.sleep(0.5)
        url = CODE_URL
        logger.info('开始启动服务 ... %s' % url)

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        # ret = Popen('%s %s' % (url, ARGS), startupinfo=startupinfo)
        ret = Popen(r'code.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,  startupinfo=startupinfo)

    except Exception as exp:
        logger.error('Error : %s, Detail : %s' % (exp, traceback.format_exc()))
    return ret


# 打开主页，为后续实现双击exe可执行文件能自动打开浏览器网页作准备
def start_url(url):
    ret = None
    try:
        logger.info('start url ... %s' % url)
        ret = webbrowser.open(url, new=2, autoraise=True)
        # time.sleep(2)
        # maxWindow()
    except Exception as exp:
        logger.error('Error : %s, Detail : %s' % (exp, traceback.format_exc()))
    return ret


# 浏览器中全屏，使用按键进行模拟
def maxWindow():
    win32api.keybd_event(122, 0, 0, 0)  # F11
    win32api.keybd_event(122, 0, win32con.KEYEVENT_KEYUP,0)  # Realize the F11 button


if __name__ == "__main__":
    logger.info('start server ...')
    if check_server():
        start_url(INDEX_URL)
    elif start_server() is not None:
        if check_server(retry=3):
            start_url(INDEX_URL)
        else:
            logger.error('ERROR : 服务未成功启动，请手工杀死进程LotServer.exe，再尝试启动！')
    else:
        start_url(os.path.join(BASE_PATH, 'error.html'))
    logger.info('end start!')