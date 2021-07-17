import gizeh as gz
import moviepy.editor as mpy
import numpy as np

W,H = 1024,1024 # width, height, in pixels
colors = [(255/255, 169/255, 0), (255/255, 118/255, 0), (205/255, 17/255, 59/255), (82/255, 0, 106/255)]
duration = 20 #3*60 + 30 # duration of the clip, in seconds
n_circles = 50

def make_frame(t):
  surface = gz.Surface(W,H)

  for i in range(n_circles):
    angle = 2*np.pi*(1.0*i/n_circles+t/duration)
    center = W*( 0.5+ gz.polar2cart(0.1,angle))
    circle = gz.circle(r=W*(1.0-1.0*i/n_circles), xy=center, fill=colors[i % len(colors)])
    circle.draw(surface)
  contour1 = gz.circle(r=.65*W,xy=[W/2,W/2], stroke_width=.5*W, stroke=(0,0,0))
  contour2 = gz.circle(r=.42*W,xy=[W/2,W/2], stroke_width=.02*W, stroke=colors[0])
  contour1.draw(surface)
  contour2.draw(surface)
  return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_videofile("hot-summer.mp4", fps=24)