from tkinter import Tk, BOTH, Canvas
import time


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
    
    def __init__(self, win: Window, x1, x2, y1, y2):
        self.right_wall = True
        self.left_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
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
            self.win.draw_line(l, "black")
            time.sleep(0.0005)
            self.win.redraw()
            
        if self.right_wall:
            p1 = Point(self.x2, self.y1)
            p2 = Point(self.x2, self.y2)
            l = Line(p1,p2)
            self.win.draw_line(l, "black")
            time.sleep(0.0005)
            self.win.redraw()
        if self.top_wall:
            p1 = Point(self.x1, self.y1)
            p2 = Point(self.x2, self.y1)
            l = Line(p1, p2)
            self.win.draw_line(l, "black")
            time.sleep(0.0005)
            self.win.redraw()
            
        if self.bottom_wall:
            p1 = Point(self.x1, self.y2)
            p2 = Point(self.x2, self.y2)
            l = Line(p1, p2)
            self.win.draw_line(l, "black")
            time.sleep(0.0005)
            self.win.redraw()
        
    def draw_move(self, to_cell, undo=False): #middle of cell to middle of another cell
        if undo == True:
            color = "red"
        else:
            color = "gray"
        midX1 = (self.x1 + self.x2) / 2
        midY1 = (self.y1 + self.x2) / 2
        midPoint1 = Point(midX1, midY1)
        
        midX2 = (to_cell.x1 + to_cell.x2) / 2
        midY2 = (to_cell.y1 + to_cell.y2) / 2
        midPoint2 = Point(midX2, midY2)
        line = Line(midPoint1, midPoint2)
        self.win.draw_line(line, color)
        
        
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.startx = x1
        self.starty = y1
        self.rows = num_rows
        self.cols = num_cols
        self.sizeX = cell_size_x
        self.sizeY = cell_size_y
        self.win = win
        self.cells = []
        
        self.create_cells()
    
            
    # init cell = Cell(win: Window, self.x1, self.y1, (self.x1 + self.sizeX), (self.y1 + self.sizeY))
    # next cell in row = Cell(win:Window, (self.x1 + self.sizeX), self.y1, (self.x1 + self.sizeX*2), (self.y1 + self.sizeY)
    
    def create_cells(self):
        nextX = self.startx + self.sizeX
        nextY = self.starty + self.sizeY
        cell = Cell(self.win, self.startx, nextX, self.starty, nextY)
        current_level = self.starty
                
        for row in range(self.rows):
            self.cells.append(cell)
            for cols in range(self.cols):
                cell = Cell(self.win, nextX, (nextX + (self.sizeX * cols)), current_level, (current_level + self.sizeY))
                self.cells.append(cell)
            current_level += self.sizeY
            cell = Cell(self.win, self.startx, nextX, current_level, (current_level + self.sizeY))
    
    def draw_cells(self):
        for cells in self.cells:
            self.win.redraw()
            cells.draw()
            
                
    
    
        
        


def main():
    win = Window(800, 600)

    
    maze = Maze(10,10,10,10,50,50,win)
    
    
    
    maze.draw_cells()
    
    win.wait_for_close()
    
    
    
    


main()
