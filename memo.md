1、从原仓库（upstream）合并最新的代码：https://github.com/selfteaching/the-craft-of-selfteaching/issues/67

2、本机安装PostgreSQL，连接调试通过 ：https://www.postgresql.org/download/linux/redhat/

—— 更改proxypool的数据库为PostgreSQL


防火墙相关：
https://cloud.tencent.com/developer/article/1633310


部署api和抓取服务：
https://www.huaweicloud.com/articles/f3d556f2181b7e3924c191370628c883.html


supervisorctl status
supervisorctl reload
supervisorctl stop all
supervisorctl start all

外网访问 & 支持https
1. 腾讯云给域名申请ssl证书
2. gunicorn启动时，指定--certfile='/home/nginx/1_cdcvm.heqiuzhi.xyz_bundle.crt' --keyfile='/home/nginx/2_cdcvm.heqiuzhi.xyz.key'
3. 换成dota2域名！
