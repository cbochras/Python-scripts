# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:29:04 2021

@author: umit
"""

pi = 3.14159

def area(radius):
    return pi*(radius**2)

def circumference(radius):
    return 2*pi*radius

def sphere_surface(radius):
    return 4.0*area(radius)

def sphere_volume(radius):
    return (4.0/3.0)*pi*(radius**3)