# !/usr/bin/env python
# *-* coding:utf-8 *-*

import heapq
import threading

REMOVED = '<removed-task>'

class InnerError(Exception):
    pass

class Tools(object):

    @property
    def priority_queue(self):
        return _PriorityQueue()

class _WrapperList(object):

    def __init__(self, sequeue):
        self._sequeue = sequeue

    @property
    def len(self):
        return len(self._sequeue)

    def nlargests(self, n):
        pass

    def nsmallest(self, n):
        pass


class _PriorityQueue(object):

    def __init__(self):
        self._queue = []
        self._sentinel = 0
        self._task_lock = threading.RLock()
        self.finder_dict = {}

    @property
    def queue(self):
        return self._queue

    def add_tasks(self, sequeue, priority=0):
        with self._task_lock:
            for task in sequeue:
                self.add_task(task, priority)

    def add_task(self, task, priority=0):
        with self._task_lock:
            if task in self.finder_dict:
                raise InnerError('the task exist')
            entry = [priority, self._sentinel, task]
            self._sentinel += 1
            self.finder_dict[task] = entry
            heapq.heappush(self._queue, entry)

    def pop_task(self):
        with self._task_lock:
            while self._queue:
                _, _, task = heapq.heappop(self._queue)
                if task is not REMOVED:
                    del self.finder_dict[task]
                    return task
        raise KeyError('pop from an empty priority queue')

    def modify_priority(self, task, priority=0):
        with self._task_lock:
            if task in self.finder_dict:
                entry = self.finder_dict[task]
                entry[-1] = REMOVED
                new_entry = [priority, self._sentinel, task]
                self.finder_dict[task] = new_entry
                heapq.heappush(self._queue, new_entry)
            else:
                raise InnerError('the task does not exist')

    def query_task_priority(self, task):
        if task in self.finder_dict:
            return self.finder_dict[task][0]
        raise InnerError('the task does not exist')

    def query_all_prioritys(self):
        priority_set = set()
        for _, entry in self.finder_dict.iteritems():
            priority_set.add(entry[0])
        return list(priority_set)

# t = _PriorityQueue()
# t.add_task(task='first', priority=1)
# print t.pop_task()
# t = Tools()
# p = t.priority_queue
# p.add_tasks(['first', 'second', 'third'])
# p.add_task('forth', priority=1)
# print p.query_all_prioritys()
# print p._queue
# p.modify_priority('fifth', priority=2)
# print p.query_all_prioritys()
# print p._queue
# print p.pop_task()
# print p.pop_task()
# print p.pop_task()
# print p.pop_task()
# p.modify_priority('first', priority=2)
