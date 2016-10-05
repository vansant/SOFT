# Tests

import unittest

def test_module_import(module_name):
    """ Import module or return false"""
    try:
        __import__(module_name)
        return True
    except:
        return False

class TestIfDependenciesImport(unittest.TestCase):

    def test_for_dependencies(self):
        self.assertTrue(test_module_import('os') is True, "{} not installed correctly".format('os'))
        self.assertTrue(test_module_import('zipfile') is True, "{} not installed correctly".format('zipfile'))
        self.assertTrue(test_module_import('django') is True, "{} not installed correctly".format('django'))


if __name__ == '__main__':
    unittest.main()