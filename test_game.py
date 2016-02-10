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
		self.game = game.Game()
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

	def test_dealer_is_hit(self):
		"""Test that when dealer hits he is given a card"""
		self.dealer.dealer_hand.append('Kc')
		self.assertTrue(self.dealer.dealer_hit(self.dealer) == self.dealer.dealer_hand)

	def test_player_stay(self):
		"""Test when the player stays no more cards are added"""
		self.player.hand = ['Jd', '5s', '2d']
		self.assertEqual(self.player.player_stay(self.player), self.player.hand)

	def test_dealer_stay(self):
		"""Test when the dealer stays no more cards are added"""
		self.dealer.hand = ['Ad', 'As']
		self.assertEqual(self.dealer.dealer_stay(self.dealer), self.dealer.dealer_hand)

	def test_when_player_has_round(self):
		"""Test that the player has the correct hand at the end of the round"""
		self.player.hand = ['Kd', 'Js']
		self.player.player_stay(self.player)
		self.assertEqual(self.player.player_hit_or_stay(self.player), self.player.hand)

	def test_when_dealer_has_round(self):
		"""Test that the dealer has the correct hand at the end of the round"""
		self.dealer.dealer_hand = ['2h', '3s']
		new_hand = self.dealer.dealer_hit(self.dealer)
		self.assertEqual(self.dealer.dealer_hit_or_stay(self.dealer), new_hand)

	def test_when_player_bust(self):
		"""Test when player busts, nothing is returned"""
		self.assertEqual(self.game.player_bust(), None)

	def test_when_dealer_bust(self):
		"""Test when the dealer busts, nothing is returned"""
		self.assertEqual(self.game.dealer_bust(), None)

	def test_player_wins_the_round(self):
		"""Test that you win is returned when the player wins the round"""
		self.assertIn(self.game.player_win(21, 19),  "You win the round!")

	def test_player_loses_the_round(self):
		"""Test that you lose is returned when the player loses the round"""
		self.assertIn(self.game.player_lose(18, 20), "You lost the round!")

	def test_tie_game(self):
		"""Test that a tie is returned when player and dealer tie"""
		self.assertIn(self.game.tie_game(19, 19), "The round is a tie!")

	def test_summary(self):
		"""Test that the summary only displays the scores and returns nothing"""
		self.assertEqual(self.game.summary(), None)

	def test_round(self):
		"""Test that the round only runs the game and returns None"""
		self.assertEqual(self.game.round(self.player, self.dealer), None)

	def test_check_victory(self):
		"""Test that check victory displays who is the winner and returns None"""
		self.assertEqual(self.game.check_victory(21, 20), None)
