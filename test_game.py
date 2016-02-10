import unittest
import game


class GameTest(unittest.TestCase):


	def setUp(self):
		"""Set up testing environment"""
		self.game = game.Game()
		self.player = game.Player()
		self.dealer = game.Dealer()
	
	def tearDown(self):
		"""Tear down testing environment"""
		self.game = None
		self.player = None
		self.dealer = None

	def test_player_has_hand(self):
		"""Test that the player has a starting hand"""
		joe = self.player
		joe.hand = ['7s', 'Td']
		self.assertEqual(joe.player_draw_hand(joe), joe.hand)

	def test_dealer_has_hand(self):
		"""Test that the dealer has a starting hand"""
		self.dealer.dealer_hand = ['2c', 'Ah']
		self.assertEqual(self.dealer.dealer_draw_hand(self.dealer), self.dealer.dealer_hand)

	def test_player_is_hit(self):
		"""Test that when player hits he is given a card"""
		self.player.hand.append('5s')
		self.assertTrue(self.player.player_hit(self.player) == self.player.hand)
