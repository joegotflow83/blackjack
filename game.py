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
		self.rounds = 0

	def player_draw_hand(self, user):
		"""Have the dealer deal a hand to the player"""
		print("The dealer deals you your hand...")
		return self.hand

	def dealer_draw_hand(self, ai):
		"""Have the dealer deal himself a hand"""
		print("The {} deals a hand for himself (Does he cheat??????)...".format(self.dealer_name))
		print("The {} shows a {} as his first card.".format(self.dealer_name, self.dealer_hand[0]))
		return self.dealer_hand

	def player_hit(self, user):
		"""If the player chooses to hit, give him a card"""
		user.hand.append(user.new_card())
		print("The dealer deals you another card... Here is what you got...\n")
		return user.hand

	def dealer_hit(self, ai):
		"""If the dealer chooses to hit have him deal himself a card"""
		ai.dealer_hand.append(ai.dealer_new_card())
		print("The {} decides to hit and adds another card to his hand...".format(ai.dealer_name))
		return ai.dealer_hand

	def player_stay(self, user):
		"""If the player decides to stay, do not deal him anymore cards"""
		print("You stay and the dealer does not deal you anymore cards...")
		return user.hand

	def dealer_stay(self, ai):
		"""If the dealer decides to stay he will not deal himself anymore cards"""
		print("The {} decides not to hit anymore and stays...".format(self.dealer_name))
		return ai.dealer_hand

	def player_hit_or_stay(self, user):
		"""If player hits, run the player hit func and if player stays, run the stay func"""
		while True:
			print(self.hand)
			decision = input("Do you want to hit or stay? ").lower()
			if decision == 'hit':
				user.player_hit(user)
				if user.check_bust(user.hand):
					print(user.hand)
					print("Oh no! You went bust!")
					break
			elif decision == 'stay':
				return user.player_stay(user)
				break
		return self.hand

	def dealer_hit_or_stay(self, ai):
		"""If ai hits, run the dealer hit func and if ai stays, run the stay func"""
		while ai.calculate_hand(ai.dealer_hand) < 17:
			ai.dealer_hit(ai)
			if ai.check_bust(ai.dealer_hand):
				print("The dealer went bust!")
				break
		else:
			ai.dealer_stay(ai)
		return self.dealer_hand

	def invalid_input(self, user):
		"""Tell the player they have typed something invalid"""
		print("I am sorry, but you have typed something invalid. Try again")
		return self.player_hit_or_stay(user)

	def player_win(self, player_total, ai_total):
		"""Let the player know he wins the game and add a point for the player"""
		self.score[0] += 1
		self.rounds += 1
		print("You had {} and the dealer had {}\n".format(player_total, ai_total))
		return "You win the round!"

	def player_bust(self):
		"""Display the player went bust so dealer wins the round"""
		self.score[1] += 1
		self.rounds += 1
		print("Since you bust the dealer wins the round!")
		print(self.summary())
		return

	def dealer_bust(self):
		"""Display the dealer went bust so the player wins the round"""
		self.score[0] += 1
		self.rounds += 1
		print("Since the dealer bust you win the round!")
		print(self.summary()  )
		return

	def player_lose(self, player_total, ai_total):
		"""Let the player know he loses the game and add a point for the ai"""
		self.score[1] += 1
		self.rounds += 1
		print("You had {} and the dealer had {}\n".format(player_total, ai_total))
		return "You lost the round!"

	def tie_game(self, player_total, ai_total):
		"""Return that the round ended in a tie"""
		print("You had {} and the dealer had {}\n".format(player_total, ai_total))
		return "The round is a tie!"

	def summary(self):
		"""Print out the scores of the player and the computer"""
		print('\n\n' + ('_' * 20))
		print("Player: {}".format(self.score[0]))
		print("Dealer: {}".format(self.score[1]))
		return

	def setup(self):
		"""Set up the players for the game"""
		user = Player()
		ai = Dealer()
		return (user, ai)

	def round(self, user, ai):
		"""Simulate a round of blackjack against the player and the computer as the dealer"""
		player_hand = user.player_draw_hand(user)
		ai_hand = ai.dealer_draw_hand(ai)
		player_hand = user.player_hit_or_stay(user)
		if user.check_bust(user.hand):
			return self.player_bust()
		ai_hand = ai.dealer_hit_or_stay(ai)
		if ai.check_bust(ai.dealer_hand):
			return self.dealer_bust()
		player_total = user.calculate_hand(user.hand)
		ai_total = ai.calculate_hand(ai.dealer_hand)
		self.check_victory(player_total, ai_total)
		return

	def check_victory(self, player_total, ai_total):
		"""Check who won the round"""
		if player_total > ai_total:
			print(self.player_win(player_total, ai_total))
			print(self.summary())
			return
		elif ai_total > player_total:
			print(self.player_lose(player_total, ai_total))
			print(self.summary())
			return
		else:
			print(self.tie_game(player_total, ai_total))
			return

	def clear(self):
		"""Clear the screen for easier readability"""
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')


class Player(Game, Deck):


	def __init__(self):
		"""Initialize variables"""
		self.suits = "chsd"
		self.ranks = '23456789TJQKA'
		self.deck = tuple([''.join(card)
			for card in itertools.product(self.ranks, self.suits)])
		self.hand = random.sample(self.deck, 2)

	def new_card(self):
		"""Give the player a card when player hits"""
		return ''.join(random.sample(self.deck, 1))

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
		return ''.join(random.sample(self.deck, 1))

	def __getitem__(self):

		return self.dealer_hand


if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Welcome to blackjack! Best of 3 wins!")
	game = Game()
	while game.rounds < 3:
		players = game.setup()
		game.round(players[0], players[1])
	else:
		print("Thanks for playing!")
