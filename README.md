#<center>软件工程课程设计I测试报告\_第33组\_姜庆彩
<p align="right">组员：姜庆彩 柳学富 林思捷</p>
GUI框架使用python中的wxpython包实现</br>完成功能：</br>基本四则运算(带括号)</br> 求余</br>乘方</br> 平方根</br> 以10为底的对数和自然对数 </br>阶乘</br> 三角函数和反三角函数</br> 单变量方程ax<sup>2</sup>+bx+c=0的求解</br> 二元一次方程组的求解</br> 进制转换</br> 求极限</br>
求微分与高阶微分</br>  求定积分</br>
##基本四则运算（带括号）
输入：```9+5*6```</br>
输出：```39```</br>
<img src="1.png" width = "230" height = "300"/></br>
测试一个稍微复杂一点的：</br>
输入：```5*9/(3+2)-(5+56.2)*(72-6.3)```</br>
输出：```-4011.84```</br>
<img src="2.png" width = "230" height = "300"/></br>
经验证，结果正确。</br>
当出现除零的情况，计算器会提示不合法输入：</br>
输入：```5/（6-2*3）```</br>
输出：``Invalid Input``</br>
<img src="3.png" width = "230" height = "300"/></br>
本计算器还对输入表达式的合法性进行检测，如果输入表示不完整、不合法、不可执行时则会提示Invalid Input</br>
输入：``9*5+``</br>
输出：``Invalid Input``</br>
<img src="8.png" width = "230" height = "300"/></br>
##求余
输入：```9%6-2.3```</br>
输出：```0.7```</br>
<img src="4.png" width = "230" height = "300"/></br>
##	乘方
输入：```9^6+32^9+3^12```</br>
输出：```35184373151714```</br>
<img src="5.png" width = "230" height = "300"/></br>
经验证，结果正确</br>
指数可以是小数、负数</br>
输入：```9^-1+9^0.5```</br>
输出：``3.11111111111``</br>
<img src="6.png" width = "230" height = "300"/></br>
##平方根
输入：```sqrt(2)```</br>
输出：``1.41421356237``</br>
<img src="7.png" width = "230" height = "300"/></br>
平方根和乘方一样，由于该计算器没有处理虚数的相关模块，对底数有一定的限制，比如平方根下的底数不能为负数，如果不满足限制要求，则会输出Invalid Input</br>
输入：``sqrt(-3)``</br>
输出：``Invalid Input``</br>
<img src="8.png" width = "230" height = "300"/></br>
##以10为底的对数和自然对数
为了方便自然对数的使用，该计算器中还实现了自然底数e。</br>
输入：``e``</br>
输出：``2.71828182846``</br>
<img src="9.png" width = "230" height = "300"/></br>
测试对数函数的使用</br>
输入：``lg(10)*ln(e^2)``</br>
输出：``2.0``</br>
<img src="10.png" width = "230" height = "300"/></br>
对数函数对括号内的变量的取值范围也有一定的限制，要求其为正数，如果为非正数则会输出Invalid Input。</br>
输入：``lg(0)``</br>
输出：``Invalid Input``</br>
<img src="11.png" width = "230" height = "300"/></br>
##阶乘
输入：``0！``</br>
输出：``1``</br>
<img src="12.png" width = "230" height = "300"/></br>
输入：``（5*3+2）！``</br>
输出：``355687428096000``</br>
<img src="13.png" width = "230" height = "300"/></br>
输入：``17``</br>
输出：``355687428096000``</br>
<img src="14.png" width = "230" height = "300"/></br>
当阶乘函数的参数变量不为自然数（大于等于0的整数）时则会输出Invalid Input</br>
输入：``(1.2)!``</br>
输出：``Invalid Input``</br>
<img src="15.png" width = "230" height = "300"/></br>
##三角函数和反三角函数
其中包含正弦、余弦、正切、反正弦、反余弦以及反正切，由于三角函数计算模块的需要，该函数实现了π，用pi表示</br>
输入：``pi``</br>
输出：``3.14159265359``</br>
<img src="16.png" width = "230" height = "300"/></br>
###测试三角函数计算模块</br>
输入：``sin(pi/6)+cos(pi/3)+tan(pi/4)``</br>
输出：``2.0``</br>
<img src="17.png" width = "230" height = "300"/></br>
###测试反三角函数计算模块
输入：``(asin(0.5)+acos(0.5)+atan(1))/pi``</br>
输出：``0.75``</br>
<img src="18.png" width = "230" height = "300"/></br>
##单变量方程ax<sup>2</sup>+bx+c=0的求解
点击按键``EQ1``(Equation 1)，则会弹出计算该方程的相关界面，如下所示：</br>
<img src="19.png" width = "230" height = "300"/></br>
在文本框中输入方程的系数向量，向量的维度是3，分隔符是英文的逗号，数字和逗号之间可以有空格。如果输入不按要求实现则会提示Invalid Input。</br>
输入：``1,2``（个数太少）</br>
输出：``Invalid Input``</br>
<img src="20.png" width = "230" height = "300"/></br>
分以下几类情况：
###1、a=0
####b=0，则提示No Resolution
输入：```0,0,1```</br>
输出：``No Resolution``</br>
<img src="21.png" width = "230" height = "300"/></br>
####b≠0，则输出唯一一个解x=-b/c
输入：``0,2,1``</br>
输出：``x=-0.5``</br>
<img src="23.png" width = "230" height = "300"/></br>
###2、a≠0
△=b<sup>2</sup>-4ac
####△>0
输出两个解 $x1=\frac{-b+\sqrt{b^2-4ac} }{2a}$     $x2=\frac{-b-\sqrt{b^2-4ac} }{2a} $</br>
输入：```3,5,1```</br>
输出：```x1=-0.232408120756```</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```x2=-1.43425854591```</br>
<img src="24.png" width = "230" height = "300"/></br>
####△=0，输出相同解 
输入：``4,4,1``</br>
输出：``x1=x2=-0.5``</br>
<img src="25.png" width = "230" height = "300"/></br>
####△<0, 提示No Real Resolution(无实数解)
输入：``1,1,4``</br>
输出：``No Real Resolution``</br>
<img src="26.png" width = "230" height = "300"/></br>
##二元一次方程组的求解
点击``EQ2``进入解方程组界面,则会弹出计算该方程的相关界面，如下所示：
<img src="27.png" width = "230" height = "300"/></br></br>
输入:``1，2，3，1，4，5	``	</br>
输出:``x=1.0 y=1.0``</br>
<img src="28.png" width = "230" height = "300"/></br></br>
若输入不符合规范,则输出``invalid input``</br>
<img src="29.png" width = "230" height = "300"/></br>
若输入的情况没有唯一解
输入:``1，2，3，2，4，6``</br>
输出:``math error``</br>
<img src="30.png" width = "230" height = "300"/></br>
##进制转换
点击``EQ3``进入进制转换界面,则会弹出进制转换的相关界面，如下所示：
<img src="31.png" width = "300" height = "300"/></br>
输入：``16,10``</br>
输出：</br>
<img src="32.png" width = "300" height = "300"/></br>
输入：``2a,16``</br>
输出：</br>
<img src="33.png" width = "300" height = "300"/></br>
##求极限
点击``极限``进入求极限界面,则会弹出求极限的相关界面，如下所示：
<img src="34.png" width = "300" height = "300"/></br>
输入：``sin(x)/x``</br>
输出：</br>
<img src="35.png" width = "300" height = "300"/></br>
输入：``(sin(x)/x^2),0``</br>
输出：</br>
<img src="36.png" width = "300" height = "300"/></br>
oo表示正无穷
##求微分
点击``微分``进入求微分界面,则会弹出求微分的相关界面，如下所示：
<img src="37.png" width = "300" height = "300"/></br>
输入：``sin(x)``</br>
输出：</br>
<img src="38.png" width = "300" height = "300"/></br>
输入：``sin(x)/x``</br>
输出：</br>
<img src="39.png" width = "300" height = "300"/></br>
##求高阶微分
点击``高阶微分``进入求高阶微分界面,则会弹出求高阶微分的相关界面，如下所示：
<img src="40.png" width = "300" height = "300"/></br>
输入：``sin(x),2``</br>
输出：</br>
<img src="41.png" width = "300" height = "300"/></br>
输入：``sin(x)/x,2``</br>
输出：</br>
<img src="42.png" width = "300" height = "300"/></br>
##求定积分
点击``定积分``进入求定积分界面,则会弹出求定积分的相关界面，如下所示：
<img src="43.png" width = "300" height = "300"/></br>
输入：``e^x,1,3``</br>
输出：</br>
<img src="44.png" width = "300" height = "300"/></br>
输入：``sin(x)/x,pi,2*pi``</br>
输出：</br>
<img src="45.png" width = "300" height = "300"/></br>