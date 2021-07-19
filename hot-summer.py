import gizeh as gz
import moviepy.editor as mpy
import numpy as np
import sys

width,height = 1024,1024 # in pixels
colors = [(255/255, 169/255, 0), (255/255, 118/255, 0), (205/255, 17/255, 59/255), (82/255, 0, 106/255)]
audio = mpy.AudioFileClip(sys.argv[1])
n_circles = 50

def make_frame(t):
  surface = gz.Surface(width,height)

  for i in range(n_circles):
    angle = 2*np.pi*(1.0*i/n_circles+t/10)
    center = width*( 0.5+ gz.polar2cart(0.1,angle))
    circle = gz.circle(r=width*(1.0-1.0*i/n_circles), xy=center, fill=colors[i % len(colors)])
    circle.draw(surface)

  contour1 = gz.circle(r=.65*width,xy=[width/2,width/2], stroke_width=.5*width, stroke=(0,0,0))
  contour2 = gz.circle(r=.42*width,xy=[width/2,width/2], stroke_width=.02*width, stroke=colors[0])
  contour1.draw(surface)
  contour2.draw(surface)
  return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=audio.duration)
clip = clip.set_audio(audio)
clip.write_videofile("hot-summer.mp4", fps=24)