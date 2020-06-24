#算法题，算法题，反转字符串
#  算法题，字符串中大小写字母分成前后两部分，字母顺序不变

'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
'''
class Solution:
    def reverseString(self,s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s[:]=s[::-1]
        #s.reverse()
        def helper(left,rigt):
            if left < right:
                s[left], s[right] = s[right],s[left]
                helper(left+1, right -1)
        helper(0,len(s)-1)

