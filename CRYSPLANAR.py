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
       - CMD bash:  pip install PIL


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


# STATS

'''
     Module      : crysplanar 2D v1.0
     Lines       : <250
     Tools       : 9
     Shapes      : 9
     Palettes    : 35

'''

# crystalmaker syntax:

''' crystalmaker(sidesno,crystalno,crayon,sidelength,spacing,x=[],y=[])

        sidesno     - no of sides of the required crystal
        crystalno   - length of the crystal(in 10px)
        crayon      - list containing desirable colors of the crystal
        sidelength  - length of the side(in px)
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
        import CRYSPLANAR as cp

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
        ds = crysplanar.drawshape()
        ds.triangle(sidelen=100, fillcolor='red')

'''

# SHAPES - AUTO GENERATED / AVAILABLE

#   1.  triangle        -   draws a triangle
#   2.  square          -   draws a square
#   3.  rectangle       -   draws a rectangle
#   4.  pentagon        -   draws a pentagon
#   5.  round           -   draws a circle or arc
#   6.  polygon         -   draws any polygon (no of sides)
#   7.  diamond         -   draws a diamond shape
#   8.  parallelogram   -   draws a parallelogram
#   9.  heart           -   draws a heart shape
    
#====================================================================================#

import turtle as t
import pygame as pg
import tkinter.filedialog as tfd
import os

p=t.Turtle()
p.shape("circle")

pg.mixer.init()

class crysplanar:
       
    def ArtPencil(self,size=1,color="black",hidepencil=False):

        p.pensize(size)
        p.pencolor(color)
        
        if hidepencil:
            p.hideturtle()

    def Board(self,title = "CRYSPLANAR 2D",color = "white"):
 
        p.getscreen().title(title)
        p.getscreen().bgcolor(color)

    def reset(self, color='white'):
        p.getscreen().clearscreen()     
        p.getscreen().bgcolor(color)
        p.shape("circle")               
        p.hideturtle()
        p.penup()
        p.goto(0, 0)
        p.pendown()
        p.getscreen().update()
        print('Board reset!')
    
    def picback(self,path):

        p.getscreen().bgpic(path)
        
    def placer(self,x,y):

        p.penup()
        p.goto(x,y)
        p.pendown()

    def bgmusic(self,path,repeat = False):

        pg.mixer.music.load(path)

        if repeat :
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

            # save canvas as eps first
            canvas = p.getscreen().getcanvas()
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
        version = '1.0 '

        print(f'name : {name} \n version : {version}')
        
    def crystalmaker(self,sidesno,crystalno,crayon,sidelen,spacing,x=None,y=None):

        x = x if x is not None else [0]
        y = y if y is not None else [0]

        p.getscreen().tracer(0)
        
        for m in range(crystalno):
            
            self.placer(x=(x[m%len(x)]*spacing),y=(y[m%len(y)]*spacing))

            p.begin_fill()
            p.pencolor(crayon[(m+1)%len(crayon)])
            
            for n in range(sidesno):

                p.right(360/sidesno)
                p.forward(sidelen)
                
            p.fillcolor(crayon[m%len(crayon)])
            p.end_fill()

        p.getscreen().update()

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
        
    class drawshape:

             def triangle(self,sidelen,rotate = False,fillcolor = None):

                p.getscreen().tracer(0)                
                p.fillcolor(fillcolor)    
                p.begin_fill()
                for n in range(3):

                    if rotate:
                        p.forward(sidelen)
                        p.right(120)

                    else:
                        p.forward(sidelen)
                        p.left(120)

                p.end_fill()
                p.getscreen().update()
               
             def square(self,sidelen,fillcolor = None):

                p.getscreen().tracer(0)
                p.fillcolor(fillcolor)    
                p.begin_fill()   
                for n in range(4):

                    p.forward(sidelen)
                    p.right(90)

                p.end_fill()
                p.getscreen().update()

             def rectangle(self,width,height,fillcolor = None):

                l=[width,height]
                
                p.getscreen().tracer(0)
                p.fillcolor(fillcolor)    
                p.begin_fill()
                
                for n in range(4):

                    p.forward(l[n%2])
                    p.right(90)

                p.end_fill()
                p.getscreen().update()

             def pentagon(self,sidelen,fillcolor = None):

                p.getscreen().tracer(0)
                p.fillcolor(fillcolor)    
                p.begin_fill()

                for n in range(5):
                    
                    p.forward(sidelen)
                    p.left(72)

                p.end_fill()
                p.getscreen().update()

             def round(self,radius,fillcolor=None,angle=360):

                p.getscreen().tracer(0)
                p.fillcolor(fillcolor)    
                p.begin_fill()

                p.circle(radius,angle)

                p.end_fill()
                p.getscreen().update()

             def polygon(self,sidesno,sidelen,fillcolor = None):

                p.getscreen().tracer(0)
                p.fillcolor(fillcolor)    
                p.begin_fill()

                for n in range(sidesno):
                    p.forward(sidelen)
                    p.left(360/sidesno)
                
                p.end_fill()
                p.getscreen().update()

             def parallelogram(self, width, height, angle=60, fillcolor=None):
    
                p.getscreen().tracer(0)
                p.fillcolor(fillcolor)
                p.begin_fill()
                
                for n in range(2):
                    p.forward(width)      
                    p.left(angle)         
                    p.forward(height)     
                    p.left(180 - angle)   
                
                p.end_fill()
                p.getscreen().update()

             def heart(self, size=100, fillcolor='red'):

                p.getscreen().tracer(0)
                p.fillcolor(fillcolor)
                p.begin_fill()

                p.setheading(140)           
                p.forward(size * 0.6)
                p.circle(-size * 0.4, 200) 
                p.setheading(60)
                p.circle(-size * 0.4, 200) 
                p.forward(size * 0.6)

                p.end_fill()
                p.getscreen().update()
                
             def diamond(self,sidelen,fillcolor = None):

                p.getscreen().tracer(0)
                p.fillcolor(fillcolor)    
                p.begin_fill()   
                for n in range(4):

                    if (n<1):
                        p.left(45)
                        p.forward(sidelen)

                    else:
                        p.left(90)
                        p.forward(sidelen)
                        
                p.end_fill()
                p.getscreen().update()
