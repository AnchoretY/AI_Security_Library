## XSS

1. [深入探究浏览器编码及XSS Bypass](https://mp.weixin.qq.com/s/liODgY4NjYqdWg3JgPXMdA)
   &emsp;&emsp;对于XSS攻击过程在浏览器中的处理过程做了比较深入的解析，尤其是三种编码方式对于XSS攻击混淆的作用方式分析的很清楚透彻。

2. 【在线XSS测试站点】[Test Your XSS Skills Using Vulnerable Sites](https://www.acunetix.com/blog/web-security-zone/test-xss-skills-vulnerable-sites/)

   &emsp;&emsp;主流在线XSS技巧测试站点的总结。

### 数据集

1. #### [xss_payload_2016](https://github.com/7ioSecurity/XSS-Payloads)

&emsp;&emsp;纯xss payload总结，不带任何其他信息

2. #### [xssdb](http://xssdb.net/)

&emsp;&emsp;一个xss payload网络数据库，数据量比较大而且除payload外，还包含了每条payload的相关信息，例如注入名称、描述等，并支持以csv、txt、json等多种形式进行导出。





### 建模方式

1. ####  语言模型+分类器

   这种方式的建模分为两个阶段：

   > Step1：建立语言模型
   >
   > &emsp;&emsp;对xss样本进行分词，使用分析结果使用word2vec建立语言模型，语言模型的好坏可以使用tnse降维后可视化进行查看。
   >
   > Step2：建立分类模型
   >
   > &emsp;&emsp;使用语言模型对payload进行向量化表示，然后使用SVM、DNN等分类模型进行分类

   代表：[DL_for_xss](https://github.com/SparkSharly/DL_for_xss)

   







