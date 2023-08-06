[toc]

## 项目背景
> 目前每次我们存数据库的时候都会有这样的问题，所有的数据在同步。或者说在入库时我们需要写入库的相关代码【day by day】，本着：`DRY - Don't Repeat Yourself(不要重复你自己)`原则于是我想到了我们可以异步及批量数据操作器。

## 项目构想
- 一个API用于数据的连接
- 数据调度分发器，用于数据的传输调度，异步
- 每个数据的操作分为单条及批量
- 数据的支持类型：`Kafka->ES`，`Mongo`，`SqlServer`


## 项目相关技术栈
- Mysql
- ~~Celery~~
- ~~RabitMQ~~
- KafKa,Mongo
- SqlServer
## 文件说明
> DBOP(Database Operation)数据库操作相关代码
- until文件夹日常用到的工具类
- cd_kafka.py文件用来存储处理kafka数据的管道
- cd_mongo.py文件用来存储处理Mongo数据的管道
- cd_sqlserver.py文件用来存储处理cd_sqlserver数据的管道

## Kafka
> 将Kafka进行了封装,对平时我们爬虫的一些常规数据存储做操作，利用单例模式开发支持多线程操作【加锁】

### 为什么叫`cd_Kes`
> `cd_Kes`:[ColourData Kafka-Es]彩数数据流通过kafka到Es的日常存储程序
### 使用方法
```python
from DBOP.cd_kafka import cd_Kes
items = {'Author': '新华社新闻',
        'AuthorID': '',
        'Channel': 'News',
        'ClientID': 'C102006',
        'CreateTime': '2021-07-07 21:15:00',
        'ForumName': None,
        'Likenumber': '0',
        'NumberofCoins': '0',
        'NumberofCollection': None,
        'NumberofPlay': '0',
        'NumberofRead': '0',
        'NumberofReplys': '0',
        'Retweetnumber': '0',
        'SearchBrand': '+(医防大咖流感系列访谈) +(流感 新冠)',
        'SearchTime': '2021-07-07 21:15:00',
        'ThreadId': '5e81f7274f6a8f96e35388720f7c681c',
        'URL': 'https://post.mp.qq.com/kan/article/3021573833-1522668101.html?sig=57f4d8ee405b9ed8610d5d273eb21db7&article_id=1522668101&time=1618533785&rowkey=8926078dc9658152',
        'articleTitle': '专家呼吁医务人员重视流感病毒 提升老年群体疫苗接种率',
        'hot': None,
        'label': None,
        'pid': '5e81f7274f6a8f96e35388720f7c681c',
        'realChannel': '腾讯看点',
        'replyDate': '2021-04-16 00:00:00',
        'reply': """流感和肺炎是导致老年人相关疾病发生和死亡的重要原因，但我国大部分地区流感疫苗接种率较低，给疾病在老年群体内传播带来了“可乘之机”。近日，中华预防医学会常务副会长兼秘书长梁晓峰教授、北京大学第三医院呼吸与危重症医学科主任孙永昌教授做客新华会客厅，就新冠肺炎和流感疫苗相关话题解答公众疑问。



中华预防医学会常务副会长兼秘书长梁晓峰教授

据权威专业机构估计，每年流感相关的呼吸和循环系统疾病的超额死亡率达到12.4/10万人，其中86%发生于65岁以上老年人。但各个地区老年人流感疫苗接种率普遍不高，谈及原因，梁晓峰表示，老年人疫苗接种率不高原因之一是大家对流感的重视程度不够，容易把流感和普通感冒混淆；第二是目前社会上对于流感的防控策略较少，意识较淡，下一步应该加强对流感的控制力度。“另外还有费用、流感疫苗是否纳入医保、接种不方便等一系列问题，综合导致目前老年人流感疫苗的接种率不高。”

孙永昌建议，针对老年人疫苗接种率不高这一现象，未来应在政策、便利性、费用等多方面综合考量，减少民众接种压力，提升老年群体接种积极性。

此外，医务人员也是流感的高危人群，感染风险高于普通人群。对于医务人员接种流感疫苗，应该注意哪些事项？对此梁晓峰表示，首先广大医务工作者要信任疫苗、了解疫苗，对疫苗的宣传要重新定位；其次，医务人员是流感的易感群体，所以也是流感疫苗接种的优先人群，应该从政策上给予支持，例如每年在秋冬季流行季之前免费对医务人员进行接种。

“呼吁广大医务工作者像重视新冠肺炎一样重视流感，正确认识疫苗接种的重要性，积极接种流感疫苗，预防急性呼吸道传染病的传播。”孙永昌说。""",
        'thread': 0,
        'uFans': '0'}
cd_Kes.save_to_kafka(items)
```


## SqlServer
> 将SqlServer进行了封装，会自动智能的去创建一些表和字段相关的东西，会省爬虫开发者一些时间
### TODO-LIST
- [x] 支持数据库的连接参数重写操作
```python
self.host = SQLSERVER_HOST
self.username = SQLSERVER_USERNAME
self.password = SQLSERVER_PASSWORD
self.db = SQLSERVER_DB
```
- [x] 智能创建表和字段
- [x] 操作数据同一个表字段不同时，会到表中智能增加字段
- [x] 批量数据插入操作
- [x] 支持单例多线程加锁操作
- [ ] 创建表时会自动报警钉钉通知消息
- [ ] 根据数据库连接状态进行异步操作或考虑异步模块封装成我们的业务api

### Q&A
#### Q:解决触发器的问题
> 注：相同数据库中不能有相同的触发器，虽然作用于这个表，但是他的范围是相对于数据库，相当于函数名

![DBEDF650-1E0D-42ff-A3FC-D32E8FF93CD6.png](http://tva1.sinaimg.cn/large/9aec9ebdgy1gxgzmytbhgj21y410ab29.jpg)

#### Q:解决字段名大小写不同判断有误的问题
> 使用字段做对比时全进行转换成小写后再对比

#### Q: