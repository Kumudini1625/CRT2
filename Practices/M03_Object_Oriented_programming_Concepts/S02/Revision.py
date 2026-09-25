class Grandparent:
    family_name="Malreddy"
class Parent(Grandparent):
    pass
class Mother(Grandparent):
    pass
class ChildSingle(Parent):
    def show(self):
        print(f"Single Inheritance:Kumudini {self.family_name}")
class ChildMultiple(Parent,Mother):
    def show(self): 
        print(f"Multiple Inheritance:Kuladeep {self.family_name}")
class ChildMultilevel(Parent):
    def show(self):
        print(f"Multilevel Inheritance:Shekar {self.family_name}")
class ChildHierarchical(Parent):
    def show(self):
        print(f"Hierarchical Inheritance:Mamatha {self.family_name}")
class HybridChild(Parent,Mother):
    def show(self):
        print(f"Hybrid Inheritance:Krishna {self.family_name}")
ChildSingle().show()
ChildMultiple().show()  
ChildMultilevel().show()
ChildHierarchical().show()  
HybridChild().show()
