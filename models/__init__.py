#!/usr/bin/python3
'''The init Module in Models Directory'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
