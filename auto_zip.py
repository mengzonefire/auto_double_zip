# -*- coding: utf-8 -*-
import subprocess
import traceback
import os
import sys
version = '1.0.1'
file_pw = ''    # 密码
pw_file = '密码写在这里面.txt'
input_path = '需要压缩的文件放这里'
output_path = '压缩完成的文件在这里'


def get_pw():
    global file_pw
    if os.path.exists(pw_file):
        with open(pw_file, 'r', encoding='utf-8') as f:
            file_pw = f.read().strip()
    else:
        with open(pw_file, 'w') as f:
            f.write()


def get_files():
    dirs = os.listdir(input_path)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    for file in dirs:
        command = 'HaoZipC a -tzip "../{2}/{0}(内层).zip" "../{1}/{0}" -mm=Copy'.format(
            file, input_path, output_path)
        command2 = 'HaoZipC a -tzip -p"{0}" "../{2}/{1}.zip" "../{2}/{1}(内层).zip" -mm=Copy'.format(
            file_pw, file, output_path)
        # 同路径下需要有压缩程序 HaoZipC
        subprocess.run(command, shell=True, cwd="./HaoZip")
        subprocess.run(command2, shell=True, cwd="./HaoZip")
        os.remove('./{1}/{0}(内层).zip'.format(file, output_path))


def main():
    exe_path, exe_name = os.path.split(sys.argv[0])
    if exe_path:
        os.chdir(exe_path)  # 切换工作目录到程序同目录
    print('version: '+version)
    get_pw()
    get_files()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
    finally:
        input('按回车键退出...')
