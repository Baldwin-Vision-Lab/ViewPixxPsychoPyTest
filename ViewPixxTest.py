from matplotlib.pyplot import draw
from numpy.lib.function_base import flip
import psychopy
from psychopy import core, visual, event, data
from psychopy.preferences import prefs


# Setup the Window
win = visual.Window([800,600], fullscr=False, monitor="testMonitor")

grating = psychopy.visual.GratingStim(win, units='cm', size=[5,5], tex='sin', pos=(0,5))


rectangle1 = psychopy.visual.rect.Rect(win, units ='cm', fillColor=[105,105,105], fillColorSpace=None, pos=(-7.5, -2), size=[5,5], ori=0.0, opacity=None, contrast=1.0, colorSpace='rgb255')
rectangle2 = psychopy.visual.rect.Rect(win, units ='cm', fillColor=[106,106,106], fillColorSpace=None, pos=(-2.5, -2), size=[5,5], ori=0.0, opacity=None, contrast=1.0, colorSpace='rgb255')
rectangle3 = psychopy.visual.rect.Rect(win, units ='cm', fillColor='black', fillColorSpace=None, pos=(2.5, -2), size=[5,5], ori=0.0, opacity=None, contrast=1.0, colorSpace='rgb')
rectangle4 = psychopy.visual.rect.Rect(win, units ='cm', fillColor='blue', fillColorSpace=None, pos=(7.5, -2), size=[5,5], ori=0.0, opacity=None, contrast=1.0, colorSpace='rgb')

rectangles = [rectangle1, rectangle2, rectangle3, rectangle4]

for rectangle in rectangles:
    rectangle.draw()

grating.draw()
win.flip()

psychopy.event.waitKeys(keyList =['q'])