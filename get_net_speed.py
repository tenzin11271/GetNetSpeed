import psutil
import time

def get_net_speed():
    old_value = psutil.net_io_counters().bytes_recv
    while True:
        time.sleep(1)
        new_value = psutil.net_io_counters().bytes_recv
        print(f"当前下载速度: {(new_value - old_value) / 1024 / 1024:.2f} MB/s")
        old_value = new_value

get_net_speed()
