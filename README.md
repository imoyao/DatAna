## 长武县贫困情况分析

### 各乡镇基本信息：

爬虫：使用`urllib2`结合xpath抓取各乡镇概述信息写入txt文本;

读取txt，通过`re`获得json格式数据写入`town_data.json`；

### 贫困户信息：

使用xlrd读取[excel文件](https://github.com/imoyao/DatAna/blob/master/statics/infiles/foo_data.xlsx)，获得各乡镇贫困户信息；

### 信息展示：

使用`matplotlib`数据可视化库绘制出条形图和饼图。

### Usage

![运行效果](http://oh6j8wijn.bkt.clouddn.com/run.png)

## 分析结果

![贫困信息概览-条形图](http://oh6j8wijn.bkt.clouddn.com/bar_out_put.png)

![贫困户分布信息-饼图](http://oh6j8wijn.bkt.clouddn.com/pie_out_put.png)

### 总结：

Python 中文编码搞得我死去活来，问题还很多，代码鲁棒性也很差，欢迎各位Pythoner积极PR和指正。


### 参考资料：

#### 数据来源：

[各乡镇贫困户统计表](https://github.com/imoyao/DatAna/blob/master/statics/infiles/foo_data.xlsx)
[乡镇概况-长武县人民政府](http://www.snchangwu.gov.cn/zjzw/xzgk.htm)
 
#### Matplotlib的使用

[Matplotlib 入门教程 · Matplotlib 入门教程](https://wizardforcel.gitbooks.io/matplotlib-intro-tut/)

[Python--matplotlib绘图可视化知识点整理 - michael翔的IT私房菜 - SegmentFault](https://segmentfault.com/a/1190000005104723#articleHeader6)

[用Python做科学计算 - 用Python做科学计算](http://old.sebug.net/paper/books/scipydoc/index.html)

[python画图－－柱状图 - jenyzhang的专栏 - 博客频道 - CSDN.NET](http://blog.csdn.net/jenyzhang/article/details/52047557)

[Python plotting - Matplotlib 2.0.0 documentation](http://matplotlib.org/index.html)


#### excel文件读取

[python操作Excel读写--使用xlrd - lhj588 - 博客园](http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html)

[python中使用xlrd、xlwt操作excel表格详解 - qiuri2008 - 博客园](http://www.cnblogs.com/jiangzhaowei/p/5856617.html)

[Python Excel解析 - 另一个自己 - 博客频道 - CSDN.NET](http://blog.csdn.net/seetheworld518/article/details/49536599)


  [1]: http://oh6j8wijn.bkt.clouddn.com/run.png
  [2]: http://oh6j8wijn.bkt.clouddn.com/bar_out_put.png
  [3]: http://oh6j8wijn.bkt.clouddn.com/pie_out_put.png
