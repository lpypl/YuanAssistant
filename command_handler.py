def command_handler(command):
    import subprocess
    import os

    if '播放音乐' in command:
        subprocess.Popen('vlc')
    elif '打开浏览器' in command:
        subprocess.Popen('google-chrome-stable')
    elif '打开vscode' in command:
        subprocess.Popen('code')
    elif '重启' in command:
        os.system('reboot')
    elif '关机' in command:
        os.system('poweroff')
    elif '睡眠' in command:
        os.system('suspend')

def command_filter(command):
    command = command.strip('。')
    if command.startswith('帮我'):
        command = command[2:]
    if command.startswith('请帮我'):
        command = command[3:]
    
    return command