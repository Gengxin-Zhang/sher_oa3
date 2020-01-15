# 升华网 OA
> made by sher_coder
## 需求列表 ：  
> - [x] 已完成  
> - [ ] 未完成  
> -  (待定)  
### 基础功能  
  - [ ] 用户系统  
  - 签到系统  
    - [ ] 提交课表  
    - [ ] 修改排班  
    - [ ] 签入签出  
    - [ ] 请假、换班  
    - [ ] 值班统计  
  - [ ] 权限账号  

### 工具功能  
  - [ ] 协同文档  
  -  问卷 
    - [ ] 编辑  
    - [ ] 导出  
    - [ ] 权限  
  - [ ] 财务报表  
  - [ ] 打分  
  - [ ] 网盘  


## 技术方案
- Nuxt.js
- Flask
- MongoDB
- Redis
- Docker  

### 开发思路  
根据前期需求调研，我们将OA的开发分为`基础功能`和`工具功能`两部分。 
基础功能是指：一个OA系统所必须具有的功能，包括基础的用户系统、签到系统、高级管理等。  
工具功能是指：可供用户使用的、对基础功能没有影响的工具，例如：协同文档、问卷系统、财务报表、打分系统等  

## 部署方法  
#### Ubuntu  
``` bash
#安装Nginx
sudo apt update
sudo apt install nginx

#安装Docker、Docker-compose
wget -qO- https://get.docker.com/ | sh
sudo service docker start
sudo curl -L https://github.com/docker/compose/releases/download/1.23.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

#运行Docker容器
cd /var
git clone https://github.com/Gengxin-Zhang/sher_oa3.git
cd sher_oa3
sudo docker-compose up

#配置Nginx
mkdir /var/log
sudo cp ./oaapi.54sher.cn.com.conf /etc/nginx/conf.d/
sudo service nginx restart
```
