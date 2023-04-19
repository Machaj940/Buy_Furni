#!/usr/bin/python3
"""This file contains the entry point of the Buy_furni command interpreter"""


import cmd


class Buy_furni_Command(cmd.Cmd):
    """simple framework for writing line-oriented Hbnb command interpreter"""
    prompt = "(Buy_Furni) "


    def emptyline(self):
        pass

    def do_quit(self, args):
        """Exits from the console"""
        return True

    def do_EOF(self, args):
        """Gives a clean way to exit interpretor"""
        return True


if __name__ == '__main__':
    Buy_furni_Command().cmdloop()
