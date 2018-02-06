# skyutils

### 1. 背景
由于公司系统实现的原因，上班时经常需要与 JSON 数据打交道，而手头有没有一个顺手的格式化JSON数据的工具，之前用的是Chrome的一款叫做 [FEHelper](https://chrome.google.com/webstore/detail/web%E5%89%8D%E7%AB%AF%E5%8A%A9%E6%89%8Bfehelper/pkgccpejnmalmdinmhkkfafefagiiiad) 的插件，但是每次使用需要先打开Chrome，在打开插件，选择格式化JSON功能，异常繁琐。
既然找不到现成的顺手的工具，那何不自己弄一个，于是 skyutils 便诞生了。
### 2. 预览
![skyutils](http://upload-images.jianshu.io/upload_images/9923561-3dfb79363c2b8bc5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 3. 使用
* **运行环境**

Python 3.6

PyQt5 5.9.1

* **运行**
1. 下载源码: `git clone https://github.com/sukaiyi/skyutils.git`
2. 进入项目目录
3. 运行`python skyutils.py`

***注**：* skyutils.py可接收两个命令行参数，代表窗口的位置。

4. 使用`python skyutils.py`的确可以运行这个程序，如果你的环境配置没问题的话。

但是这是不推荐的方法，因为：不够快捷，每次运行会伴随一个命令行窗口。

**推荐的方法：**
使用AutoHotkey快速启动，以下是一个AutoHotkey脚本示例：
```ahk
XButton1::
AppsKey::
CoordMode,Mouse,Screen
; 获取鼠标位置
MouseGetPos,mouseX,mouseY 
CoordMode,Mouse,Relative
; 在鼠标的位置附近打开 skyutils
; 使用pythonw命令是为了避免出现命令行窗口
Run ,pythonw skyutils\skyutils.py %mouseX% %mouseY% 
return
```
运行这个脚本之后，若按下了鼠标侧键，或者键盘的应用键，便会启动程序。
有关[AutoHotkey](https://autohotkey.com/)的用法，请自行查找相关资料。
应用键一般长这样：

![应用键](http://upload-images.jianshu.io/upload_images/9923561-b6c3f63490c20203.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


* **自定义菜单**
该工具支持自定义菜单。
1. 第一步，编辑文件：`skyutils/configuration.json`
```json
[
	{
		"icon":"icon/format_json.png",
		"title":"JSON",
		"description":"格式化JSON"
	},
	{
		"icon":"icon/hide.png",
		"title":"hide",
		"description":"hide"
	},
	{
		"icon":"icon/quit.png",
		"title":"quit",
		"description":"退出"
	}
]
```
数组里的每一项代表一个菜单项，其中各字段含义如下：

icon : 该项的图标

title : 该项的标题，也是点击项之后要执行的函数名

description : 描述，当鼠标悬停时，弹出的描述性文字

***注**：*`hide`和`quit` 两项是自带的菜单，不建议删除，分别是隐藏程序（便于下次快速启动），和退出程序；他们的处理函数也不需要在`skyutils/function.py`中定义（见第三步）。

2. 第二步，找一个好看的图标
为该菜单找一个漂亮的图标`format_json.png`，放到`skyutils/icon`目录下。

3. 第三步，在`skyutils/function.py`中定义函数`JSON`
当鼠标点击该菜单时，会调用该函数；为什么是调用这个函数呢，是因为`configuration.json`文件中`title`字段指定了。下面是一个示例：

```python
def JSON(command, success, failed):
    try:
        format = formatJson.formatJSON(getClip())
        setClip(format)
        success(format)
    except Exception as e:
        message = str(type(e)) + '\n' + str(e)
        failed(message)
```
***注**：* 其中的`formatJSON, getClip, setClip` 函数都需要自己实现，事实上在这个函数里可以做任何操作，在这里做的操作是：获取剪切板的字符串，并且把他当成json格式进行格式化。

1）若格式化成功，将格式化之后的字符串设置到剪切板，并调用`success`方法，通知程序显示成功的提示消息。

2）若失败，就调用`failed`方法，传递错误消息，通知程序显示错误的提示消息

### 4. 应用场景
如下一个格式糟糕的json串：
```json
[{
"logic":"and","left":false,
"required":false,
"field":"instructionName",
"compare":"cn","data":"",
"right":false,"title":"hello",
"inputtype":"input","presetFunc":{
"funcId":"29857c2n8345o2cnx395m3f34zx9m384",
"funcCode":"code_func",
"funcName":"test"
}}]
```
1. 按下Ctrl + A, Ctrl + X 将串剪切到剪切板；
2. 按下鼠标侧键呼出skyutils，双击JSON 菜单项；
3. 回到之前的编辑器，Ctrl + V 。

以上三步，便格式化好了这个json字符串。
以下是一个演示：
![1.gif](http://upload-images.jianshu.io/upload_images/9923561-65b316a41a156fd1.gif?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
