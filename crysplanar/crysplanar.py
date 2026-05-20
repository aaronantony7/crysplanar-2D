                                    # CRYSPLANAR 2D #

'''

~  CRYSPLANAR 2D is a python module used for designing generative art using ArtPencil.

~   ArtPencil is a tool used for designing.

~   It is based on turtle, pygame,PIL and tKinter modules in python.

~   You can also save your projects in png format using save() method.

~   It can be used to create cool design more simpler and easier.

~   Use crysplanar.version() to view the version of crysplanar 2D.

~   Crysplanar save() requires the installation of ghostscript to save file as (*.png).

~   If ghostscript is not found , the file will be saved as *.eps(encapsulated postscript).
    
~   Crysplanar bgmusic() requires the installation of pygame module (version:2.6.1).

~   If module is not found , bgmusic() cannot be used.

#   Please read the following descriptions to learn how to use the module.


'''

'''

    CRYSPLANAR 2D requires PIL ( PYTHON IMAGING LIBRARY ) for saving the projects.
    So kindly install PIL using
       - CMD bash:  pip install Pillow


'''

                            #CRYSPLANAR TOOLS AND THEIR FUNCTIONS

# ArtPencil     -   to modify the ArtPencil tool(size,color). It is invisible in Board.
# placer        -   to change the position of ArtPencil.
# crystalmaker  -   a special method(function) to create crystal like stuctures.
# Board         -   Art Screen (crysBoard)
# Bgmusic       -   Background music
# save          -   used for saving the projects.
# Drawshape     -   default shape generator
# reset         -   used to clear crysBoard
# colorgen      -   auto generates color palettes (35 available).
# version       -   displays the current version of crysplanar 2D.
# picback       -   sets a background image on the crysBoard.
# removeart     -   to remove the ArtPencil(cursor).
# undo          -   to undo only the last operation.

# STATS

'''
     Module       : crysplanar 2D v1.5.3
     Lines        : <350
     Tools        : 14
     Shapes       : 10
     Palettes     : 35
     last updated : 5/20/2026
     
'''

# ANGLE CONFIGURE

'''
          90 

          |    
180  ____ | ____  0
          |
          |

         270

'''

# GRAPH CONFIGURE (board)

# board is a 800 x 600 screen.

'''
board:

  x=-400        x=0       x=400
    ____________|___________ 
   |                        |- y = 300
   |                        |
   |                        |
   |          (0,0)         |- y = 0
   |                        |
   |                        |
   |________________________|_ y= -300


points:

              (0,+300)
                 |
                 |
  (-400,0)-----(0,0)-----(+400,0)
                 |
                 |   
              (0,-300)

'''
# crystalmaker syntax:

''' crystalmaker(sidesno,crystalno,crayon,sidelen,spacing,x=[],y=[])

        sidesno     - no of sides of the required crystal
        crystalno   - length of the crystal(in 10px)
        crayon      - list containing desirable colors of the crystal
        sidelen     - length of the side(in px)
        spacing     - spacing between overlapping smaller crystals
        x / y       - positional list of x and y coordinates

'''

# Bgmusic syntax:

''' bgmusic(path, repeat=False)
        path    - path to the music file (.mp3 or .wav)
        repeat  - if True, loops the music forever
'''

# COLOR PATTERNS - AUTO GENERATED / AVAILABLE 

