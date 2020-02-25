import math

class Vec:

	 def __init__(self,x,y):
	 	self.x = x
	 	self.y = y
	 	self.__length = math.sqrt(self.x ** 2 + self.y ** 2)

	 def plus(vector):
	 	newX = self.x += vector.x
	 	newY = self.y += vector.y
	 	return Vec(newX,newY)

	 def minus(vector):
	 	new_x = self.x -= vector.x
	 	new_y = self.y -= vector.y
	 	return Vec(new_x,new_y)
	 @property
	 def length(self):
        return self.__length
     
     @staticmethod
     def distance(lst1,lst2):
     	num1 = lst1[0] - lst2[0]
     	num2 = lst1[1] - lst2[1]
     	return math.sqrt(num1 ** 2 + num2 ** 2)
    

        
        
