 Implement a min heap data structure. For the parent and left/right functions use bit manipulation operators. In addition your heap should have the following functionality

 code:[heapify.py](https://github.com/mounikamittapalli/DAA_Handson5/blob/3fe59ce720a3f8429a4b64e5b2586142582a8c76/heapify.py)

 output:[img](https://github.com/mounikamittapalli/DAA_Handson5/blob/3fe59ce720a3f8429a4b64e5b2586142582a8c76/717DF07D-5E20-4AD8-9378-D11F81848617.jpeg)

The ability to initially build the heap (build_min_heap)
The ability to heapify
def heapify(self,i)

The ability to get and remove ("pop") the root node from the heap (and of course re-heapify everything)
Implemented below functions
def get_root_element(self)-To get current root element
def remove(self)-To remove root node
def insert(self, value)-To insert value

The heap should be generic to the type of data (can store floats, int, custom datastructure)
-refere output 1 & 2 
Show example(s) of your heap working. Please demonstrate ALL the functionality you implemented.