'''
# COLOR PATTERN

#Heat & Fire:
fire     = ['red', 'gold', 'orange']
lava     = ['red', 'darkred', 'orange', 'yellow']
ember    = ['black', 'darkred', 'red', 'orange']
sunset   = ['red', 'orange', 'gold', 'pink', 'purple']

#Cold & Ice:
ice      = ['navy', 'royalblue', 'cyan']
frost    = ['white', 'lightblue', 'cyan', 'blue']
arctic   = ['white', 'silver', 'lightcyan', 'navy']
blizzard = ['white', 'lightgray', 'gray', 'blue']

#Space & Cosmic:
galaxy   = ['purple', 'violet', 'magenta', 'black']
nebula   = ['purple', 'blue', 'cyan', 'pink', 'white']
cosmos   = ['black', 'navy', 'purple', 'magenta']
pulsar   = ['white', 'cyan', 'blue', 'navy', 'black']
stardust = ['gold', 'white', 'yellow', 'orange', 'pink']

# Nature:
forest   = ['darkgreen', 'green', 'lime', 'yellow']
ocean    = ['navy', 'blue', 'teal', 'cyan', 'white']
earth    = ['brown', 'sienna', 'tan', 'khaki']
jungle   = ['darkgreen', 'green', 'lime', 'yellow', 'orange']
desert   = ['tan', 'gold', 'orange', 'brown', 'red']

#Gems & Minerals:
amethyst = ['purple', 'violet', 'lavender', 'white']
emerald  = ['darkgreen', 'green', 'lime', 'white']
sapphire = ['navy', 'blue', 'royalblue', 'white']
ruby     = ['darkred', 'red', 'crimson', 'white']
diamond  = ['white', 'lightcyan', 'lightblue', 'silver']
obsidian = ['black', 'darkgray', 'gray', 'purple']

#Neon & Toxic:
toxic    = ['lime', 'yellow', 'green', 'black']
neon     = ['lime', 'cyan', 'magenta', 'yellow']
radioactive = ['lime', 'yellow', 'black', 'darkgreen']
plasma   = ['cyan', 'white', 'blue', 'purple']

# Soft & Pastel:
candy    = ['pink', 'hotpink', 'violet', 'white']
sakura   = ['pink', 'lightpink', 'white', 'lavender']
pastel   = ['lightpink', 'lightyellow', 'lightblue', 'lavender']
cotton   = ['white', 'pink', 'lightblue', 'lightyellow']

# Monochrome:
mono     = ['white', 'lightgray', 'gray', 'darkgray', 'black']
shadow   = ['black', 'darkgray', 'gray']
silver   = ['white', 'silver', 'gray', 'darkgray']

#Good vs Evil:
good     = ['white', 'gold', 'yellow', 'cyan']
evil     = ['black', 'darkred', 'red', 'purple']
war      = ['red', 'black', 'darkred', 'gray']

'''

# HOW TO ACCESS AUTO GENERATED COLOR PATTERNS ?

'''
    In other modules: crysplanar.colorgen('galaxy')

    example:
        import crysplanar as cp

        art = cp.crysplanar()
        art.Board('My Art', 'black')
        art.ArtPencil(hidepencil=True)

        art.crystalmaker(
            sidesno=6,
            crystalno=24,
            crayon=art.colorgen('nebula'),  
            sidelen=100,
            spacing=10,
            x=list(range(25)),
            y=list(range(25)))

        
'''

# DRAWSHAPE MODULE - A MODULE OF GENERATING SHAPES

'''
    drawshape is an inner class of crysplanar that provides
    a collection of ready-to-use geometric shapes for generative art.
    
    All shapes support custom fill colors and are optimized
    for use with the crysplanar Board and ArtPencil tools.


    PARAMETERS:
        sidelen     -   length of the side in pixels
        fillcolor   -   fill color of the shape
        rotate      -   rotates triangle upside down (True/False)
        angle       -   arc angle for round() / slant for parallelogram()
        width       -   width for rectangle and parallelogram
        height      -   height for rectangle and parallelogram
        sidesno     -   number of sides for polygon()
        size        -   size of heart shape
        radius      -   radius of circle

    NOTE:
        All shapes use ArtPencil for outline color.
        Use cp.ArtPencil(color='red') to change outline color.
        Use cp.placer(x, y) to position shapes on the Board.

'''

# HOW TO ACCESS DRAWSHAPE MODULE ?

'''
    import crysplanar as cp

    # ArtPencil engine instance is required
    art = cp.crysplanar()

    # Pass the art engine into the shape constructor
    ds = cp.drawshape(art)

    # Position your brush and draw your shape
    art.placer(100, 150)
    ds.triangle(sidelen=100, fillcolor='red')
        
'''

# SHAPES - AUTO GENERATED / AVAILABLE

#   1.  line            -   draws a line
#   2.  triangle        -   draws a triangle
#   3.  square          -   draws a square
#   4.  rectangle       -   draws a rectangle
#   5.  pentagon        -   draws a pentagon
#   6.  round           -   draws a circle or arc
#   7.  polygon         -   draws any polygon (no of sides)
#   8.  diamond         -   draws a diamond shape
#   9.  parallelogram   -   draws a parallelogram
#  10.  heart           -   draws a heart shape
    
#====================================================================================#

import turtle as t
import pygame as pg
import tkinter.filedialog as tfd
import os

