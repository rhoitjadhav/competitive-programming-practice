# Add Two Numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        last = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, remainder = divmod(val1+val2 + carry, 10)    
                      
            last.next = ListNode(remainder)
            last = last.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


if __name__ == "__main__":
    s = Solution()
    
    a = ListNode(8)
    b = ListNode(9)
    # c = ListNode(3)

    l1 = a
    a.next = b
    # b.next = c

    a = ListNode(0)
    # b = ListNode(6)
    # c = ListNode(4)

    l2 = a
    # a.next = b
    # b.next = c

#     l3 = s.addTwoNumbers(l1, l2)
#     while(l3):
#         print(l3.val)
#         l3 = l3.next


# # In order to solve this problem we use python decorator 

# def validate_params(func):
#     # Validation code goes here
#     def wrapper(age, name):
#         if not isinstance(age, int) or not isinstance(name, str):
#              raise TypeError
        
#         if age < 0:
#              raise ValueError
        
#         if name == '':
#             raise ValueError
#         return func(age, name)
    
#     return wrapper


# @validate_params
# def user(age, name):
#     print("Name: {}".format(name))
#     print("Age: {}".format(age))


# import numpy as np 
  
# minn, maxx = tuple(map(int, input("Enter min and max numbers: ").split()))

# output = np.random.randint(low = minn, high = maxx, size = (3, 3))

# print(output)

json_data = [
    {
        "client": {
            "00:20:90:B3:16:25": {
                "conID": "",
                "encryption": "NA",
                "IsValid": 1,
                "lastaccessed": 1594356454,
                "numberofclients": [10]
            },
            "1E:51:A4:D4:B7:29": {
                "conID": "",
                "encryption": "WPA Mixed PSK (CCMP TKIP)",
                "IsValid": 1,
                "lastaccessed": 1594356448,
                "numberofclients": [24]
            }
        }
    }
]

# Accesing the 12 digit id and encryption method through the following snippet

data = {}
for d in json_data:
    for i in d:
        data[i] = {}
        for j in d[i]:
            data[i]['12_digit_code'] = j
            data[i]['encryption'] = d[i][j]['encryption']

print(data)

