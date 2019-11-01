# 接口文档 V1 

> 后端接口统一采用RESTful风格  
## 用户验证  
使用JWT。header中添加auth。  

## 接口返回数据格式  
  
Key | Type  | Description  
---- | ----  | -----------  
status | boolean | 表示接口是否调用成功  
msg | string | 错误信息  
data | object | 接口返回的数据  

## 用户信息  
### 用户基本信息    
```
/api/v1/user/baseinfo  
```
**Request Data**   
  
Key | Type | Mandatory | Default | Description  
---- | ---- | --------- | -------- | -----------  
id | string | Yes | - | 要查询的用户id    


**Response Data**    
  
Key | Type  | Description  
---- | ----  | -----------  
id | string | 用户标识id  
name | string | 用户名   
avatar | string | 用户头像  
bio | string | 个性签名   
followers | int | 关注者数量   
following | int | 关注的用户数量   

### 用户详细信息  
```
/api/v1/user/detailinfo
```


## 博客  
### 专栏基础信息  
```
/api/v1/blog/baseinfo  
```  
**Request Data**  
  
Key | Type | Mandatory | Default | Description  
---- | ---- | --------- | -------- | -----------  
id | string | Yes | - | 专栏标识id  

**Response Data**   
  
Key | Type  | Description  
---- | ----  | -----------  
id  | string | 专栏标识id  
name | string | 专栏名  
authors | list | 专栏作者列表，列表内用户格式同 `用户基本信息`  
bio | string | 专栏简介 
followers | int | 关注者数量  
articles | int | 文章数量  

### 专栏下的文章列表  
```
/api/v1/blog/list
```
**Request Data**  
  
Key | Type | Mandatory | Default | Description  
---- | ---- | --------- | -------- | -----------  
id  | string | Yes | - | 专栏标识id
from | string | No | null | 上次加载最后一条内容的id，用来表示加载此id前的内容   
order | string | No | "timeup" | 用来表示博客加载的排序方式，可选的类型有: `timeup`,`timedown`,`hotup`,`hotdown` 分别表示按时间正序、倒序，按热度正序、倒序加载  

**Response Data**  
  
Key | Type  | Description  
---- | ----  | -----------  
articles | list | 博客文章列表，内容格式详见Article Data  

**Article Data**  
  
Key | Type  | Description   
---- | ----  | -----------   
title | string | 文章标题  
author | object | 作者信息， 同`用户基本信息`   
summary | string | 文章摘要   
create_datetime | int | 博客创建时间，格式为秒为单位的时间戳   
views | int | 浏览量  
comments | int | 评论数  

每次最多加载15条博客内容

### 文章详细内容 
```
/api/v1/blog/article/detail  
```  
**Request Data**  
  
Key | Type | Mandatory | Default | Description  
---- | ---- | --------- | -------- | -----------  
id | string | Yes | - | 文章ID  


**Response Data**  
  
Key | Type  | Description  
---- | ----  | -----------  
id | string | 文章ID 
title | string | 文章标题  
author | object | 作者信息， 同`用户基本信息`  
summary | string | 文章摘要  
views | int | 浏览量 
comments | int | 评论数  
content | string | 文章内容  
blog | object | 文章所属专栏，不在专栏中为null，数据格式同 `专栏基础信息`   
create_datetime | int | 博客创建时间，格式为秒为单位的时间戳   
last_modify | int | 文章最后修改时间，格式为秒为单位的时间戳 

### 文章评论  
```
/api/v1/blog/article/comments  
```  
一次性加载所有评论  

**Request Data**  
  
Key | Type | Mandatory | Default | Description  
---- | ---- | --------- | -------- | -----------  
id | string | Yes | - | 文章id  

**Response Data**  
  
Key | Type  | Description  
---- | ----  | -----------  
comments | list | 博客文章列表，内容格式详见 `Comment Data`  

**Comment Data**  
  
Key | Type  | Description  
---- | ----  | -----------  
user | object | 评论的作者， 数据格式同 `用户基本信息`   
cid | int | 评论的楼层，即本文章下第几条评论   
content | string | 评论的内容   
datetime | int | 评论的创建时间， 格式为以秒为单位的时间戳   
replay | int | 回复的楼层，不是回复的评论replay为null  


