# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:57:45 2019

@author: David G
"""
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Defining a class which will create our linked list and also defining other utility methods
class LinkedList:
    def __init__(self):
        self.head = None

# Defining the method to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next

# Defining the method to create a node at the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
      
        # Returns data at given index in linked list 
    def getNth(self, index): 
        current = self.head # Initialise temp 
        count = 1 # Index of current node 
  
        # Loop while end of linked list is not reached 
        while (current): 
            if (count == index): 
                return current.data 
            count += 1
            current = current.next
  

  

def listLength(list):
    temp=list.head
    count=0
    while(temp):
        count+=1
        temp=temp.next
    return count
    
# Defining function which will merge two linked lists
def mergeLists(l1, l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = mergeLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeLists(l1, l2.next)
    return temp

# Defining function which will sort the linked list using mergeSort
def mergeSort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divideLists(head)
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    head = mergeLists(l1, l2)
    return head



# Defining function which will divide a linked list into two equal linked lists
def divideLists(head):
    slow = head                     # slow is a pointer to reach the mid of linked list
    fast = head                     # fast is a pointer to reach the end of the linked list
    if fast:
        fast = fast.next            
    while fast:
        fast = fast.next            # fast is incremented twice while slow is incremented once per loop
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None 
    return head, mid

def is_sorted(list1):
    node = list1.head
    while node and node.next:
        if node.data > node.next.data:
            return False
        else:
            node = node.next

    return True

def bubble_sort(list1):
    """Sorts a list of numbers using bubble sort."""
    needSorting= True
    while needSorting:
    
        # comparing 2 at a time, skipping ahead
        node = list1.head
        needSorting= False
        while node.next is not None:
            # loop through comparing node to the next
            if node.next.data < node.data:
                # if the next is greater, then we need to swap
                node.data, node.next.data= node.next.data, node.data
                # oops, looks like we have to scan again
                needSorting = True
            node = node.next
def partition(l1):
    pivot=l1.head
    loList=LinkedList()
    hiList  = LinkedList()
    
    if pivot.data > pivot.next.data:
        loList.append(pivot.next.data)
    else:
        hiList.append(pivot.next.data)
    if isEmpty(loList)==True:
        loList.head=pivot
    if isEmpty(hiList)==True:
        loList.tail=pivot
    return loList, hiList
def quickSort(listOne):
    if listOne.head== None or listOne.head.next== None:
        return listOne.head
    l=LinkedList()
    l1= LinkedList()
    l2 =LinkedList() 
    l1, l2 = partition(listOne)
    l1= quickSort(l1)
    l2= quickSort(l2)
    if  isEmpty(l1)==True:
        l2.head=l.head 
        l.tail=l2.tail
    if isEmpty(l2)==True:
        l.head=l1.head
    else:
        l.head = l1.head
        l2.head= l1.tail
        l.tail= l2.tail
        
  
    return l
# The main logic starts from here
if __name__ == '__main__':

    list1 = LinkedList()   
for i in range (0,7):                # Creating a linked list
    list1.append(random.randint(1,101))   # Assigning Random values

medianIndx=listLength(list1)//2
print ("Linked list before sorting")
list1.printList()                       # Printing the unsorted linked list
list1.head = mergeSort(list1.head)      # Applying mergeSort to linked list
print ("Linked list after Merge Sort")  # Applying mergeSort to linked list
list1.printList()   # Printing the sorted linked list
print ("Linked list after BubbleSort Sort")  
bubble_sort(list1)
list1.printList()                    
print("this is the length:",listLength(list1))
print( )
n = medianIndx+1
print ("Median is :", list1.getNth(n))
    
