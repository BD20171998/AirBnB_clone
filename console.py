#!/usr/bin/python3
import cmd, sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class for hbnd interpreter"""
    prompt = '(hbnb)'
    file = None

    def do_quit(self):
        """Command to quit"""
        return True

    def do_EOF(self, arg):
        """Command to exit program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file"""
        if len(arg) < 2:
            print("** class name missing **")
            return

        if type(arg[2]) != "BaseModel":
            print("** class doesn't exist **")
            return

        inst = self.BaseModel()
        print(inst.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
