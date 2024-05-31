import psutil
import logging
import time

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 100  # Example threshold for the number of processes

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')

    # Check memory usage
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_info.percent}%')

    # Check disk usage
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        logging.warning(f'High disk usage detected: {disk_info.percent}%')

    # Check number of running processes
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f'High number of running processes detected: {process_count}')

def main():
    while True:
        check_system_health()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
