class DynamicArray:
    
    def __init__(self, capacity: int):
        
        self.capacity = int(capacity) 
        self.size = 0 
        self.arr = [None] * capacity 
    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n 

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity: 
            self.resize()
        self.arr[self.size] = n 
        self.size += 1 


    def popback(self) -> int:
        el = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1 
        return el 

 
    def resize(self) -> None:
        new_capacity = max(2, self.capacity * 2)
        new_arr = [None] * new_capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

        

    def getSize(self) -> int:
        return int(self.size)  
    
    def getCapacity(self) -> int:
        return int(self.capacity)
