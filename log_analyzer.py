# Log Analyzer that detects suspicious keywords in a log file

def analyze_log(file_path):
    keywords = ["error", "failed", "unauthorized", "invalid", "denied"]

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            print("Suspicious entries:")
            for line in lines:
                if any(word.lower() in line.lower() for word in keywords):
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found.")

# Example: logs.txt
path = input("Enter path to log file: ")
analyze_log(path)
