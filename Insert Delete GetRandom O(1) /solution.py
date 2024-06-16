import random
class RandomizedSet:
   
    def __init__(self):

        self.dic={}
        self.my_list=[]
        

    def insert(self, val: int) -> bool:
        
        if val in self.dic:
            return False
        self.dic[val]=len(self.my_list)
        self.my_list.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        index = self.dic[val]
        self.my_list[index] = self.my_list[-1]
        self.dic[self.my_list[-1]] = index
        self.my_list.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        num = random.choice(self.my_list)
        return num 


