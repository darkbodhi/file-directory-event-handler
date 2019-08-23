import sys
import time
from watchdog.observers import Observer


f = open("./config.ini", "r")
for basic_app_event_handler in f:
    required_handler = basic_app_event_handler
f.close()

src_path = './test_folder'


class FileWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = required_handler
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )


if __name__ == "__main__":
    src_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    FileWatcher(src_path).run()
