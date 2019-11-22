#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-
"""

Jogo da velha

Licensa:

Copyright 2017 E. S. Pereira
"""

from curses import initscr, wrapper
from random import randint

def main(stdscr):
    pass

if __name__ == "__main__":
    initscr()
    wrapper(main)

def boas_vindas(stdscr):
    stdscr.addstr(1, 1, "Bem-vindo ao Jogo da Velha")
    stdscr.addstr(2, 1, "Pressione q para sair ou h para obter ajuda")