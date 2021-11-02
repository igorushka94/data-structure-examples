# Пример реализации очереди в python
# Example realization queue in python

import queue

q_fifo = queue.Queue(maxsize=3)   # FIFO queue class in module
q_lifo = queue.LifoQueue(maxsize=0)  # LIFO queue class in module
q_priority = queue.PriorityQueue(maxsize=0)     # Приоритетная очередь
q_simple_queue = queue.SimpleQueue()    # Неограниченная FIFO очередь
"""
max_size - верхнее ограничение на количество элементов, которые
могут быть помещены в очередь
"""


"""
    #General questions on interview#
Обратить первые k элементов очереди.
Реализуйте очередь, используя связанный список.
Реализуйте стек с помощью очереди.
"""


def f1():
    print('i task №1')


def f2():
    print('i task №2')


def f3():
    print('i task №3')


# q_fifo.put(f3)
# q_fifo.put(f2)
# q_fifo.put(f1)
# print(dir(q_fifo))
