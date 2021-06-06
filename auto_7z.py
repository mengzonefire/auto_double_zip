# -*- coding: utf-8 -*-
import subprocess, traceback, os
version = '1.0'
file_pw = ''    # 密码
pw_file = '密码写在这里面.txt'
input_path = '需要压缩的文件放这里'
output_path = '压缩完成的文件在这里'


def get_pw():
    global file_pw
    with open(pw_file, 'r', encoding='utf-8') as f:
        file_pw = f.read().strip()
    

def get_files():
    dirs = os.listdir(input_path)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    for i in range(len(dirs)):
        command = 'HaoZipC a -t7z "../{2}/{0}(内层).7z" "../{1}/{0}" -mhe=on -mmt=on'\
            .format(dirs[i], input_path, output_path)
        command2 = 'HaoZipC a -t7z -p"{0}" "../{2}/{1}.7z" "../{2}/{1}(内层).7z" -mhe=on -mmt=on' \
            .format(file_pw, dirs[i], output_path)
        # 同路径下需要有压缩程序 HaoZipC
        subprocess.run(command, shell=True, cwd="./HaoZip")
        subprocess.run(command2, shell=True, cwd="./HaoZip")
        os.remove('./{1}/{0}(内层).7z'.format(dirs[i], output_path))


def main():
    print('version: '+version)
    get_pw()
    get_files()
    input('按任意键退出')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        input('按任意键退出')
