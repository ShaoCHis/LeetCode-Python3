# coding:utf-8

"""
    题目描述：
    给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
    如果可以，返回 true ；否则返回 false 。
    magazine 中的每个字符只能在 ransomNote 中使用一次。

    来源：力扣（LeetCode）
"""

import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 利用collections对词频单词频率进行统计，返回字典
        ransom = collections.Counter(ransomNote)
        maga = collections.Counter(magazine)
        # 对ransom中出现的字符在maga中进行判断
        for item in ransom.keys():
            # 若ransom中的字符在maga中并未出现，则直接返回false
            if item not in maga.keys():
                return False
            # 若ransom中的字符出现次数大于maga中出现次数，直接返回false
            elif ransom[item]>maga[item]:
                return False
        # 将ransom中所有字符判断完毕后则返回true
        return True