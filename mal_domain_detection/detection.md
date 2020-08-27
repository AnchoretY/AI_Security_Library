
**Pleiades C&C信道检测整体架构图**：
![image](https://raw.githubusercontent.com/AnchoretY/images/master/blog/image.hivsidjdpi5.png)


检测整体思路：首先以主机为单位对NXDomain域名进行进行数据特征的统计，然后采用谱聚类、Xmeans聚类等进行相似的同种域名划分到同一家族，然后使用一定的策略进行精细化的过滤，然后再针对产生大量NXDomain的Host的域名其他域名同样被分类到了DGA家族中并拥有正常返回，那么该域名则为C&C域名。

&emsp;&emsp;检测主要分为两个阶段：**DGA域名发现**和**DGA分类、C&C信道检测**。


### DGA域名发现
&emsp;&emsp;在本阶段中对DNS数据的使用方式为以发起访问主机为单位对DNS域名进行特征统计。

#### Step1 数据构造
&emsp;&emsp;收集每个主机在一个时间窗口内产生的NXDomain序列

#### Step2 使用域名统计特征+XMeans进行聚类
&emsp;&emsp;构建的统计特征  
##### 1. n-gram特征
&emsp;&emsp;这里说是分别取1-4 ngram分布的中位数、均值、标注差作为特征，共12个特征。
##### 2. 熵特征
&emsp;&emsp;host的各个NXDomain的二级、三级域名和整个域名的交叉熵，然后分别取均值标准差，共6个特征。  

##### 3. 域名结构特征
&emsp;&emsp;计算各个host的各个NXdomain的长度的均值、中位数、标准差、方差，四个特征。
&emsp;&emsp;计算各个host的各个NXdomain的级别的均值、中位数、标准差、方差，四个特征。
&emsp;&emsp;计算出现不同字符的数量。
&emsp;&emsp;就算不同的TLD数量、.com域名下的子域名数量占中域名数量的比例,两个特征。
&emsp;&emsp;不同TLD出现的均值、中位数、标准差，三个特征。


#### Step3 使用Host与NXDomain的访问关系角度进行聚类







【参考文献】
- Manos Antonakakis, Damballa Inc. and Georgia Institute of Technology. "From Throw-Away Traffic to Bots: Detecting the Rise of DGA-Based Malware",2012. (DGA,图，谱聚类)
