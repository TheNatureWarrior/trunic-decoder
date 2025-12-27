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
    rows = [['id', 'sound']]
    for i in range(2**num_bits + 1):
        rows.append([i, MISSING_VALUE])
    with open(proper_path(file_name), 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

        


def verify_files():
    if not (file_exists('vowels.csv') and file_exists('consonants.csv') and file_exists('runes.csv')):
        discard_files('vowels.csv', 'consonants.csv', 'runes.csv', 'sounds.csv', 'words.csv')
        create_base_file('beep', 5)


    
def main():
    verify_files()

if __name__ == "__main__":
    main()