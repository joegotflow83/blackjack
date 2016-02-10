import itertools
import random


class Deck:


	def __init__(self):
		"""Initialize variables"""
		self.suits = "chsd"
		self.ranks = '23456789TJQKA'
		self.deck = tuple([''.join(card)
			for card in itertools.product(self.ranks, self.suits)])
		self.hand = random.sample(self.deck, 2)

	def dealer_new_card(self):
		"""Give the dealer a card when dealer hits"""
		return random.sample(self.deck, 1)

	def check_bust(self, hand):
		"""Check if player has busted or not"""
		numbers = []
		numbers = self.grab_numbers(numbers, hand)
		total = sum([num for num in numbers])
		if total >= 21:
			return True
		else:
			return False

	def grab_numbers(self, numbers, hand):
		"""Grab only the ranks from the hand"""
		for card in hand:
			for value in card[:1]:
				try:
					value = int(value)
				except ValueError:
					if value in 'TJQK':
						value = 10
					elif value in 'A':
						
						value = 11
			numbers.append(value)
		if numbers[0] == 11 and numbers[1] == 11:
			numbers[0] = 1
		return numbers

	def calculate_hand(self, hand):
		"""Calculate the score of the hand"""
		score = []
		score = self.grab_numbers(score, hand)
		total = sum([num for num in score])
		return total

	def __str__(self):
		"""Allow the hand to be prettified when printed"""
		return '{} {}'.format(self.hand[0], self.hand[1])
