 

#Task 4
class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin

class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the',f.getName(),'.')
            print(f)
        else:
            print('Eat the',f.getName(),'.')
            print(f)
class Mango(Fruit):
  def __init__(self,formalin=True, name='Mango'):
      super().__init__(formalin, name)

  def getComment(self):
      if self.hasFormalin():
        return ( 'Mangos are bad for you')
      else:
        return ('Mangos are good for you')

  def __str__(self):
      return f'{self.getComment()}'

class Jackfruit(Fruit):
  def __init__(self,formalin=False, name='Jackfruit'):
     super().__init__(formalin, name)
  def getComment(self):
    if self.hasFormalin():
      return( 'Jackfruits are bad for you')
    else:
      return('Jackfruits are good for you')

  def __str__(self):
      return f'{self.getComment()}'


m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)