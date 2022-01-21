# 书籍分析项目

## 项目文件简要介绍

- .gitee ( gitee 配置文件)
- BookAnalysis ( 项目代码 )
  - analysis ( 数据分析 )
  - data ( 数据 )
  - spiders ( 爬虫 )
  - static ( Web 静态文件 )
  - templates ( Jinja 模板 )
  - test ( 测试 )
  - utils ( 辅助函数 )
  - views ( 视图 )
  - \_\_init__.py ( 项目初始化 )
  - extensions.py ( 扩展 )
  - settings.py ( 设置 )
- Files ( 项目文档 )
- .gitignore ( git 忽略文件 )
- README.md ( 项目介绍 )
- wsgi.py ( 项目入口 )

## 项目各模块

### 爬虫

#### 数据格式

1. tags.csv [标签页面](https://book.douban.com/tag/?view=type&icn=index-sorttags-all)  
   数据格式：
   
   - 父标签 parentTag
   - 子标签 tag
   - url
   
   例子：  
   
   ```csv
   parentTag,tag,url
   文学,小说,https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4
   文学,文学,https://book.douban.com/tag/%E6%96%87%E5%AD%A6
   ```
   
2. books.csv [书籍页面](https://book.douban.com/tag/%E6%96%87%E5%AD%A6)  
   数据格式：  

   - 父标签 parentTag
   - 子标签 tag
   - url
   - 书名 name
   - 作者 author
   - 出版社 publisher
   - 出品方 producer
   - 作者 author
   - 出版社 publisher
   - 出品方 producer
   - 原作名 originalName
   - 译者 translator
   - 出版年 publicationYear
   - 页数 pages
   - 定价 price
   - 装帧 bind
   - 丛书 series
   - ISBN isbn
   - 得分 score
   - 评价人数 evaluator
   - 内容简介 content
   - 作者简介 introductionAuthor
   - 目录 menu
   
3. comments.csv [短评](https://book.douban.com/subject/35534519/comments/)  
   数据格式：

   - ISBN isbn
   - 评论人 person
   - 星级 star
   - 时间 time
   - 分数 score
   - 评论 comment

4. reviews.csv [书评](https://book.douban.com/subject/35534519/reviews)  
   数据格式：  

   - ISBN isbn
   - 评论人 person
   - 星级 star
   - 时间 time
   - 有用 good
   - 没用 bad
   - 回应 reply
   - 评论 comment

#### 爬取步骤

1. 先进入 [豆瓣图书标签 (douban.com)](https://book.douban.com/tag/?view=type&icn=index-sorttags-all) 保存所有标签到 tags.csv
2. 根据各个标签的 url [豆瓣图书标签: 小说 (douban.com)](https://book.douban.com/tag/小说) ，进入每个标签下列出的书籍 url [书籍](https://book.douban.com/subject/4913064/)，保存书籍信息到 books.csv
3. 在 2 步骤中，接着保存当前页的 短评 和 书评  
   <img src="https://gitee.com/ruanxinwei/image/raw/master/image/image-20220121133843180.png" alt="image-20220121133843180" style="zoom: 50%;float:left;" />