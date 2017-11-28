# !/usr/bin/env python
# *-* coding:utf-8 *-*

import heapq
import threading

class ExistError(Exception):
    pass

class Tools(object):
    pass


class _PriorityQueue(object):

    def __init__(self):
        self._queue = []
        self._sentinel = 0
        self._task_lock = threading.RLock()
        self.finder_dict = {}

    def add_tasks(self, sequeue):
        pass

    def add_task(self, task, priority=0, reverse=False):
        with self._task_lock:
            if task in self.finder_dict:
                raise ExistError('the task exist')
            entry = [priority, self._sentinel, task]
            self._sentinel += 1
            self.finder_dict[task] = entry
            heapq.heappush(self._queue, entry)

    def pop_task(self):
        with self._task_lock:
            pass

    def modify_priority(self, task, priority=0):
        with self._task_lock:
            if task in self.finder_dict:
                entry = self.finder_dict[task]