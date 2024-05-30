import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:/Users/tj811/OneDrive/Documents/Projects/Python/projects/Project 103/New folder"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
        
    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved!")

    def on_deleted(self, event):
        print(f"Hey, {event.src_path} has been deleted!")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified!")
    
event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        print("running..")
        time.sleep(2)

except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
