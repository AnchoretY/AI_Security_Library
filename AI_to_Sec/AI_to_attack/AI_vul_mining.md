# AI辅助漏洞挖掘



### Paper

1. **Finding Bugs Using Your Own Code: Detecting Functionally-similar yet Inconsistent Code, 2020, Unsix**

&emsp;&emsp;*Northeastern University*使用bag-embedding和graphy embedding两种方式对开源代码相似度进行度量，以辅助漏洞挖掘的解决方案。具体流程如下：

1. 将C语言源程编译成Libbvm字节码

2. 对每个函数生成Data Dependency Graph

3. 将DDG差分成Constructs

4. 两步聚类

   - 查找Constructs函数功能相似的聚集成为一列

     ```
        采用每条语句进行bagging的方式进行向量化，只表达了图是否有语句、以及语句的出现次数，使用connected-component 算法进行聚类
     ```

     

   - 将功能相似的Constructions函数中上下文不一致的

     ```
       对第一步聚类中聚到一类的Constructs图进行Graph-embedding编码，然后再聚类。这种聚类融入了结构信息，对于有相同的源于，但是顺序不同、结构不同的Constructs区分道到不同的类别。然后其中的小类即为可能存在漏洞的函数。
     ```

![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.b06tw1pr51q.png)

2. [**Order Matters: Semantic-Aware Neu for Binary Code Similarity Detection**](https://keenlab.tencent.com/en/whitepapers/Ordermatters.pdf)



### Blog

1. **[AAAI-20论文解读：基于图神经网络的二进制代码分析](https://keenlab.tencent.com/zh/2019/12/10/Tencent-Keen-Security-Lab-Order-Matters/)**

科恩实验室在使用图神经网络进行大规模二进制代码相似性分析的成果，发布在人工智能顶级会议AIII-20上。





### 开源项目

