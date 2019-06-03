# 升华网 OA
> made by sher_coder
## 需求列别 ：  
> - [x] 已完成  
> - [ ] 未完成  
> -  (待定)  
- **全局**  
  - [ ] 任务分配，DDL提醒  
- **办公室**  
- **信息部**  
- **运营部**  
  - 剩余物资统计 (待定)  
- **美工部**  
- **网络部**  
- **程序部**  

## 技术方案
- Vue
- flask
- mongodb
- redis
- docker

## 部署方法  
#### Ubuntu  
```
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