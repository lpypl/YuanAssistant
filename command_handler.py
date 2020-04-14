def response(text, speed="1.14"):
    import tts
    import config
    if config.speech_on:
        tts.say(text, speed=speed)


def command_handler(command):
    import subprocess
    import os

    if '打开播放器' in command:
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

    elif '睡眠' in command:
        response('正在睡眠')
        os.system('suspend')

    else:
        response('小源还没有学会此命令 ' + command)


def command_filter(command):
    command = command.strip('。')
    if command.startswith('帮我'):
        command = command[2:]
    if command.startswith('请帮我'):
        command = command[3:]

    return command
