# learn_Flask

zlktqa文件夹为demo项目
配置步骤为：
1. 配置Flask环境``pip install -r requirements.txt``
2. 在config.py中配置Mysql参数
3. 创建名为zlktqa的数据库
4. 数据库初始化
    * ``python manage.py db init``
    * ``python manage.py db migrate``
    * ``python manage.py db upgrade``
5. 运行
    ``python zlktqa.py&``或``gunicorn zlktqa:app -w 1 -b 0.0.0.0:8080 -D``
