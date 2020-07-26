## Webshell

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