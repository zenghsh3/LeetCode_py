"""
push:
    enqueue in queue2
    enqueue all items of queue1 in queue2, then switch the names of queue1 and queue2
pop:
    deqeue from queue1
"""
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = [] 
        self.q2 = []
        self.flag = True

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.flag:
            self.q2.append(x) 
            while self.q1:
                self.q2.append(self.q1[0])
                del self.q1[0]
        else:
            self.q1.append(x) 
            while self.q2:
                self.q1.append(self.q2[0])
                del self.q2[0]

        self.flag = not self.flag


    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
            if self.flag:
                del self.q1[0]
            else:
                del self.q2[0]

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            if self.flag:
                return self.q1[0]
            else:
                return self.q2[0]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.q1 and not self.q2:
            return True
        else:
            return False

if __name__ == '__main__':
   stk = Stack() 
   stk.push(0)
   stk.push(1)
   stk.pop()
   print stk.top()
   print stk.empty()
   stk.push(2)
   print stk.top()
