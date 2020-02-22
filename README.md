AI_And_Web_Security_Library

Ai与Web安全相关资料的总结库，包括认为写的比较好的一些博客、项目、数据等

## 资料

1. [华为AI安全白皮书]https://github.com/AnchoretY/AI_And_Web_Security_Library/blob/master/book/ai-security-white-paper-cn.pdf





## Webshell 

### 项目

#### 1. [WebShell-Detector](https://github.com/flykingmz/WebShell-Detector)

​	全称《基于深度学习与集成学习的可配置webshell检测系统》，是08年大学生信息安全竞赛的一个Webshell检测系统，主要是是**针对Webshell文件**进行检测，采用的方式基本上是比较传统的静态检测（正则+机器学习）、动态检测技术（深度学习）的进行检测，然后使用加权的方式对模型进行组合，是一个比较基础的实现。

### 数据集



### 检测规则



### 文章

1. 



## XSS

###  项目



### 数据集

##### 1. [xss_payload_2016](https://github.com/7ioSecurity/XSS-Payloads)

​	纯xss payload总结，不带任何其他信息

##### 2. [xssdb](http://xssdb.net/)

​	一个xss payload网络数据库，数据量比较大而且除payload外，还包含了每条payload的相关信息，例如注入名称、描述等，并支持以csv、txt、json等多种形式进行导出。

### 检测规则



## DGA域名检测



### Paper&Blog

1. Hyrum S. Anderson, Jonathan Woodbridge, Bobby Filar. "DeepDGA: Adversarially-Tuned Domain Generation and Detection" [[pdf\]](https://arxiv.org/abs/1610.01969),6 Oct 2016 **(生成对抗网络，DGA检测)** 
2. Jonathan Woodbridge, Hyrum S. Anderson, Anjum Ahuja, Daniel Grant. "Predicting Domain Generation Algorithms with Long Short-Term Memory Networks" [[pdf\]](https://arxiv.org/abs/1611.00791),2 Nov 2016 **(LSTM,DGA检测)**



## 入侵检测

### 项目

#### 1.[Seq2Seq for Web Attack Detection](https://github.com/flykingmz/seq2seq-web-attack-detection)

​	使用某银行应用中的数据集进行HTTP Web攻击检测模型项目。该项目检测对象为**HTTP流量**，具有的一个比较特别的点是在**训练阶段不使用攻击样本，而只使用正常样本**，是一种类似异常检测思路，而不是大部分人使用的分类的方式。

### 数据集

1. [Vulnbank_dataset](https://github.com/AnchoretY/AI_And_Web_Security_Library/tree/master/dataset/vulnbank_dataset)

   ​	KDD大赛的一个竞赛项目，主要目的是使用机器学习得手段建立一个入侵检测器。其中的入侵行为主要包括：DDOS、密码暴力破解、缓冲区溢出、扫描等多种攻击行为。**数据格式为一些基本的统计信息**。

2. [KDD CUP 1999 Data]()

   ​	某银行应用中的HTTP流量数据集，含来自银行应用程序的21991良性和1097异常HTTP请求的数据。  数据格式为HTTP流量日志数据。

   

   ​	



