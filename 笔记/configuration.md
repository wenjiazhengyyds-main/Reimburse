## 1. 下载python

z注意下载器上一定是64-bit，不存在32-bit的，32-bit下载器弄出来一定是错的

3.10.9这个版本可以用 https://www.python.org/downloads/release/python-3109/



下载QT designer

https://build-system.fman.io/qt-designer-download

python 暂时必须是3.10以下的，最好目前是python3.8

https://www.python.org/downloads/release/python-390a1/

更新源

新建pip文件夹

C-users wen pip  pip.ini

[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple/
[install]
trusted-host=mirrors.aliyun.com



pip install sip

pip install wheel

pip install PyQt5

pip install PySide2

pip install pandas

- [PySide2](https://pypi.org/project/PySide2/)要求Python>=2.7、!=3.0.*、!=3.1.*、!=3.2.*、!=3.3.*、!=3.4.*、< 3.11



四个工具

- Qt Designer - 新建.ui文件
- Edit In Designer - 编辑已有的.ui文件
- PyUIC - 将.ui文件转换为python代码
- PyRCC - 将qrc文件转换为python代码

Qt Designer 









Edit In Designer

**File→Settting→Tools→External Tools→+**

名称：Edit In Designer 

程序：C:\Users\wenji\Desktop\Reimburse\venv\Scripts\pyside2-designer.exe 是在虚拟的环境下的

参数：$FileName$

工作目录：\$ProjectFileDir\$



PYUIC：

程序：pyuic。exe 位置

```Aarugment：$FileName$ -o $FileNameWithoutExtension$.py```

\$FileDir\$
