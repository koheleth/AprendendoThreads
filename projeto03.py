#!/usr/bin/python
# -*- coding: utf-8 -*
"""
Exemplo tirado do site:
https://imasters.com.br/back-end/threads-em-python
Autor Original: Breno Leitão

Modificado por: Koheleth(Aurélio)
Fiz adaptação e correções do python 2 para o python 3
O interessante desse exempo é a possibilidade de criar várias threads
Isso ajuda bastante em alguns trabalhos que precisamos
saber quando terminam, e que terminem todas as threads
"""
# from threading import Thread
import threading
import sys

COUNTDOWN = 20


class Th(threading.Thread):
    def __init__(self, num):
        # esse tipo de saida por vezes melhor que o print
        # pelo fato do print ter threads no seu código
        # ----
        sys.stdout.write(f'Fazendo Thread number {num}\n')
        sys.stdout.flush()
        threading.Thread.__init__(self)
        self.num = num
        self.countdown = COUNTDOWN

    def run(self):
        while self.countdown:
            sys.stdout.write(f'Thread {self.num} ({self.countdown})\n')
            sys.stdout.flush()
            self.countdown -= 1


def main():
    # Podemos criar várias threads desta forma
    # um bom exemplo para cálculos com valores grandes e sequenciais
    for thread_number in range(10):
        thread = Th(thread_number)
        thread.start()


if __name__ == '__main__':
    main()
