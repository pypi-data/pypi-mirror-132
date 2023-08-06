# 1.项目简介
  数据处理基础功能库
# 2. 代码结构：
1. maxda：数据处理基础库 
	* analysis：核心数据处理功能
	* config： 配置文件
	* executor: 简单的处理框架
	* util：工具类
2. tutorials：文档、示例数代码 
	* run_example.py： 测试代码
3. test：测试、调用代码
4. test_cases：测试用例
	* test_da_clean.py： 清洗功能测试代码
5. dataset：tests以及tutorials所需要的数据 


# 3. 安装部署：
1.方法一(手动安装)

   * 从gitlab上拉取代码
   * 进入代码目录执行：python3 setup.py sdist
   *  sudo pip3 install dist/maxda-x.x.x.x.tar.gz
   
2.方法二(手动安装)

   * 从gitlab上拉取代码
   * 进入代码目录执行：python3 run_build.py
   
3.方法三(pip安装)

   * 配置数据源(没有则手动创建)，linux/mac 配置文件在 ~/.pip/pip.conf，windows系统使用 pip -v config list 查找文件位置
   * 添加配置源，如下图所示
   
   ![avatar](tutorials/images/pip-config.jpg)
   
4.模型/资源配置 

  * 算法模型默认存放根目录，unix/mac: /data/share/nlp, windows系统：D:\\data\\share\\nlp或E:\\data\\share\\nlp
  * 目前maxda需要的模型文件为(以unix/mac系统为例): /data/share/nlp/label







		