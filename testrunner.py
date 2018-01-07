import unittest
import test

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test)

runner = unittest.TextTestRunner(verbosity = 1)
result = runner.run(suite)
