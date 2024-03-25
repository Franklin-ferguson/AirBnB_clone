#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import cmd
import shlex
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


"""
command line interface for testing Airbnb clone application
"""


class HBNBCommand(cmd.Cmd):
    """
    Represents a class called HBNBCommand
    """

    all_classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """
        Quits the program
        """
        return True

    def do_EOF(self, arg):
        """
        end of file and quits the program
        """
        print()
        return True

    def do_help(self, arg):
        """
        gives you more info about a command
        """
        print("Quit command to exit the program")

    prompt = "(hbnb)"

    def default(self, arg):
        """
        updating cmd to accept <class name>.all()
        """
        input_command_list = arg.split(".")

        input_class_name = input_command_list[0]

        input_method = input_command_list[1]

        input_method_command = input_method.split("(")

        command_method = input_method_command[0]

        command_dict = {
            "update": self.do_update,
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
        }

        if command_method in command_dict.keys():
            return command_dict[command_method]("{} {}".format(input_class_name, ""))

        print("Incorrect syntax: {}***".format(arg))
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        command_passed = shlex.split(arg)

        if len(command_passed) == 0:
            print("** class name missing **")

        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")

        else:
            new_instance = eval(f"{command_passed[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        command_passed = shlex.split(arg)

        if len(command_passed) == 0:
            print("** class name missing **")

        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")

        elif len(command_passed) < 2:
            print("** instance id missing **")

        else:
            all_objects = storage.all()

            key = "{}.{}".format(command_passed[0], command_passed[1])

            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file)
        """

        command_passed = shlex.split(arg)

        if len(command_passed) == 0:
            print("** class name missing **")

        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")

        elif len(command_passed) < 2:
            print("** instance id missing **")

        else:
            all_objects = storage.all()
            key = "{}.{}".format(command_passed[0], command_passed[1])
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """

        command_passed = shlex.split(arg)
        all_objects = storage.all()

        if len(command_passed) == 0:
            for key, value in all_objects.items():
                print(str(value))
        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")
        else:
            for key, value in all_objects.items():
                if key.split(".")[0] == command_passed[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """

        command_passed = shlex.split(arg)

        if len(command_passed) == 0:
            print("** class name missing **")

        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")

        if len(command_passed) < 2:
            print("** instance id missing **")

        else:
            all_objects = storage.all()

            key = "{}.{}".format(command_passed[0], command_passed[1])

            if key not in all_objects:
                print("** no instance found **")

            elif len(command_passed) < 3:
                print("** attribute name missing **")

            elif len(command_passed) < 4:
                print("** value missing **")

            else:

                inst_object = all_objects[key]

                attribute_one = command_passed[2]

                attribute_two = command_passed[3]

                try:
                    attribute_two = eval(attribute_two)

                except Exception:
                    pass

                setattr(inst_object, attribute_one, attribute_two)

                inst_object.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
