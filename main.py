from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.running = False
        self.root.destroy()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    
    def __init__(self, win: Window):
        self.right_wall = True
        self.left_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.x1 = 100
        self.x2 = 300
        self.y1 = 300
        self.y2 = 500
        self.win = win
        
        # x1y1-------x2y1
        #
        #
        # x1y2--------x2y2
        
        
        
    def draw(self):
        if self.left_wall:
            p1 = Point(self.x1, self.y1)
            p2 = Point(self.x1, self.y2)
            l = Line(p1,p2)
            self.win.draw_line(l, "red")
            



def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw()
    
    win.wait_for_close()
    
    


main()
