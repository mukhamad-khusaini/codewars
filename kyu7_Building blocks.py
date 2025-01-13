class Block:
    width = 0
    length = 0
    height = 0
    def __init__(self, attr):
        self.width = attr[0]
        self.length = attr[1]
        self.height = attr[2]

    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.width*self.length*self.height
    
    def get_surface_area(self):
        return self.width*self.height*2+self.length*self.height*2+self.width*self.length*2
