# auto_double_zip

批量双层压缩工具

# usage 使用方法

把文件放入待压缩文件夹 -> 在右边的密码文件内输入密码 -> 运行exe文件 -> 在压缩完成文件夹拿到压缩包

 <img src="https://pic.rmb.bdstatic.com/bjh/b3b12ba67ec8b8ce62453d30ea9e604b.png">
 
 <img src="https://pic.rmb.bdstatic.com/bjh/cfd4b2e51a8a6740391b184931429b09.png">

# TODO 待更新

1. ~~移除外部的压缩程序依赖(HaoZip), 改用 py7zr, 并尝试加入多线程参数提高压缩速度~~ (py7zr 压缩性能过差, 废弃)

# tips 提示

1.  任何对程序文件夹/文件的删改都会导致程序报错无法运行
2.  ~~默认输出格式为固实 7z~~ 1.0.1版本改为输出的zip格式, 且使用copy参数(即只打包不压缩)
3.  由于使用copy参数, 文件的压缩率将为100%(不压缩), 对压缩率有需求的文件请不要使用此工具
4.  默认只有外层压缩包有密码, 若密码文件内留空, 则两层都没有密码
5.  默认对待压缩文件夹内的每个文件/文件夹做压缩, 而不是把所有文件压缩到同个压缩包, 压缩包名取文件/文件夹同名
6.  可以根据程序报错信息自行排查一些问题, 例如下图就是 删除/重命名 了密码文件

 <img src="https://pic.rmb.bdstatic.com/bjh/531a5f422d303bf6b7dd2a2ae91ff4e1.png">
