import sys

def response(text, speed="1.14"):
    import tts
    import config
    if config.speech_on:
        tts.say(text, speed=speed)


def command_handler(command):
    import subprocess
    import os

    if '打开播放器' in command:
        # 使用os.system的话，若终端被杀死，则vlc也会被杀死
        subprocess.Popen('vlc')
        response('正在打开vlc')

    elif '打开浏览器' in command:
        subprocess.Popen('google-chrome-stable')
        response('正在打开chrome')

    elif '打开vscode' in command:
        subprocess.Popen('code')
        response('正在打开vscode')

    elif '重启' in command:
        response('正在重启')
        os.system('reboot')

    elif '关机' in command:
        response('正在关机')
        os.system('poweroff')

    elif '休眠' in command:
        response('正在休眠')
        os.system('systemctl hibernate')

    # commit 并 push 本项目
    elif '推送' in command:
        response('正在启动推送')
        os.system(f"gnome-terminal -e  '{sys.path[0]}/push.sh'")

    elif '讲个笑话' in command:
        response('不讲')

    elif command.startswith('搜索'):
        response('正在启动搜索')
        os.system(f"google-chrome-stable --new-window  www.google.com/search?q={command[2:]}")

    elif '你会干什么' in command or '你会做什么' in command:
        response('小源只是个人工智障，你自己看一下源代码中定义的功能吧')

    else:
        response('小源还没有学会此命令 ' + command)


def command_filter(command):
    command = command.strip('。')
    if command.startswith('帮我'):
        command = command[2:]
    if command.startswith('请帮我'):
        command = command[3:]

    return command
