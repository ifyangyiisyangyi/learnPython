function now(){
    echo [`date "+%Y-%m-%d %H:%M:%S"`] $@
}
function send(){
    # now $*
    adb shell sendevent /dev/input/event$1 1 $2 $3
    adb shell sendevent /dev/input/event$1 0 0 0
}
# suite
function nose(){
    now "开始-点击鼻子"
    send 4 28 1
    send 4 28 0
    now "结束-点击鼻子"
    sleep 1
}
function head(){
    now "摸头"
    send 5 220 1
    send 5 220 0
}
function tummy(){
    now "短按luka 肚子贴片"
    send 5 216 1
    send 5 216 0
}
function vol_up(){
    now "音量加大"
    send 4 115 1
    send 4 115 0
}
function vol_down(){
    now "音量减小"
    send 4 114 1
    send 4 114 0
}
function wifi(){
    now "wifi"
    send 3 139 1
    # now "左翅膀139-1"
    send 4 102 1
    # now "右翅膀102-1"
    sleep 2
    send 3 139 0
    # now "左翅膀139-0"
    send 4 102 0
    # now "右翅膀102-0"
}
function combination_ota(){
    wifi
    now "组合键升级"
    send 3 139 1
    send 4 102 1
    send 4 28 1
    sleep 2
    send 3 139 0
    send 4 102 0
    send 4 28 0
}

function right_key(){
	now "点右翅膀"
	send 4 102 1
	send 4 102 0
}
# wifi
# nose
# combination_ota
# sleep 10
# nose
# head
# sleep 2
# nose>
# sleep 2
# tummy
# sleep 2
# for i in {1..12}
#     do
#         # echo $i
#         vol_down
#     done
# for i in {1..12}
#     do
#         # echo $i
#         vol_up
#     done



for i in {1..200}
    do
        echo $i
		sleep 1
        right_key
    done
sleep 5
nose


