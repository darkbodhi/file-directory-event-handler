from watchdog.events import FileSystemEventHandler

src_path = "./test_folder"


class FileEventHandler(FileSystemEventHandler):

    def init(self):
        super().__init__(self)

    def dispatch(self, event):
        pass

    def on_created(self, event):
        print('A subdirectory or a file was created.')

    def on_deleted(self, event):
        f = open("delete_message.txt" "w+")
        f.close()

    def on_modified(self, event):
        f = open("modification_message.txt" "w+")
        r = open("modification_message.txt" "a")
        r.write("File was modified!")
        r.close()
        f.close()
