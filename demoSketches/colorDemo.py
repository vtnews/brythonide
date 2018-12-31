﻿#
# Complementary colors interactive demo 
#
# Based on program P.1.0.1 of "Generative Design" by
# H. Bohnacker, B. Gross, J. Laub, C. Lazzeroni
#


from p5py import *

def setup():
    createCanvas(600,600)
    noStroke()
    rectMode(CENTER)
    
def draw():
    colorMode(HSB,100)
    h = map(mouseY,0,600,0,100)
    background(h,100,100)
    fill(100-h,100,100)
    rect(300,300,mouseX+1,mouseX+1)

run()