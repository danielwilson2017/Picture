"""
picture.py
Author: <Daniel Wilson>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xFF4040, 1.0)
blue = Color(0x40FFFF, 1.0)
green = Color(0x000000, 1.0)
purple = Color(0xA040FF, 1.0)
dblue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thickline = LineStyle(5, purple)
thinline = LineStyle(2.5, black)
noline = LineStyle(1, dblue)
ellipse1 = EllipseAsset(250, 300, thickline, dblue)
ellipse2 = EllipseAsset(50, 70, thinline, green)
circle1 = CircleAsset(50, thinline, red)
circle2 = CircleAsset(50, thinline, purple)
grin1 = CircleAsset (30, thinline, green)
grin2 = CircleAsset (30, noline, dblue)
smile = PolygonAsset ([(0, 75), (125, 30), (0, 50), (-125, 30)], thickline, purple)

Sprite(ellipse1, (800, 400))
Sprite(ellipse2, (800, 400))
Sprite(circle1, (700, 350))
Sprite(circle2, (900, 350))
Sprite(grin1, (950, 530))
Sprite(grin2, (940, 530))
Sprite(smile, (805, 500))


# add your code here /\  /\  /\
#http://www.colorpicker.com

myapp = App()
myapp.run()
