import math

class Vec:

	 def __init__(self,x,y):
	 	self.x = x
	 	self.y = y

	 def plus(vector):
	 	newX = self.x += vector.x
	 	newY = self.y += vector.y
	 	return Vec(newX,newY)

	 def minus(vector):
	 	newX = self.x -= vector.x
	 	newY = self.y -= vector.y
	 	return Vec(newX,newY)

	 def length:
        return math.sqrt(math.pow(self.x,2) + math.pow(self.y,2))
     
     @staticmethod
     def distance(lst1,lst2):
     	num1 = lst1[0] - lst2[0]
     	num2 = lst1[1] - lst2[1]
     	return math.sqrt(num1 ** 2 + num2 ** 2)
    

        
        
