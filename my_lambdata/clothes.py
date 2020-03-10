


class Polo():
    def __init__(self,style,size,color):
        self.style = style
        self.size = size
        self.color = color
        

if __name__ == "__main__":
    
    polo = Polo(style='Sheek', size='L', color='Blue')
    print(type(polo))
    print(polo.size)
    print(polo.style)
    print(polo.color)
