### ADB命令
##### 显示系统中全部设备

```
adb devices
这个命令是查看当前连接的设备, 连接到计算机的android设备或者模拟器将会列出显示
```
##### 安装一个apk 

```
adb install -r (APK路径) 
-r 代表如果apk已安装，重新安装apk并保留数据和缓存文件。apk路径则可以直接将apk文件拖进cmd窗口，记得加空格
```
##### 直接卸载

```
adb uninstall (apk包名)
卸载 app 但保留数据和缓存文件
```
##### 清除应用数据与缓存

```
adb shell pm clear （apk包名）
```
##### 强制停止应用 

```
adb shell am force-stop （apk包名）
```
##### 重启设备

```
adb reboot
```

##### 删除文件

```
adb shell 
cd sdcard/model/book
ls 
rm -r 415
```
##### pull和push文件 

```
adb push (文件路径) (想要push的路径) 
adb pull (文件路径) (想要pull的路径) 
```
##### 查看日志

```
adb logcat -v threadtime
```
##### 过滤日志

```
adb logcat -v threadtime | grep (关键字)
```

##### 投屏(用于电脑控制设备)

```
打开vysor
adb shell am start -n com.android.settings/com.android.settings.Settings
```
##### 查看内存占用

```
adb shell
dumpsys meminfo
```
##### 动态查看CPU&内存占用

```
adb shell
top -m 10 -s cpu
```

##### 本地批量推送绘本到sdcard

```
adb push ./book /sdcard/model/book
```
