"""
A simple module that can be used to test python code.
"""

class testing:
	""" A class that contains a testing method."""
	
	def __init__(self):
		self.tests_run = 0
		self.failures = 0
		
			
		
	def smoke(self, func_result, func_expected):
		""" 
		A method that can check functions for the correct output.
		"""
		self.tests_run += 1
		
		if func_result == func_expected:
			pass
		else: 
			self.failures += 1
	
	def reporting(self):
		if self.failures > 0:
			print('Tests Failed: ' + self.failures)
			print('Tests Successful: ' + (self.tests_run - self.failures))
		else:
			print('All tests were successful.')
			
		
		
