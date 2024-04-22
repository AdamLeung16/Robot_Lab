# Robot_Lab

## lab1

```shell
# /catkin_ws
source devel/setup.bash
catkin_make
roslaunch differential_4-wheeled_car differential_4-wheeled_car.launch
roslaunch differential_4-wheeled_car_control keyboard.launch
```

## lab2

|参数 | 值 | 参数 | 值| 参数 | 值 |
|-|-|-|-|-|-|
$K_p\_long$ |  0.95 |$K_p\_lat$ |  4.2 |$K_p\_ang$ |  4.3|
$K_i\_long$  | 0.36 |$K_i\_lat$  | 0.16 |$K_i\_ang$  | 0.36|
$K_d\_long$ | 0 | $K_d\_lat$ | 0|$K_d\_ang$ | 0|

```shell
catkin_make
source devel/setup.bash
roslaunch tracking_pid test_tracking_pid.test rviz:=true
rosrun rqt_reconfigure rqt_reconfigure 
```