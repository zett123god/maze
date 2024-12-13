# Maze Notes

- Setting up the Window
    - The very skinny is defining a variable using the **Tk()** class, and then running the **mainloop()** method on that variable.
    - For the rest of the *README*, ther window will be refered to as **root**
    - To change the size of the window on startup, we run the **geometry** method with a string of dimensions: ("800x800")

- Closing the Window
    - The window will actually close just by hitting the X, but we want the window to constantly update itself with new instructions, which will prevent it from closing.
    - We need 3 methods to accomplish this.
    - We need the update method, which calls the root's "update()" and "update_idletasks()" methods
    - We need to define a variable within the Window's constructor that signifies whether the window is running.
    - Then we need to make a running method with sets the running variable to **True** and calls upon the update method until the variable is set to False
    - and Finally we need to make a close method that sets the variable to **False**, and closes the window via **root.destroy()**
    - We go back to the constructor and set a new data variable using the method **protocol("WM_DELETE_WINDOW", self.close)**, calling the close method we made.

- Canvas
    - A Canvas is the element that we will be drawing the lines in
    - we initiate via
    `self.canvas = Canvas(self.root, bg="white", height = 800, width = 800)
     self.canvas.pack(fill=BOTH, expand=1)`

- Drawing a line
    - We need 2 classes, Point and Line
    - Point will be a class that holds the x and y coordinates of a point
    - Line will be a class that takes 2 constructors as inputs. It will have a draw method that takes a Canvas() class and a color as inputs. It will draw the line on the Canvas in the color.
    - draw() will use the canvas' **create_line** method that takes the x of point1, y of point1, x of point2, y of point2, the color, and a width as arguments to draw the line.
    `class Point:`
    `def __init__(self, x,y)`
    ` self.x, self.y = x,y`

    `class Line`
    `def __init__(self,p1,p2)`
    ` self.p1, self.p2 = p1, p2`
    `def draw(self, canvas, color):`
    `canvas.create_line(`
    `self.p1.x. self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)`