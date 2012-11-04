pycmd
=====

a simple python program

可以在linux管道命令中来使用这个程序, 接收一个参数字符串, 里面包含需要执行的python命令
其中LINE代表从管道中读取到的一行数据

使用方法如下:

cat access.log  | pycmd.py "arr=LINE.split();print arr[12][20:].replace('11', '')"

