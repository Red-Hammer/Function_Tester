"""
A simple module that can be used to test python code.
"""

class testing:
	""" A class that contains a testing method."""
	
	def __init__(self, function_name, *func_args, expected_outcome):
		self.function_name = function_name
		self.func_args = func_args
		self.expected = expected_outcome
		
		
		
		
	def func_checker(self):
		""" 
		A method that can check functions for the correct output.
		
		Currently the method can only check fucntions with a single, 
		list input for accuracy. 
		"""
		
		
		er_message = 'Test failed!'
		suc_message = 'Test passed!'
		
		args = self.func_args[0]
		
		
		
		tst = self.function_name(args)
		
		
		if tst != self.expected:
			print(er_message)
		else:
			print(suc_message)
		
