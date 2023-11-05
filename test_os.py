import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        import os
        os.mkdir('test_dir')
        assert 'test_dir' in os.listdir() and os.path.isdir('test_dir')

    def test_2(self):
        import shutil
        shutil.copyfile('test_file', 'test_file1')
        with open('test_file', 'r') as f:
            fr = f.read()
        with open('test_file1', 'r') as f1:
            fr1 = f1.read()
        assert fr == fr1

    def test_3(self):
        import os, shutil
        shutil.copytree('test_dir', 'test_dir1')
        assert os.listdir('test_dir') == os.listdir('test_dir1')

    def test_4(self):
        import os, posix
        name = os.uname()
        assert isinstance(name, posix.uname_result)

    def test_5(self):
        import os
        os.remove('test_file1')
        assert 'test_file1' not in os.listdir()

    def test_6(self):
        import os
        os.rmdir('test_dir1')
        assert 'test_dir1' not in os.listdir()

    def test_7(self):
        import os
        os.chdir('test_dir')
        assert os.getcwd().split('/')[-1] == 'test_dir'

if __name__ == '__main__':
    unittest.main()
