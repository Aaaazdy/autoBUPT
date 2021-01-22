# BUPT疫情防控通自动打卡Python脚本小白版

> ###### 声明1：本脚本为不得用于任何商业利益，仅为方便同学和自己打卡使用
>
> ###### 声明2：本教程为楼主结合github同校友所发代码，并对其进行解释和详细步骤补充后所得
> ###### 声明3：博主只是个菜鸡，希望dl们轻喷

### 本教程分为网址分析与代码编写、使用教程两个步骤，想直接使用的同学请直接跳转到使用教程

### 一、网址分析与代码编写

疫情防控通内置于微信企业号，我们在电脑端微信打开疫情防控通——每日打卡，复制其链接在浏览器打开[https://app.bupt.edu.cn/ncov/wap/default/index](https://app.bupt.edu.cn/ncov/wap/default/index)
			![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122162935298.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
			从未登录过的同学首次访问该网址进入的便是这个页面，输入的账号和密码是你的**学号**和**信息门户密码**，登录成功后便是打卡页面
			![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012216330180.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
因此要实现自动打卡，我们第一步就是要通过POST数据登录后获取Session信息，之后才能向打卡的网址进行POST打卡信息，那POST哪个网址呢？我们打开调试工具看一眼这个POST包
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122163720581.png#pic_center)
POST的URL为[https://app.bupt.edu.cn/uc/wap/login/check](https://app.bupt.edu.cn/uc/wap/login/check)，Data数据为
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122163900638.png#pic_center)
由此，我们便可以编写代码模拟POST该数据给此URL以此得到需要的其他数据
**代码如下：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122164709708.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
因为是一整块，就只放图片了，不放代码段了，最后会有完整代码
**第二步**
登录成功后，就可以进行打卡了，同样步骤，看看打卡信息POST的网址是啥
[https://app.bupt.edu.cn/ncov/wap/default/save](https://app.bupt.edu.cn/ncov/wap/default/save)
这个emmm，因为这个本人的一直每天自动打卡了，所以截不了图，暂时知道就是这个网址吧，等有图了再补，然后POST的数据有很多很多很多，但每天变的就只有时间这一项（除非你位置移动），因此只需要自行填充时间的数据，其他数据复制粘贴之前的就可以
在某一天的凌晨使用电脑端打卡一次并拿到自己的data后，便之后可以用这个数据奔放啦~
大家的数据应该都 一样，长这样（这个是一个在线网站转换后的样式）

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122171224407.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70)
**重要的是date这个参数**，他代表的是你打卡的日期，因此也只有这一个参数是每天变化的，需要我们自己填充，我们将前后date前后两段分别截，储存成**FORMDATA1**和**FORMDATA2**，格式是这种&的形式![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122171825140.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122171945753.png#pic_center)
然后编写代码进行POST打卡
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122172110871.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
若return信息里包含如下，即打卡成功
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012217215979.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
### 二、使用教程
#### (一)参数获取
首先复制或下载示例代码，在里面填入你自己的参数，我们需要四个参数，分别是
**USERNAME=['学号']
PASSWORD=['信息门户密码']
FORMDATA1=['date前半段数据,一直复制到date=']
FORMDATA2=['后半段数据，从&tw=开始']**
如果你没看第一节，那个可能得需要学习一下怎么拿到后面这两个数据

 **1. 用电脑打开登录网址[https://app.bupt.edu.cn/ncov/wap/default/index](https://app.bupt.edu.cn/ncov/wap/default/index)**，**最好是edge最新版或者chrome，firefox等**
  **2. 输入学号和信息门户密码登录，登录成功后，进入打卡页面**
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122173510324.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
  **3. 重点！！首先开启定位获取定位信息，之后！
  在点击打卡之前，按F12或右键-检查，将调试者工具页面调出，点击右上角的NetWork**
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122173818927.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)

   **4. 保持以上页面不动后，点击打卡，之后右侧便会出现一个名字叫“save”的东西**
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122174010886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)


   **5. 点击save，翻到最下面，点击这个“view source”**
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012217412970.png#pic_center)
   **6. 完整复制整个字符串，应该是以ismoved开头的 很长很长一段字符串**

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122174329803.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
   **7. FORMDATA1为 从开头到“date=”这一段**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122174450447.png#pic_center)
   **8. FORMDATA2为日期之后 从&tw开始到结束这一段**
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122174549632.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
#### (二)填写参数 并部署到服务器
 环境为Python3.6(其余版本未测试，3以上应该都可以)，需要其余包，使用pip或anaconda安装即可
 **1.apscheduler**
 		用于定时执行任务
 **2.requests**
 		基本包
 		![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122185644603.png#pic_center)
参数填写完成后将最后一行开始日期修改为下一天的任意时间点（例如我设置的开始日期就是2021年1月23日零点零一分）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122185910549.png#pic_center)

登录服务器，输入命令

```c
nohup python3 main.py &
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122190215862.png#pic_center)
由此完成了我们整个的部署工作，如果运行失败请检查一下环境问题和代码填充问题，默认打卡日志输出到本目录下的log1.txt内
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122190437945.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
#### (三)无服务器使用
windows上使用可采用系统定时任务执行python程序，
单次运行首先请将最后四行注释，并将倒数第五行解注释，然后直接点击运行即可
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122191121134.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzI1NTcxMw==,size_16,color_FFFFFF,t_70#pic_center)
运行可以使用命令 python3 main.py或点击工具里的运行按钮，运行效果图为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210122191541149.png#pic_center)
将其添加到系统定时执行任务中，具体可参考一下博客
[https://blog.csdn.net/u012849872/article/details/82719372](https://blog.csdn.net/u012849872/article/details/82719372)
以上便是所有内容，配置完成后即可实现每天零点自动打卡，解放双手啦~
要是想给同学舍友都打的话，把他们的参数都放到数组里就可以了
**有问题欢迎留言啊~**

**附录：main.py代码下载地址**
[https://github.com/hexing2333/autoBUPT](https://github.com/hexing2333/autoBUPT)
另：感谢github用户校友RaidriarB大佬初版代码