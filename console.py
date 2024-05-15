#!/usr/bin/python3
"""Module for console.py."""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print() 
        return True

    def emptyline(self, line):
        """Do nothing on empty input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
