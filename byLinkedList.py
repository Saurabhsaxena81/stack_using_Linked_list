class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    
class stack:
    def __init__(self):
        self.top=None

    #to check whether thestac is empty or not and it returns boolean True or false
    def isempty(self):
        return self.top==None
    
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node

    def traverse(self):
        temp=self.top
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def peak(self):
        if(self.isempty()):
            return "Empty"
        else:
            return self.top.data
    def pop(self):
        if(self.isempty()):
            return 'Stack empty'
        else:
            self.top=self.top.next
    def size(self):
        pos=0
        if(self.isempty()):
            return 'Stack empty'
        else:
            temp=self.top
            while temp!=None:
                pos+=1
                temp=temp.next
        return pos



s=stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.size())
s.pop()
s.pop()
s.pop()
print(s.peak())
s.pop()
s.pop()
print(s.pop())
s.traverse()
print(s.isempty())