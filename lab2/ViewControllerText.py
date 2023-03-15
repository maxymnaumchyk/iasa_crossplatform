import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from Model import TodoModel

class MainWindow():
    def __init__(self):
        self.model = TodoModel()

    def add(self,text):
        if text: # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            self.save()

    def delete(self,index):
        if index:
            # Remove the item and refresh.
            del self.model.todos[index]
            self.save()

    def complete(self,index):
        status, text = self.model.todos[index]
        self.model.todos[index] = (True, text)
        self.save()

    def show(self):
        print(self.model.todos)

    def load(self):
        try:
            with open('data.db', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.db', 'w') as f:
            data = json.dump(self.model.todos, f)