
  [toc]  

 # <center> 新浪微博使用说明 </center>

 [跳转至底部](#注意事项)  ----  [回到主页](https://github.com/Sunert/Scripts)

### IOS配置教程
 ```
[MITM]
hostname = api.weibo.cn, m.weibo.cn
 ```
#### Surge:
* [模块地址](https://raw.githubusercontent.com/Sunert/Script/master/TaskConf/sina/surge.sgmodule)

 ```
https://raw.githubusercontent.com/Sunert/Script/master/TaskConf/sina/surge.sgmodule
 ```
 * 本地重写
 
 ```
[Script]
微博&钱包签到 = type=cron,cronexp=35 5 0 * * *,script-path=https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js,script-update-interval=0

# 获取微博 Cookie.
微博签到 = type=http-request,pattern=https:\/\/api\.weibo\.cn\/\d\/users\/show,script-path=https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js
微博签到 = type=http-request,pattern=https:\/\/api\.weibo\.cn\/2\/logservice\/service,script-path=https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js
```
#### Shadowrocket(Cron配置): 

```
[Script]
新浪微博 = type=cron,script-path=https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js,cronexpr="35 5 0 * * *",timeout=20,enable=true
```
####  Loon:

* [插件地址](https://raw.githubusercontent.com/Sunert/Script/master/TaskConf/sina/loon.plugin)

 ```
https://raw.githubusercontent.com/Sunert/Script/master/TaskConf/sina/loon.plugin
 ```
* 本地重写
  
 ```
[Script]
cron "4 0 * * *" script-path=https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js, enabled=true, tag=新浪微博

http-request https:\/\/api\.weibo\.cn\/\d\/users\/show script-path=https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js, enabled=true, tag=新浪微博
http-request https:\/\/api\.weibo\.cn\/2\/logservice\/service script-path=https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js, enabled=true, tag=新浪微博
```
#### Quantumult X:
   * [远程重写配置](https://raw.githubusercontent.com/Sunert/Script/master/TaskConf/sina/qx_rewite.txt)
   
```
[rewrite_remote]
https://raw.githubusercontent.com/Sunert/Script/master/TaskConf/sina/qx_rewite.txt
```
   * 本地重写配置
   
```
[rewrite_local]
https:\/\/api\.weibo\.cn\/\d\/users\/show url script-request-header https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js
https:\/\/api\.weibo\.cn\/2\/logservice\/service url script-request-header https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js
```
   * 本地任务配置
   
```
[task_local]
1 0 * * * https://raw.githubusercontent.com/Sunert/Script/master/Task/weibo.js, tag=新浪微博
```
###  获取Cookie方法
 1. 打开微博App，获取签到Cookie，获取后请注释或禁用Cookie
 2. 稍等或者刷新一下，获取用户信息Cookie(可选，增加显示个人任务红包余额)

 >>> [回到顶部](#IOS配置教程)

### Nodejs 配置密钥 (Github Actions)

<details>

  <summary>
    <span style="font-size:22">
       Actions Secrets 
    </span>
  </summary>  

| Name | 脚本相关YML | Value分割符 | 必须 / 可选 | 注意事项及样式(其中"xxx"代表任意字符) |
| :-------: | :------: | :-------: | ------ | ------- |
| WB_TOKEN | <span style="font-size:18; color:#0000ff">微博 </span> | #或换行 | 必须 | 请求地址: "https://api.weibo.cn/2/users/show"， <br>签到token: uid=xxx&gsid=xxx&s=xxx |

</details>

 >>> [回到上一页](..)
 
### 注意事项:






  
  
  
  
  
