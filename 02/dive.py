class Submarine():
    def __init__(self,horizontal,depth):
        self.horizontal = horizontal
        self.depth = depth
    def forward(self,x):
        self.horizontal += x
    def down(self,y):
        self.depth += y
    def up(self,z):
        self.depth -= z
    def get_current_position(self):
        print(f"Horizontal Position: {self.horizontal} Depth: {self.depth}")
        print(f"Product = {self.horizontal * self.depth}")

c = Submarine(0,0)

c.forward(5)
c.down(5)
c.forward(8)
c.up(3)
c.down(8)
c.forward(2)
c.get_current_position()