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

| 参数          | 值   | 参数         | 值   | 参数         | 值   |
| ------------- | ---- | ------------ | ---- | ------------ | ---- |
| $K\_p\_long$ | 0.95 | $K\_p\_lat$ | 4.2  | $K\_p\_ang$ | 4.3  |
| $K\_i\_long$ | 0.36 | $K\_i\_lat$ | 0.16 | $K\_i\_ang$ | 0.36 |
| $K\_d\_long$ | 0    | $K\_d\_lat$ | 0    | $K\_d\_ang$ | 0    |

```shell
catkin_make
source devel/setup.bash
roslaunch tracking_pid test_tracking_pid.test rviz:=true
rosrun rqt_reconfigure rqt_reconfigure 
```

## lab3

1. slam扫描建图
   autocar.launch解注释掉“雷达扫描建图步骤”部分，注释掉“显示地图步骤”部分

   ```shell
   roslaunch differential_4-wheeled_car autocar.launch 
   ```
2. 地图映射

   ```shell
   roslaunch differential_4-wheeled_car map_listener.launch 
   ```
3. 保存地图

   ```shell
   roslaunch differential_4-wheeled_car save_map.launch 
   ```
4. 确定起点终点，Astar找路径，pid控制小车运动
   autocar.launch解注释掉“显示地图步骤”部分，注释掉“雷达扫描建图步骤”部分

   ```shell
   roslaunch differential_4-wheeled_car autocar_show.test 
   ```
   2d navi箭头确定终点，将调用find_path，输出起点终点坐标，输出路径坐标列表，更新path.yaml，调用autocar_run.test实现小车运动
