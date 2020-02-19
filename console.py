#!/usr/bin/python3
import cmd, sys, json, shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for hbnd interpreter"""
    prompt = '(hbnb) '

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name
        """
        args = arg.split(' ')
        valid_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                         'Place', 'Review']

        if len(arg) == 0:
            for key in storage.all():
                obj = storage.all()[key]
                print(obj)
            return

        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return

        else:
             for key in storage.all():
                obj = storage.all()[key]
                if obj.__class__.__name__ == args[0]:
                    print(obj)
             return

    def do_quit(self, arg):
        """Command to quit"""
        return True

    def do_EOF(self, arg):
        """Command to exit program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file"""
        args = shlex.split(arg)
        valid_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                         'Place', 'Review']

        if len(args) < 1:
            print("** class name missing **")
            return

        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return

        if args[0] == "BaseModel":
            inst = BaseModel()
            inst.save()
            print(inst.id)

        if args[0] == "User":
            inst = User()
            inst.save()
            print(inst.id)

        if args[0] == "State":
            inst = State()
            inst.save()
            print(inst.id)

        if args[0] == "City":
            inst = City()
            inst.save()
            print(inst.id)

        if args[0] == "Amenity":
            inst = Amenity()
            inst.save()
            print(inst.id)

        if args[0] == "Review":
            inst = Review()
            inst.save()
            print(inst.id)

        if args[0] == "Place":
            inst = Place()
            inst.save()
            print(inst.id)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id, saves the change
        into the JSON file)
        """
        args = shlex.split(arg)
        valid_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                         'Place', 'Review']

        if len(args) < 1:
            print("** class name missing **")
            return

        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return

        if args[0] in valid_classes and len(args) < 2:
            print("** instance id missing **")
            return

        show_obj =  args[0]+"."+args[1]

        try:
            del storage.all()[show_obj]
            storage.save()

        except:
            print("** no instance found **")
            return

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id
        """
        args = shlex.split(arg)
        valid_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                         'Place', 'Review']

        if len(args) < 1:
            print("** class name missing **")
            return

        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return

        if args[0] in valid_classes and len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()

        show_obj =  args[0]+"."+args[1]

        try:
            print(all_objs[show_obj])

        except:
            print("** no instance found **")
            return

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute (save the change into the JSON file)
        """
        args = shlex.split(arg)
        valid_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                         'Place', 'Review']

        if len(args) < 1:
            print("** class name missing **")
            return

        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return

        if args[0] in valid_classes and len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()

        show_obj =  args[0]+"."+args[1]

        try:
            json_dict_update = all_objs[show_obj]

        except:
            print("** no instance found **")
            return

        attribs = json_dict_update.__dict__.keys()

        if len(args) < 3 or args[2] not in attribs:
            print("** attribute name missing **")
            return

        if len(args) == 3 or args[3] == None:
            print("** value missing **")
            return

        json_dict_update.__dict__[args[2]] = args[3]

        json_dict_update.save()

    def emptyline(self):
        """skips line when command is empty"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
