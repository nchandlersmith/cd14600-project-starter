"""Simple logger class"""

class Logger():
    @staticmethod
    def log(message):
        log_message = f"[LOG] {message}"
        print(log_message)
        return log_message