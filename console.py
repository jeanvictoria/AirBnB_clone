#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Hbnbc command'''
    prompt = '(hbnb)'
    file = None

    def do_EOF(self, line):
        """ Exit the program in EOF"""
        return True

    def do_quit(self, line):
        """ quit commad to exit """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