class crysplanar:

    def __init__(self):
        self.p = t.Turtle()
        self.p.shape("circle")
        pg.mixer.init()
        
    def removeart(self):
        self.p.hideturtle()
        self.p.getscreen().update()

    def undo(self):
        if self.p.undobufferentries() > 0:
            self.p.undo()
            self.p.getscreen().update()           

    def ArtPencil(self, size=1, color="black", hidepencil=False):
        self.p.pensize(size)
        self.p.pencolor(color)
        if hidepencil:
            self.p.hideturtle()

    def Board(self, title="CRYSPLANAR 2D", color="white"):
        self.p.getscreen().title(title)
        self.p.getscreen().bgcolor(color)

    def reset(self, color='white'):
        self.p.getscreen().clearscreen()     
        self.p.getscreen().bgcolor(color)
        self.p.shape("circle")                
        self.p.hideturtle()
        self.p.penup()
        self.p.goto(0, 0)
        self.p.pendown()
        self.p.getscreen().update()
        print('Board reset!')
    
    def picback(self, path):
        self.p.getscreen().bgpic(path)
        
    def placer(self, x, y):
        self.p.penup()
        self.p.goto(x, y)
        self.p.pendown()

    def bgmusic(self, path, repeat=False):
        pg.mixer.music.load(path)
        if repeat:
            pg.mixer.music.play(-1)
        else:
            pg.mixer.music.play(0)

    def save(self, file_name='crysplanar_ART'):
        path = tfd.asksaveasfilename(
                defaultextension='.png',
                filetypes=[('PNG files', '*.png'), ('EPS files', '*.eps')],
                initialfile=file_name)

        if path:
            eps_path = os.path.splitext(path)[0] + '.eps'

            self.p.hideturtle()
            self.p.getscreen().update()

            canvas = self.p.getscreen().getcanvas()
            canvas.postscript(file=eps_path)

            try:
                from PIL import Image
                img = Image.open(eps_path)
                img.save(path)
                img.close()
                os.remove(eps_path)  # cleanup eps
                print(f'Saved as PNG: {path}')
            except OSError:
                print(f'Ghostscript not found!')
                print(f'Saved as EPS instead: {eps_path}')

    def version(self):
        name = 'crysplanar 2D '
        version = '1.5.3 '
        print(f'name : {name} \n version : {version}')
        
    def crystalmaker(self, sidesno, crystalno, crayon, sidelen, spacing, x=None, y=None):
        x = x if x is not None else [0]
        y = y if y is not None else [0]

        self.p.getscreen().tracer(0)
        
        for m in range(crystalno):
            self.placer(x=(x[m%len(x)]*spacing), y=(y[m%len(y)]*spacing))

            self.p.begin_fill()
            self.p.pencolor(crayon[(m+1)%len(crayon)])
            
            for n in range(sidesno):
                self.p.right(360/sidesno)
                self.p.forward(sidelen)
                
            self.p.fillcolor(crayon[m%len(crayon)])
            self.p.end_fill()

        self.p.getscreen().update()

    def colorgen(self, theme):
        themes = {
            'fire'    : ['red', 'gold', 'orange'],
            'lava'    : ['red', 'darkred', 'orange', 'yellow'],
            'ember'   : ['black', 'darkred', 'red', 'orange'],
            'sunset'  : ['red', 'orange', 'gold', 'pink', 'purple'],
            'ice'     : ['navy', 'royalblue', 'cyan'],
            'frost'   : ['white', 'lightblue', 'cyan', 'blue'],
            'arctic'  : ['white', 'silver', 'lightcyan', 'navy'],
            'blizzard': ['white', 'lightgray', 'gray', 'blue'],
            'galaxy'  : ['purple', 'violet', 'magenta', 'black'],
            'nebula'  : ['purple', 'blue', 'cyan', 'pink', 'white'],
            'cosmos'  : ['black', 'navy', 'purple', 'magenta'],
            'pulsar'  : ['white', 'cyan', 'blue', 'navy', 'black'],
            'stardust': ['gold', 'white', 'yellow', 'orange', 'pink'],
            'forest'  : ['darkgreen', 'green', 'lime', 'yellow'],
            'ocean'   : ['navy', 'blue', 'teal', 'cyan', 'white'],
            'earth'   : ['brown', 'sienna', 'tan', 'khaki'],
            'jungle'  : ['darkgreen', 'green', 'lime', 'yellow', 'orange'],
            'desert'  : ['tan', 'gold', 'orange', 'brown', 'red'],
            'amethyst': ['purple', 'violet', 'lavender', 'white'],
            'emerald' : ['darkgreen', 'green', 'lime', 'white'],
            'sapphire': ['navy', 'blue', 'royalblue', 'white'],
            'ruby'    : ['darkred', 'red', 'crimson', 'white'],
            'diamond' : ['white', 'lightcyan', 'lightblue', 'silver'],
            'obsidian': ['black', 'darkgray', 'gray', 'purple'],
            'toxic'   : ['lime', 'yellow', 'green', 'black'],
            'neon'    : ['lime', 'cyan', 'magenta', 'yellow'],
            'radioactive': ['lime', 'yellow', 'black', 'darkgreen'],
            'plasma'  : ['cyan', 'white', 'blue', 'purple'],
            'candy'   : ['pink', 'hotpink', 'violet', 'white'],
            'sakura'  : ['pink', 'lightpink', 'white', 'lavender'],
            'pastel'  : ['lightpink', 'lightyellow', 'lightblue', 'lavender'],
            'cotton'  : ['white', 'pink', 'lightblue', 'lightyellow'],
            'mono'    : ['white', 'lightgray', 'gray', 'darkgray', 'black'],
            'shadow'  : ['black', 'darkgray', 'gray'],
            'silver'  : ['white', 'silver', 'gray', 'darkgray'],
            'good'    : ['white', 'gold', 'yellow', 'cyan'],
            'evil'    : ['black', 'darkred', 'red', 'purple'],
            'war'     : ['red', 'black', 'darkred', 'gray'],
        }
        return themes.get(theme, ['white', 'black'])

