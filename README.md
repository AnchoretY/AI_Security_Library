# AI_And_Web_Security_Library
Ai与Web安全相关资料的总结库，包括认为写的比较好的一些博客、项目、数据等

## 资料

1. 华为AI安全白皮书

## 项目

#### 1.[Seq2Seq for Web Attack Detection](https://github.com/flykingmz/seq2seq-web-attack-detection)

​	使用某银行应用中的数据集进行HTTP Web攻击检测模型项目。该项目检测对象为HTTP流量，具有的一个比较特别的点是在训练阶段不使用攻击样本，而只使用正常样本，是一种类似异常检测思路，而不是大部分人使用的分类的方式。

####2. [WebShell-Detector](https://github.com/flykingmz/WebShell-Detector)

​	全称《基于深度学习与集成学习的可配置webshell检测系统》，是08年大学生信息安全竞赛的一个Webshell检测系统，主要是是**针对Webshell文件**进行检测，采用的方式基本上是比较传统的静态检测（正则+机器学习）、动态检测技术（深度学习）的进行检测，然后使用加权的方式对模型进行组合，是一个比较基础的实现。




## 数据集
1. 某银行应用中的HTTP流量数据集，含来自银行应用程序的21991良性和1097异常HTTP请求的数据。

   

2.