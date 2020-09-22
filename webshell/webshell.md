## Webshell

### 检测方法
#### （1）访问主要特征
|特征描述|量化指标  |
|       ----      |        ----              |
|少量IP对其发起访问|单个URL访问的IP分布         |
|总访问次数少     |单个URL每天的总访问的分布    |
|该页面属于孤立页面|单个URL的入度、出度分布      |

~~~
在构建有向图之前有一步非常关键的预处理步骤，不进行该预处理步骤很容易产生计算时间过长的问题。
**有向图**构建前的**预处理**包括：
（1）按照小时为单位进行流量切割
（2）只留下响应码为200、300的流量
（3）特征规范化：
   I. **Host规范化**： 将*.xxx.com或.xxx.com 变成 www.xxx.com
   II.**Path规范化**：归并多个/,替换\为/
   III.**referer规范化**：
      （1）将相对地址还原为绝对地址，e.g. /a.php => www.xxx.com/a.  
      （2）将host部分非本域（不在根域名内）、空字段、不符合referer规范的referer字段皆设置为空  
      （3）去除query部分  
~~~


> 这里有两个问题需要特别说明一下：  
> 1. 并不是孤立页面全是Webshell，常见还存在下面两种情况也可能是孤立页面：  
> - 隐藏管理后台等正常页面（管理后台访问不进行登录）,可以使用白名单进行剔除  
> - 扫描器，这是最主要的干扰，需要首先进行剔除扫描器产生的日志或流量(按ip+host聚类，将单位时间内请求数超过M，独立路径数超过N的请求视为扫描器)  
> 2. Webshell并不全部都是孤立页面，也存在少量Webshell会产生非孤立页面。例如：当webshell页面使用<a href标记列出当前目录下所有文件时和多页面协同型Webshell都会产生交互。因此上面的孤立页面其实就是对于页面出度、入度的一个阈值，在实际环境中可以根据具体情况进行调整。  

#### （2）Webshell Payload特征
&emsp;&emsp;WAF、IDS等基于全流量的安全产品，会把Payload特征当成主要的检测手段。




### 项目

1. #### [WebShell-Detector](https://github.com/flykingmz/WebShell-Detector)

   &emsp;&emsp;全称《基于深度学习与集成学习的可配置webshell检测系统》，是08年大学生信息安全竞赛的一个Webshell检测系统，主要是是**针对Webshell文件**进行检测，采用的方式基本上是比较传统的**静态检测（正则+机器学习）+动态检测技术（深度学习）**的进行检测，然后使用**加权的方式对模型进行组合**，是一个比较基础的实现。

2. #### [CloudWalker](https://github.com/chaitin/cloudwalker)

 &emsp;&emsp;**长亭科技在线的Webshell文件检测项目**，可以本地检测也可以线上检测。

### 数据集

1. #### [webshell-sample](https://github.com/ysrc/webshell-sample)

&emsp;&emsp;&emsp;各种**webshell文件数据**，根据webshell文件类型进行分类，量很大。

2. #### [tennc/webshell](https://github.com/tennc/webshell)

   &emsp;&emsp;一个比较大的的webshell文件收集项目。

### Blog

1. #### [基于机器学习的分布式webshell检测系统-特征工程](https://www.s0nnet.com/archives/fshell-feature-1)

   &emsp;&emsp;该文章主要对采用机器学习方式进行Webshell检测特征选取做出了一系列的总结，包括了**基于日志、基于统计学分析、基于文件的文本属性**三个角度的特征提取过程，还是比较有借鉴意义的一篇文章，作者还提供了实现的[github](https://github.com/Lingerhk/fshell)项目，在实际使用过程中可根据实际情况进行特征的选取。其中比较有借鉴意义的特征包括：

   - parameter的熵值
   - url访问频率
   - parameter的key出现的频率
   - parameter的key关联的页面数
   - 采用fuzz hashing与已知黑名单进行相似度匹配

2. #### [初探机器学习检测 PHP Webshell](https://paper.seebug.org/526/)

   &emsp;&emsp;对PHP Webshell使用opcode作为特征朴素贝叶斯算法进行检测，非常详细的讲解。
   
3. #### [Webshell检测——日志分析](http://www.91ri.org/14841.html)