# --- END OF CRYSPLANAR CLASS --- #

class drawshape:

    def __init__(self, engine):
        self.p = engine.p

    def _filler(self, fillcolor, func, *args, **kwargs):
        self.p.fillcolor(fillcolor)
        self.p.begin_fill()
        func(*args, **kwargs)
        self.p.end_fill()
        
    def line(self, length, angle):
        self.p.getscreen().tracer(0)
        old_heading = self.p.heading() 
        self.p.left(angle)
        self.p.forward(length)
        self.p.setheading(old_heading) 
        self.p.getscreen().update()
        
    def triangle(self, sidelen, rotate=False, fillcolor=None):
        self.p.getscreen().tracer(0)                  

        def _raw_draw():
            for n in range(3):
                if rotate:
                    self.p.forward(sidelen)
                    self.p.right(120)
                else:
                    self.p.forward(sidelen)
                    self.p.left(120)
                    
        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()
            
        self.p.getscreen().update()
               
    def square(self, sidelen, fillcolor=None):
        self.p.getscreen().tracer(0)   

        def _raw_draw():
            for n in range(4):
                self.p.forward(sidelen)
                self.p.right(90)

        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()
            
        self.p.getscreen().update()

    def rectangle(self, width, height, fillcolor=None):
        l = [width, height]
        self.p.getscreen().tracer(0)

        def _raw_draw():
            for n in range(4):
                self.p.forward(l[n%2])
                self.p.right(90)

        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()
            
        self.p.getscreen().update()
        
    def pentagon(self, sidelen, fillcolor=None):
        self.p.getscreen().tracer(0)

        def _raw_draw():
            for n in range(5):
                self.p.forward(sidelen)
                self.p.left(72)

        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()

        self.p.getscreen().update()

    def round(self, radius, fillcolor=None, angle=360):
        self.p.getscreen().tracer(0)

        def _raw_draw():
            self.p.circle(radius, angle)

        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()
            
        self.p.getscreen().update()

    def polygon(self, sidesno, sidelen, fillcolor=None):
        self.p.getscreen().tracer(0)
        
        def _raw_draw():
            for n in range(sidesno):
                self.p.forward(sidelen)
                self.p.left(360/sidesno)

        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()
            
        self.p.getscreen().update()

    def parallelogram(self, width, height, angle=60, fillcolor=None):
        self.p.getscreen().tracer(0)
        
        def _raw_draw():
            for n in range(2):
                self.p.forward(width)      
                self.p.left(angle)         
                self.p.forward(height)     
                self.p.left(180 - angle)   

        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()
            
        self.p.getscreen().update()

    def heart(self, size=100, fillcolor='red'):
        self.p.getscreen().tracer(0)
        
        def _raw_draw():
            self.p.setheading(45)            
            self.p.forward(size)
            self.p.circle(size / 2, 180) 
            self.p.right(90)
            self.p.circle(size / 2, 180) 
            self.p.forward(size)
        
        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()
            
        self.p.getscreen().update()
                
    def diamond(self, sidelen, fillcolor=None):
        self.p.getscreen().tracer(0)

        def _raw_draw():   
            for n in range(2):
                self.p.forward(sidelen)
                self.p.left(60)
                self.p.forward(sidelen)
                self.p.left(120)

        if fillcolor is not None:
            self._filler(fillcolor, _raw_draw)
        else:
            _raw_draw()
            
        self.p.getscreen().update()
        
# --- END OF DRAWSHAPE CLASS --- #    

