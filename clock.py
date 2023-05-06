# 导入sys模块和time模块
import sys
import time

# 定义专注时钟函数，接收两个参数：专注时间和休息时间
def focus_clock(focus_time, break_time):
    # 将参数转换为整数类型
    focus_time = int(focus_time)
    break_time = int(break_time)
    # 循环执行专注和休息
    while True:
        # 打印开始专注的提示信息
        print(f"开始专注{focus_time}分钟！")
        # 计时专注时间，并在每分钟打印剩余时间
        for i in range(focus_time):
            time.sleep(60) # 等待一分钟
            print(f"还剩{focus_time - i - 1}分钟！")
        # 打印结束专注的提示信息
        print(f"专注结束，休息{break_time}分钟！")
        # 计时休息时间，并在每分钟打印剩余时间
        for i in range(break_time):
            time.sleep(60) # 等待一分钟
            print(f"还剩{break_time - i - 1}分钟！")
        # 打印开始下一轮专注的提示信息
        print("开始下一轮专注！")

# 获取命令行参数，第一个参数为专注时间，第二个参数为休息时间
focus_time = sys.argv[1]
break_time = sys.argv[2]
# 调用专注时钟函数，传入命令行参数
focus_clock(focus_time, break_time)
