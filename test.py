
from GitHubApi567 import *

import unittest

class TestGitHubApi567(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testIfUserIDisValid(self):
      self.assertEqual(read_from_git_api("qiblaqi"),['Repo: 2020Fall-810-B Number of commits: 21',
                                                     'Repo: 567-Fall-2020-master Number of commits: 6',
                                                     'Repo: 567-HW04a Number of commits: 2',
                                                     'Repo: 567-Spring-2020-qzhao Number of commits: 12',
                                                     'Repo: 567HW02a Number of commits: 6',
                                                     'Repo: action-build Number of commits: 30',
                                                     'Repo: Fall2020-567-533-590 Number of commits: 22',
                                                     'Repo: Fall2020_567_HW02 Number of commits: 8',
                                                     'Repo: GitHubApi567 Number of commits: 15',
                                                     'Repo: InterNatter Number of commits: 27',
                                                     'Repo: n_r Number of commits: 1',
                                                     'Repo: Stevens-Python-Course-ByQ.Zhao Number of commits: 44',
                                                     'Repo: Student-Repository Number of commits: 5'])
    def testIfInvalidUserID(self):
        with self.assertRaises(Exception) as context:
            read_from_git_api("qiblaqi213891038193")    #test invalid user id

        self.assertTrue('invalid user id' in str(context.exception))
   

if __name__ == '__main__':
    print('Running unit tests for GitHubApi567!')
    unittest.main()
