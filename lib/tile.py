#!/usr/bin/env python2.7

class tile():
	def __init__(self, letter, points):
		self.letter = letter.upper()
		self.points = points
		self.multiplier = 1

	def setMultiplier(self, multiplier):
		self.multiplier = multiplier

	def getLetter(self):
		return self.letter

	def getPoints(self):
		return self.points * self.multiplier

	def __str__(self):
		return ("{0} : {1}").format(self.letter, self.getPoints())