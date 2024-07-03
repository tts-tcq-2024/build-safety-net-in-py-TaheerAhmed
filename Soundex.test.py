import unittest
from Soundex import (
    generate_soundex, 
    get_soundex_code, 
    validate_name, 
    initialize_soundex, 
    should_add_code, 
    handle_character, 
    process_characters, 
    pad_soundex
)

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")

    def test_double_letters(self):
        self.assertEqual(generate_soundex("Aa"), "A000")
        self.assertEqual(generate_soundex("Bb"), "B000")
    
    def test_similar_sounding_names(self):
        self.assertEqual(generate_soundex("Smith"), "S530")
        self.assertEqual(generate_soundex("Smyth"), "S530")
    
    def test_names_with_same_letters(self):
        self.assertEqual(generate_soundex("Tymczak"), "T520")
        self.assertEqual(generate_soundex("Pfister"), "P236")

    def test_mixed_case(self):
        self.assertEqual(generate_soundex("SoUnDeX"), "S532")

    def test_numbers_and_symbols(self):
        self.assertEqual(generate_soundex("S!@#m1i2th3"), "S530")

    def test_non_mapped_characters(self):
        self.assertEqual(generate_soundex("AEIOUHWY"), "A000")

    def test_valid_characters(self):
        self.assertEqual(generate_soundex("Washington"), "W252")
        self.assertEqual(generate_soundex("Lee"), "L000")

    # Additional tests for internal functions
    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code('A'), '0')
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('C'), '2')
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('Z'), '2')
        self.assertEqual(get_soundex_code('a'), '0')  # Case insensitivity

    def test_validate_name(self):
        self.assertFalse(validate_name(""))
        self.assertTrue(validate_name("John"))

    def test_initialize_soundex(self):
        self.assertEqual(initialize_soundex("John"), "J")
        self.assertEqual(initialize_soundex("smith"), "S")

    def test_should_add_code(self):
        self.assertTrue(should_add_code('1', '0'))
        self.assertFalse(should_add_code('0', '0'))
        self.assertFalse(should_add_code('1', '1'))

    def test_handle_character(self):

        prev_code, soundex = handle_character('m', '0', 'S')
        self.assertEqual(prev_code, '5')
        self.assertEqual(soundex, 'S5')

    def test_process_characters(self):
        self.assertEqual(process_characters("Washington"), "W252")
        self.assertEqual(process_characters("Lee"), "L")

    def test_pad_soundex(self):
        self.assertEqual(pad_soundex("W252"), "W252")
        self.assertEqual(pad_soundex("L"), "L000")

if __name__ == '__main__':
    unittest.main()
