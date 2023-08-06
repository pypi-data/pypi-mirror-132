# Agilex LIMO python API

###### 这是limo的Python接口文档，你可通过pip安装此接口，通过python接收limo发出的信息，也可以按照规定向limo发送命令，控制limo的移动。

### 安装

##### 注意:

###### 本接口依赖于Python3，如果没有请安装python3.5版本以上的python，如果你的电脑上同时有python2和python3，请使用python3

###### 请确认pip3版本为最新版. 

```bash
pip3 -V     																				 #cheak the pip3 version
python3 -m pip install --upgrade pip                          #updata pip3
```

##### 安装命令：

#### pip

````bash
pip3 install pylimo
````

### 添加库

```python
#!/usr/bin/env python3
# coding=utf-8
from pylimo import Limo
robots=limo.LIMO()
```

#### 方法列表:

```python
    EnableCommand()
    SetMotionCommand()
    GetLinearVelocity()
    GetAngularVelocity()
    GetSteeringAngle()
    GetLateralVelocity()
    GetControlMode()
    GetBatteryVoltage()
    GetErrorCode()
    GetRightWheelOdem()
    GetLeftWheelOdem()
    GetIMUAccelData()
    GetIMUGyroData()
    GetIMUYawData()
    GetIMUPichData()
    GetIMURollData()
```

#### 控制使能

- **方法名**: `EnableCommand()`
- **描述**:   使能控制命令.

#### 设置移动命令

- **方法名**: `SetMotionCommand()`
- **描述**:limo的移动控制命令.
- **Parameters**
  - `linear_vel`:(float)                   车体行进速度                                           m/s
  - `angular_vel`:(float)				车体旋转角速度(四轮差速模式有效)      rad/s 
  - `lateral_velocity`:(float)          车体横移速度(麦轮模式有效)  		        m/s 
  - `steering_angle`:(float)           转向内转角角度(阿克曼模式有效)  		rad/s 

#### 获取线速度

- **方法名**: `GetLinearVelocity()`
- **描述**:从limo获取线速度 . 
- **返回值**:linear velocity  （m/s）

#### 获取角速度

- **方法名**: `GetAngularVelocity()`
- **描述**:从limo获取角速度.
- **返回值**:angular velocity  （rad/s）

#### 获取内转角角度

- **方法名**: `GetSteeringAngle()`
- **描述**:从limo获取内转角角度.
- **返回值**:steering angle   （rad/s）

#### 获取横移速度

- **方法名**: `GetLateralVelocity()`
- **描述**:从limo获取横移速度.
- **返回值**:lateral velocity

#### 获取控制模式

- **方法名**: `GetControlMode()`
- **描述**:获取当前limo控制模式.
- **返回值**:control mode      0 待机模式 1 指令模式 3遥控模式

#### 获取左轮里程计

- **方法名**: `GetLeftWheelOdeo()`
- **描述**:获取左轮里程计信息.
- **返回值**:LeftWheelOdom   （mm）

#### 获取右轮里程计

- **方法名**: `GetRightWheelOdom()`
- **描述**:获取右轮里程计 .
- **返回值**:RightWheelOdeom (mm)

#### 获取电池电量

- **方法名**: `GetBatteryVoltage()`
- **描述**:获取电池电量信息.
- **返回值**:battery voltage      (v)

#### 获取错误代码

- **方法名**: `GetErrorCode()`
- **描述**:获取错误代码.
- **返回值**:error code                    

#### 获取加速度数据

- **方法名**: `GetIMUAccelData()`
- **描述**:获取加速度信息.
- **返回值**:IMU_accel_x,IMU_accel_y,IMU_accel_z  (0.01°)

#### 获取陀螺仪数据

- **方法名**: `GetIMUGyroData()`
- **描述**:获取陀螺仪信息.
- **返回值**:IMU_gyro_x,IMU_gyro_y,IMU_gyro_z   (0.01°)

#### 获取航向角

- **方法名**: `GetIMUYawData()`
- **描述**:获取航向角.
- **返回值**:IMU_yaw (0.01°)

#### 获取俯仰角

- **方法名**: `GetIMUPitchData()`
- **描述**:获取俯仰角.
- **返回值**:IMU_pitch (0.01°)

#### 获取横滚角

- **方法名**: `GetIMURollData()`
- **描述**:获取横滚角.
- **返回值**:IMU_roll (0.01°)

### 例子

#####  注意：如果想通过python控制LIMO,请在发送控制指令前使能控制

##### 移动到文件目录 cd /home/agilex/agilex_ws/src/limo_ros/limo_base/script,此目录下有两个.py文件，其中limomove.py可控制limo移动

#### 1.移动LIMO

```python
#!/usr/bin/env python3
# coding=UTF-8
from pylimo import limo
import time
limo=limo.LIMO()
limo.EnableCommand()         # 使能控制s
num=10
while num>0:
    limo.SetMotionCommand(linear_x=0.1)
    time.sleep(0.3)
    num-=1
```

##### 运行 python3 limomove.py实现机器人的移动，在运行此程序前请确保小车处于安全状态，退出程序命令为ctrl+z

#### 2.获取信息

```python
#!/usr/bin/env python3
# coding=UTF-8
from pylimo import limo
import time
limo=limo.LIMO()
#limo.EnableCommand()          # 没有控制LIMO 可以不使能控制
while True:                                       #循环获取
    time.sleep(0.1)
    print(limo.GetLinearVelocity())
```

#####  运行 python3 limogetmessage.py 可以通过遥控控制小车移动，查看电脑端输出的速度数据
