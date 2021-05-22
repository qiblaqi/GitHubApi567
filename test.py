
from GitHubApi567 import *

import unittest

class TestGitHubApi567(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testHelloWorld(self): 
      self.assertEqual(read_from_git_api("qiblaqi"),[1,2,3,"qiblaqi"])
   

if __name__ == '__main__':
    print('Running unit tests for GitHubApi567!')
    unittest.main()
