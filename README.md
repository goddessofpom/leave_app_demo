## LOONFLOW请假APP demo说明
1.leave_app/settings.py配置数据库环境，运行python manage.py makemigrations, python manage.py migrate  
2.运行python init_data.py 导入示例数据  
3.登录loonflow后台配置app，工作流,同步用户。  
4.settings.py配置LOONFLOW_TOKEN(loonflow注册的apptoken)，LOONFLOW_APP_NAME(loonflow注册的app名称)，LOONFLOW_HOST(loonflow服务器地址)，LOONFLOW_ID(工作流id)  
5.运行python manage.py runserver 8082启动  