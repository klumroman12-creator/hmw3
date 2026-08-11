import sys

def parse_log_line(line: str) -> dict:
    line = line.strip()
    line = line.split(' ', maxsplit=3)
    line = {'date': line[0], 'times' : line[1], 'level' : line[2], 'message' : line[3]}
    return line
      
    
def load_logs(file_path: str) -> list:
    try:
        logs = []
        with open(file_path, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = parse_log_line(line)
                logs.append(line)
        return logs 
    except FileNotFoundError:
          print("File not Found, please try again")


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        if log['level'] in counts:
            counts[log['level']] += 1
        else:
            counts[log['level']] = 1
    return counts  


def filter_logs_by_level(logs: list, level: str) -> list:
     return[log for log in logs if log['level'] == level.upper()]

def display_log_counts(counts: dict):
     print(f"{'Рівень логування':<17} | {'Кількість':<10}")
     print("-" * 18 + "|" + "-" * 11)
     for level, count in counts.items():
        print(f"{level:<17} | {count:<10}")


def main():
    # Перевірка наявності аргументів командного рядка
    if len(sys.argv) < 2:
        print("Використання: python dz3.3.py <шлях_до_файлу> [рівень]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        return

    # 1. Підрахунок та вивід таблиці
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # 2. Перевірка чи передано другий необов'язковий аргумент (наприклад, 'error')
    if len(sys.argv) > 2:
        filter_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, filter_level)

        print(f"\nДеталі логів для рівня '{filter_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()