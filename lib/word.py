#!/usr/bin/env python2.7

from tile import tile

class word():
	def __init__(self, blocks):
		self.blocks = blocks
		self.total = self.calcPoints()
		print self.total

	def calcPoints(self):
		total = 0
		for i in self.blocks:
			total += i.getPoints()
		return total