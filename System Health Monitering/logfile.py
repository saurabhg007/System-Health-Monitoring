import re
from collections import defaultdict

log_file_path = 'access.log'  # Path to the web server log file

def parse_log(log_file):
    with open(log_file, 'r') as file:
        log_lines = file.readlines()
    return log_lines

def analyze_logs(log_lines):
    ip_requests = defaultdict(int)
    page_requests = defaultdict(int)
    error_404_count = 0

    for line in log_lines:
        # Extract IP address
        ip_match = re.match(r'(\d+\.\d+\.\d+\.\d+)', line)
        if ip_match:
            ip = ip_match.group(1)
            ip_requests[ip] += 1

        # Extract requested page
        page_match = re.search(r'\"GET\s(\/\S*)\sHTTP\/', line)
        if page_match:
            page = page_match.group(1)
            page_requests[page] += 1

        # Count 404 errors
        if ' 404 ' in line:
            error_404_count += 1

    return ip_requests, page_requests, error_404_count

def generate_report(ip_requests, page_requests, error_404_count):
    print("Log Analysis Report")
    print("===================")
    print(f"Total 404 errors: {error_404_count}")
    print("\nTop 5 Requested Pages:")
    for page, count in sorted(page_requests.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"{page}: {count} requests")
    print("\nTop 5 IP Addresses:")
    for ip, count in sorted(ip_requests.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"{ip}: {count} requests")

def main():
    log_lines = parse_log(log_file_path)
    ip_requests, page_requests, error_404_count = analyze_logs(log_lines)
    generate_report(ip_requests, page_requests, error_404_count)

if __name__ == "__main__":
    main()
