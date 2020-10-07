## 扫描器识别

### 目前主流扫描器：

1. 全能型扫描器：wvs（Acunetix Web Vulnerability Scanner）、AppScan、WebInspect、aisec、bugscan等
2. 目录类扫描器
3. 注入工具：sqlmap、Havij

### 扫描器识别的角度

1. #### 扫描器指纹（header中的特殊字段和参数值）

2. #### IP+cookie为单位单位时间内出发规则的次数

3. #### IP+cookie(+User-Agent)单位时间内返回404的比例

   ​	这种方法主要用来应对探测敏感目录和文件的扫描器，这类的扫描器都是基于字典文件，通过对字典内的url进行请求获得的返回信息来进行判断目录或者文件的是否存在。 如果某个IP在一段时间内请求频率过快，这时候waf可以进行收集一段时间内webserver返回404状态数目，到达一定阀值后进行封杀。

~~~python
一大拨人使用同一个公网IP，怎么判断谁是攻击者？
	这里可以使用IP+Cookie的方式判断独立的用户，对于没有使用Cookie的站点也可以使用User-Agent的方式进行比较粗略的判断。
~~~



