# :fire: OpenCV Webcam 脚本



### :sparkles: 更新

- `2021-12-29` **OpenCV Webcam v0.1.0正式上线**



### :zap: 安装教程

#### :white_check_mark: 方法一：Linux Shell版

```shell
# 克隆项目
git clone https://gitee.com/CV_Lab/opencv-webcam.git
# 创建conda虚拟环境，以python 3.8为例
conda create -n ow python==3.8 # 虚拟环境名称为ow
conda activate ow # 激活虚拟环境
pip install -r ./requirements.txt -U # 安装OpenCV Webcam脚本
```



#### :white_check_mark: 方法二：pip 快速安装

```shell
# 第一步：创建ow虚拟环境，参见方法一
# 第二步：执行pip指令
pip install opencv_webcam
```



### :zap: 使用教程
#### :bulb: 常规调用

```shell
# 默认按q键退出
python opencv_webcam.py
```



#### :bulb: 设置退出键

```shell
# 默认按q键退出
# 设置z键退出
python opencv_webcam.py -q z
# 设置k键退出
python opencv_webcam.py -q k
```



#### :bulb: 自动保存帧

```shell
python opencv_webcam.py -isasf
```



#### :bulb: 每隔n帧保存一次帧

```shell
# 每隔10帧保存一次帧
python opencv_webcam.py -isasf -fns 10
```



#### :bulb: 手动保存帧

```shell
# 默认按a键捕获一帧
python opencv_webcam.py -ishsf
```



#### :bulb: 自定义捕获键

```shell
# 设置z键为捕获键
python opencv_webcam.py -ishsf -fck z
```



#### :bulb: 重塑帧尺寸（自定义宽高）

```shell
# 重塑宽度300 高度200
# 自动版
python opencv_webcam.py -isasf -isrf -rf 300 200
# 手动版
python opencv_webcam.py -ishsf -isrf -rf 300 200
```



#### :bulb: 重塑帧尺寸（自定义宽高缩放比）

```shell
# 宽高缩放比为0.5
# 自动版
python opencv_webcam.py -isasf -isrf -rrf 0.5
# 手动版
python opencv_webcam.py -ishsf -isrf -rrf 0.5
```



#### :bulb: 设置保存路径

```shell
# 设置保存路径，默认保存路径为./WebcamFrame
python opencv_webcam.py -fsd custom_dir -isasf # 以自动版为例
```

