# Definition for singly-linked list.
# coding:utf-8

"""
    题目描述：
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

    来源：力扣（LeetCode）
"""

from typing import Optional

# 非递归实现
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 首先判断输入串是否为空
        if list1==None and list2==None:
            return None
        elif list1==None and list2!=None:
            return list2
        elif list1!=None and list2==None:
            return list1
        # 若输入串均不为空
        else:
            # 拿到初始节点，并创建一个空的下继节点
            head = ListNode()
            if list1.val>list2.val:
                head.val=list2.val
                list2 = list2.next
            else:
                head.val=list1.val
                list1 = list1.next
            temp = ListNode()
            head.next = temp
            while list1!=None or list2!=None:
                # 若两串中有一串为空，直接连接节点并终止循环即可
                if list1==None:
                    temp.val = list2.val
                    temp.next = list2.next
                    list2 = None
                elif list2==None:
                    temp.val = list1.val
                    temp.next = list1.next
                    list1 = None
                # 若两串均不为空
                # 考虑一下我们现在所拿到的节点，head(val:存在)->temp(val:无，next:None)
                # list1和list2均为下一个需要连接的节点（比较大小）
                # 那么我们需要做的是，找出list1和list2中的较小值，赋给temp，且连接下一个节点
                # temp = min(list1.val,list2.val)
                # temp.next = ListNode()
                # 在每一次循环我们均保证temp中的值为初始化并未被赋值
                # temp = temp.next
                else:
                    if list1.val>list2.val:
                        temp.val = list2.val
                        temp.next = ListNode()
                        temp = temp.next
                        list2 = list2.next
                    else:
                        temp.val = list1.val
                        temp.next = ListNode()
                        temp = temp.next
                        list1 = list1.next
            return head 

