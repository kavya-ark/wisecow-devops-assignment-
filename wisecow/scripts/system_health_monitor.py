import psutil
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def monitor_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())

    print("=" * 50)
    print("System Health Report")
    print(f"Time: {datetime.now()}")
    print("=" * 50)
    print(f"CPU Usage      : {cpu}%")
    print(f"Memory Usage   : {memory}%")
    print(f"Disk Usage     : {disk}%")
    print(f"Running Processes : {processes}")
    print()

    if cpu > CPU_THRESHOLD:
        print("ALERT: CPU usage exceeded threshold!")

    if memory > MEMORY_THRESHOLD:
        print("ALERT: Memory usage exceeded threshold!")

    if disk > DISK_THRESHOLD:
        print("ALERT: Disk usage exceeded threshold!")

if __name__ == "__main__":
    monitor_system()
