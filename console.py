#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Hbnbc command'''
    prompt = '(hbnb)'
    file = None
