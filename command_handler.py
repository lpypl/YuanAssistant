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
    
    elif '播放音乐' in command:
        subprocess.Popen(['vlc', '/home/lpy/Music/'])
        response('即将播放')

    elif '打开浏览器' in command:
        subprocess.Popen('google-chrome-stable')
        response('正在打开chrome')

    elif '管理路由器' in command:
        subprocess.Popen('google-chrome-stable --new-window  192.168.2.1'.split())
        response('正在打开luci')

    elif '管理小飞机' in command:
        subprocess.Popen('google-chrome-stable --new-window  192.168.2.1/cgi-bin/luci///admin/services/shadowsocksr'.split())
        response('正在打开ssr plus')

    elif '打开vscode' in command:
        subprocess.Popen('code')
        response('正在打开vscode')
    
    elif '连接树莓派' in command:
        # 参数中有空格了，不能再简单的split一个字符串了
        subprocess.Popen(['gnome-terminal', '-e', 'ssh pi@192.168.2.4'])
        response('正在连接树莓派')

    elif '现在几点' in command:
        import time
        response(time.strftime('%m月%d日 %H:%M', time.localtime()))

    elif '你叫什么' in command:
        response('我叫小源，是你专属的人工智障呀')

    elif '智障' in command:
        response('你才是智障')

    # commit 并 push 本项目
    elif '推送' in command:
        subprocess.Popen(f"gnome-terminal -e  '{sys.path[0]}/push.sh'".split())
        response('正在启动推送')
    
    elif command.startswith('搜索'):
        subprocess.Popen(f"google-chrome-stable --new-window  www.google.com/search?q={command[2:]}".split())
        response('正在启动搜索')

    elif '唱歌' in command or '唱首歌' in command:
        response('twinkle, twinkle, little star, how i wonder what you are')

    elif '讲个笑话' in command:
        response('不讲')

    elif '你会干什么' in command or '你会做什么' in command:
        # subprocess.Popen(f"gedit {sys.path[0]}/command_handler.py".split())
        response('小源只是个人工智障，你自己看一下源代码中定义的功能吧')

    elif '开启复读机模式' in command:
        response('已开启复读机模式')
        os.system(f'touch {sys.path[0]}/.repeater')
    
    elif '关闭复读机模式' in command:
        response('已关闭复读机模式')
        os.system(f'rm -rf {sys.path[0]}/.repeater')

    elif '重启' in command:
        response('正在重启')
        os.system('reboot')

    elif '关机' in command:
        response('正在关机')
        os.system('poweroff')

    elif '休眠' in command:
        response('正在休眠')
        os.system('systemctl hibernate')

    else:
        if os.path.exists(f'{sys.path[0]}/.repeater'):
            response(command)
        else:
            response('小源还没有学会此命令 ' + command)


def command_filter(command):
    command = command.strip('。')
    if command.startswith('帮我'):
        command = command[2:]
    if command.startswith('请帮我'):
        command = command[3:]

    return command
