#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from random import randint
import sys

class Player(object):
	def __init__(self, name, hit_range):
		self.hit_range = hit_range
		self.alive = True
		self.name = name
		self.health = 100
		self.print_name()
		self.hit_points = 0

	def print_name(self):
		print self.name

	def attack(self, player):
		self.death()
		self.hit_points = randint(0, self.hit_range)
		self.check_health()
		if isinstance(player, Player):
			if self.alive:
				player.health -= self.hit_points
			else:
				sys.exit()
		else:
			print "Can not attack animals"

	def check_health(self):
		print "Player " + self.name + " has :" + str(self.health)

	def death(self):
		if self.health <= 0:
			self.alive = False


class Hero(Player):
	def __init__(self, name, hit_range):
		super(Hero, self).__init__(name, hit_range)
		self.health = 200

	def defence(self, player):
		if isinstance(player, Player):
			self.health += player.hit_points/2




player1 = Player("Alexandros", 20)
hero1 = Hero("Nikos", 40)
print player1.name + " has " + str(player1.hit_points)
print hero1.health
player1.attack(hero1)
print player1.name + " has " + str(player1.hit_points)
hero1.defence(player1)
print hero1.health
# player1 = Player("Sotiris")
# player2 = Player("Alexandros")

# while True:
# 	player1.attack(player2)
# 	player2.attack(player1)
# 	time.sleep(3)