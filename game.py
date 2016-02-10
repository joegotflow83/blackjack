"""This is the game blackjack where the player tries to beat the dealer and win the round!

Author: Joseph Moran
Created: 02/08/2016

!/usr/local/env python3.5
"""
import itertools
import random
import sys
import os

from deck import Deck


class Game:


	def __init__(self):
		"""Initialize variables"""
		self.score = [0, 0]

	def player_draw_hand(self):
		"""Have the dealer deal a hand to the player"""
		print("The dealer deals you your hand...")
		return self.hand

	def dealer_draw_hand(self):
		"""Have the dealer deal himself a hand"""
		print("The {} deals a hand for himself (Does he cheat??????)...")
		return self.dealer_draw_hand

	def player_hit(self, user):
		"""If the player chooses to hit, give him a card"""
		user.hand.append(user.new_card())
		print("The dealer deals you another card... Here is what you got...\n")
		if user.check_bust(self.hand):
			print("Oh no! You went bust!")
			return True
		else:
			return False

	def dealer_hit(self, ai):
		"""If the dealer chooses to hit have him deal himself a card"""
		self.dealer_hand.append(ai.dealer_new_card)
		print("The {} decides to hit and adds another card to his hand...".format(self.dealer_name))
		if ai.check_bust(self.dealer_hand):
			return True
		else:
			return False

	def player_stay(self):
		"""If the player decides to stay, do not deal him anymore cards"""
		print("You stay and the dealer does not deal you anymore cards...")
		return self.hand

	def dealer_stay(self):
		"""If the dealer decides to stay he will not deal himself anymore cards"""
		print("The {} decides not to hit anymore and stays...".format(self.dealer_name))
		return self.dealer_hand

	def player_hit_or_stay(self, user):
		"""If player hits, run the player hit func and if player stays, run the stay func"""
		while True:
			print(self.hand)
			decision = input("Do you want to hit or stay? ").lower()
			#if 'hit' or 'stay' not in decision:
				#return self.invalid_input()
			if decision == 'hit':
				bust_or_not = user.player_hit(user)
				if bust_or_not:
					break
			elif decision == 'stay':
				return user.player_stay()
				break
		return self.hand

	def dealer_hit_or_stay(self, ai):
		"""If ai hits, run the dealer hit func and if ai stays, run the stay func"""
		for ai_turns in range(2):
			ai_hit_or_stay = random.randint(0, 2)
			if ai_hit_or_stay == 1:
				ai.dealer_hit(ai)
				bust_or_not = ai.dealer_hit(ai)
				if bust_or_not:
					break
			else:
				ai.dealer_stay()
				break
		return self.dealer_hand

	def invalid_input(self):
		"""Tell the player they have typed something invalid"""
		print("I am sorry, but you have typed something invalid. Try again")
		return self.round(user, ai)

	def player_win(self, player_total, ai_total):
		"""Let the player know he wins the game and add a point for the player"""
		self.score[0] += 1
		print("You had {} and the dealer had {}\n".format(player_total, ai_total))
		return "You win the round!"

	def player_lose(self, player_total, ai_total):
		"""Let the player know he loses the game and add a point for the ai"""
		self.score[1] += 1
		print("You had {} and the dealer had {}\n".format(player_total, ai_total))
		return "You lost the round!\n"

	def tie_game(self, player_total, ai_total):
		"""Return that the round ended in a tie"""
		print("You had {} and the dealer had {}\n".format(player_total, ai_total))
		return "The round is a tie!"

	def summary(self):
		"""Print out the scores of the player and the computer"""
		print("Player: {}".format(self.score[0]))
		print("Dealer: {}".format(self.score[1]))
		return

	def round(self, user, ai):
		"""Simulate a round of blackjack against the player and the computer as the dealer"""
		player_hand = user.player_draw_hand()
		player_hand = user.player_hit_or_stay(user)
		ai_hand = ai.dealer_draw_hand()
		ai_hand = ai.dealer_hit_or_stay(ai)
		player_total = user.calculate_hand(user.hand)
		ai_total = ai.calculate_hand(ai.dealer_hand)
		if player_total > ai_total:
			print(self.player_win(player_total, ai_total))
			print(self.summary())
			return
		elif ai_total > player_total:
			print(self.player_lose(player_total, ai_total))
			print(self.summary())
			return
		else:
			print(tie_game(player_total, ai_total))
			return


class Player(Game, Deck):


	def __init__(self, player):
		"""Initialize variables"""
		self.player = player
		self.suits = "chsd"
		self.ranks = '23456789TJQKA'
		self.deck = tuple([''.join(card)
			for card in itertools.product(self.ranks, self.suits)])
		self.hand = random.sample(self.deck, 2)

	def new_card(self):
		"""Give the player a card when player hits"""
		return random.sample(self.deck, 1)

	def __getitem__(self):

		return self.hand


class Dealer(Game, Deck):


	def __init__(self):
		"""Initialize variables"""
		self.choices_for_name = ['Ace Dealer', 'Dragon Dealer', 
								 'Master Dealer', 'Invicincible Dealer']
		self.dealer_name = random.choice(self.choices_for_name)
		self.suits = "chsd"
		self.ranks = '23456789TJQKA'
		self.deck = tuple([''.join(card)
			for card in itertools.product(self.ranks, self.suits)])
		self.dealer_hand = random.sample(self.deck, 2)
		

	def dealer_new_card(self):
		"""Give the dealer a card when dealer hits"""
		return random.sample(self.deck, 1)

	def __getitem__(self):

		return self.dealer_hand


if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	user = Player(player=input("What is your name player? "))
	ai = Dealer()
	game = Game()
	game.round(user, ai)