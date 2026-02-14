import os
import csv
VOWEL_BITS = 5
CONSONANT_BITs = 7
MISSING_VALUE = '__UNKNOWN'
def proper_path(file_name : str) -> str:
    return os.path.join('./data_files', file_name)

def file_exists(file_name : str) -> bool:
    return os.path.exists(proper_path(file_name))

def discard_files(*args : str) -> None:
    for file_name in args:
        try:
            os.remove(proper_path(file_name))
        except OSError:
            pass
    
def create_base_file(file_name : str, num_bits : int) -> None:
    if num_bits < 1:
        raise ValueError('Invalid number of bits given, must be positive.')
    rows = [('id', 'sound', 'notes')]
    for i in range(2**num_bits):
        if i ==0:
            rows.append((i, ""))
        else:
            rows.append((i, MISSING_VALUE, MISSING_VALUE))
    with open(proper_path(file_name), 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

        
def verify_files():
    if not (file_exists('vowels.csv') and file_exists('consonants.csv') and file_exists('runes.csv')):
        discard_files('vowels.csv', 'consonants.csv', 'runes.csv', 'words.csv')
        for file_name, bits in (('vowels.csv', VOWEL_BITS), ('consonants.csv', CONSONANT_BITs)):
            create_base_file(file_name, bits)
    if not file_exists('runes.csv'):
        with open(proper_path('consonants.csv'), 'r') as consonant_file:
            with open(proper_path('vowels.csv'), 'r') as vowel_file:
                consonant_reader = csv.reader(consonant_file)
                vowel_reader = csv.reader(vowel_file)
                consonant_rows = list(consonant_reader)[1:]
                vowel_rows = list(vowel_reader)[1:]
                rune_rows = [('id', 'sound', 'notes')]
                for c_row in consonant_rows:
                    for v_row in vowel_rows:
                        if c_row[1] != "" and v_row[1] != "":
                            for vowel_first in (0, 1):
                                pass #TODO
                        elif c_row[1] == "" and v_row[1] != "":

    
def main():
    verify_files()

if __name__ == "__main__":
    main()