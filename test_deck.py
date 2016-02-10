import unittest

from deck import Deck


class DeckTest(unittest.TestCase):


	def setUp(self):
		"""Set up testing environment for deck"""
		self.deck = Deck()

	def tearDown(self):
		"""Tear down testing environment for deck"""
		self.deck = None

	def test_check_bust_true(self):
		"""Test that if someone busts, it returns True"""
		hand = ['Ts', '9c', 'Qs']
		self.assertEqual(self.deck.check_bust(hand), True)

	def test_check_bust_false(self):
		"""Test that if someone does not bust, it returns False"""
		hand = ['2d', '3s', '5d', '6h']
		self.assertEqual(self.deck.check_bust(hand), False)

	def test_check_bust_21(self):
		"""Test that if someone has exactly 21 they do not bust and return False"""
		hand = ['Js', 'Ac']
		self.assertEqual(self.deck.check_bust(hand), False)

	def test_grab_numbers(self):
		"""Test that the numbers or face cards are selected from their suits for adding"""
		hand = ['Js', '2d']
		self.assertEqual(self.deck.grab_numbers(hand), [10, 2])

	def test_calculate_hand(self):
		"""Test that the numbers from the cards add up"""
		hand = ['Ad', '5h', '2h']
		self.assertEqual(self.deck.calculate_hand(hand), 18)
