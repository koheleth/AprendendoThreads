#!/usr/bin/python
# -*- coding: utf-8 -*
"""
Exemplo tirado do site:
https://imasters.com.br/back-end/threads-em-python
Autor Original: Breno Leitão

Modificado por: Koheleth(Aurélio)
Fiz adaptação e correções do python 2 para o python 3
O interessante desse exempo é a sincronização de threads
Isso ajuda bastante em alguns trabalhos que precisamos
saber quando terminam, e que terminem todas as threads
Código precisa de ainda alguma correções
"""
from threading import Thread
import random
import sys

NUM_VALUES = 1000
NUM_THREADS = 4
values = []
sequential_total = 0
threaded_total = 0
threads = []


class Th(Thread):
    subtotal = 0

    def __init__(self, num):
        sys.stdout.write("Making thread number " + str(num) + "\n")
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num

    def run(self):
        range_start = self.num * NUM_VALUES / NUM_THREADS
        range_end = ((self.num + 1) * NUM_VALUES / NUM_THREADS) - 1

        for i in range(range_start, range_end):
            self.subtotal += values[i]
            sys.stdout.write("Subtotal for thread " + str(self.num) +
                             ": " + str(self.subtotal)
                             + " (from " + str(range_start)
                             + " to " + str(range_end) + ")\n");
            sys.stdout.flush()

    def get_subtotal(self):
        return self.subtotal


def main():
    global sequential_total
    global threaded_total
    global NUM_VALUES
    global values
    global threads
    global NUM_THREADS

    for i in range(NUM_VALUES):
        values.append(random.randint(0, 100))

    for i in range(NUM_VALUES):
        sequential_total += values[i]

    print("Sequential total: " + str(sequential_total))

    for thread_number in range(NUM_THREADS):
        threads.insert(thread_number, Th(thread_number))
        threads[thread_number].start()

    for thread_number in range(NUM_THREADS):
        threads[thread_number].join()
        threaded_total += threads[thread_number].get_subtotal()

    print("Threaded total: " + str(threaded_total))


if __name__ == '__main__':
    main()
