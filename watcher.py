import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"🔁 Python file modified: {event.src_path}")
            print("🚀 Re-running intro.py...\n")
            subprocess.run(["python", "variables.py"])  # change to your script's name

if __name__ == "__main__":
    path = "."  # current directory
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        print("👀 Watching for .py changes... Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
