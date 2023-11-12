from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import json_helper

class JSONHelperTestClass(TestCase):

    """
    Next 4 tests are for open_json_file.
    """

    # Full path existing json file
    def test_open_json_file(self):
        test_file = '/Users/mike/projects/zcw_python/PythonFundamentals.Exercises.Part9/data/super_smash_bros/sonic.json'
        test_data = {'name': 'Sonic', 'neutral_special': 'Spin Dash', 'side_special': 'Super Slide', 'up_special': 'Cannonball', 'down_special': 'Turbo Charge', 'final_smash': 'Sonic Super Slam'}
        actual_data = json_helper.open_json_file(test_file)
        self.assertEqual(test_data, actual_data)

    # Same directory as program / where i'm running it json file
    def test_open_json_file2(self):
        test_file = 'data/super_smash_bros/mario.json'
        test_data = {'name': 'Mario', 'neutral_special': 'Fireball', 'side_special': 'Cape', 'up_special': 'Super Jump Punch', 'down_special': 'F.L.U.D.D.', 'final_smash': 'Mario Finale'}
        actual_data = json_helper.open_json_file(test_file)
        self.assertEqual(test_data, actual_data)

    # Misfed path that include a precdeing slash, should not be found
    def test_open_json_file3(self):
        test_file = '/data/super_smash_bros/mario.json'
        with self.assertRaises(FileNotFoundError):
            json_helper.open_json_file(test_file)

    # Good path, but not a json file, should through ValueError (covers json decoder errors)
    # Note: okay so if the data is still in json format this won't through an error, python is smart and will get it
    def test_open_json_file4(self):
        test_file = 'data/super_smash_bros/bob.txt'
        with self.assertRaises(ValueError):
            json_helper.open_json_file(test_file)
    
    """
    Next test is for open_all_json_files.  Directory includes non-json .txt file
    """

    # Full path to dir with json files.  test_data excludes the contents of the .txt file in directory
    def test_open_all_json_files(self):
        test_dir = '/Users/mike/projects/zcw_python/PythonFundamentals.Exercises.Part9/data/super_smash_bros/'
        test_data = [{'name': 'Wario', 'neutral_special': 'Slimeball', 'side_special': 'Cloak', 'up_special': 'Super Jump Slap', 'down_special': 'Belly Flop', 'final_smash': 'Mustache You to Leave'}, {'name': 'Sonic', 'neutral_special': 'Spin Dash', 'side_special': 'Super Slide', 'up_special': 'Cannonball', 'down_special': 'Turbo Charge', 'final_smash': 'Sonic Super Slam'}, {'name': 'Mario', 'neutral_special': 'Fireball', 'side_special': 'Cape', 'up_special': 'Super Jump Punch', 'down_special': 'F.L.U.D.D.', 'final_smash': 'Mario Finale'}, {'name': 'Link', 'neutral_special': 'Bow and Arrows', 'side_special': ' Boomerang', 'up_special': ' Spin Attack', 'down_special': 'Remote Bomb', 'final_smash': 'Ancient Bow and Arrow'}]
        actual_data = json_helper.open_all_json_files(test_dir)
        self.assertEqual(test_data, actual_data)

        # Path that does not exist, should not be found
    def test_open_all_json_files2(self):
        test_dir = '/PythonFundamentals.Exercises.Part9/files/super_smash_bros/'
        with self.assertRaises(NotADirectoryError):
            json_helper.open_all_json_files(test_dir)
