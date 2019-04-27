from django.test import TestCase
# TDD cycle involves starting with a test 
# that fails, then writing code to get it to pass.
# Create your tests here.

class SmokeTest(TestCase):

	def test_bad_maths(self):
		self.assertEqual(1+1, 3)