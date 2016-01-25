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

thickline = LineStyle(5, purple)
ellipse1 = EllipseAsset(50, 70, thickline, blue)

Sprite(ellipse1)

# add your code here /\  /\  /\
#http://www.colorpicker.com

myapp = App()
myapp.run()
