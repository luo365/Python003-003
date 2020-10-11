from abc import ABC, abstractmethod

class Zoo:
    def __init__(self, name):
        self.name = name
        self._animals = []
        
    def add_animal(self, animal):
        if not self.is_in_zoo(animal):
            self._animals.append(animal)
            
    def is_in_zoo(self, animal):
        if len(self._animals) == 0:
            return False
        else:
            for item in self._animals:
                if id(item) == id(animal):
                    return True
            return False
        
    def has_attr(self, animal_type):
        for item in self._animals:
            if type(item) is animal_type:
                return True
        else:
            return False
        
    @property
    def animals(self):
        return self._animals


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, group, size, character):
        pass
    
    @property
    def is_dangerous(self):
        if (self.size == '中等' or self.size == '大') and self.group == '食肉':
            return '是凶猛动物'
        else:
            return '不是凶猛动物'


class Cat(Animal):
    def __init__(self, name, group, size, character):
        self.name = name
        self.group = group
        self.size = size
        self.character = character
        self._bark_type = '喵喵'
        
    @property
    def is_pet(self):
        if self.is_dangerous == '是凶猛动物':
            return '不适合作为宠物'
        else:
            return '适合作为宠物'
        
    @property
    def bark_type(self):
        return self._bark_type
    
    @bark_type.setter
    def bark_type(self, value):
        self._bark_type = value



class Dog(Animal):
    def __init__(self, name, group, size, character):
        self.name = name
        self.group = group
        self.size = size
        self.character = character
        self._bark_type = '汪汪'
        
    @property
    def is_pet(self):
        if self.is_dangerous == '是凶猛动物':
            return '不适合作为宠物'
        else:
            return '适合作为宠物'
        
    @property
    def bark_type(self):
        return self._bark_type
    
    @bark_type.setter
    def bark_type(self, value):
        self._bark_type = value


if __name__ == '__main__':
    # 实例化动物园
    zoo = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    zoo.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = zoo.has_attr(Cat)

    print(have_cat)