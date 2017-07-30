"""
This is the BitFile class sample module.  It's sole purpose to to
provide sample usages for the methods in the BitFile class.

Here's a doctest that verifies the BitFile class.  To see the full
output use the command "python sample.py -v":

>>> example(6)
Writing characters:
     ABCDEF
Writing bits:
     101010
Writing 12 bits LS byte to MS byte:
     0x111
     0x222
     0x333
     0x444
     0x555
     0x666
Writing bits:
     101010
Reading characters:
     ABCDEF
Reading bits:
     101010
Reading 12 bits MS byte to LS byte:
     0x111
     0x222
     0x333
     0x444
     0x555
     0x666
Reading bits:
     101010
Writing characters:
     ABCDEF
Writing bits:
     101010
Writing 12 bits LS byte to MS byte:
     0x111
     0x222
     0x333
     0x444
     0x555
     0x666
Writing bits:
     101010
Reading characters:
     ABCDEF
Reading bits:
     101010
Reading 12 bits MS byte to LS byte:
     0x111
     0x222
     0x333
     0x444
     0x555
     0x666
Reading bits:
     101010
"""

from __future__ import print_function
import sys
import os
import bitfile

NUM_CALLS = 6

def example(num_calls):
    bf = bitfile.BitFile()

    # Open bit file for writing.
    bf.open('testfile', 'w')
    write_test(bf, num_calls)
    bf.close()

    # Now read back writes

    # Open bit file for reading.
    bf.open('testfile', 'r')
    read_test(bf, num_calls)

    bf.close()

    # Open bit file for reading and writing.
    bf.open('testfile', 'r+')
    write_test(bf, num_calls)

    # Now read back writes

    # Go back to the beginning of the file (it was opened with r+).
    bf.seek(0)
    read_test(bf, num_calls)

    bf.close()
    os.remove('testfile')

def write_test(bf, num_calls):
    # Write chars
    value = 'A'
    print('Writing characters:\n     ', end='')
    for i in range(num_calls):
        print(value, end='')
        bf.put_char(value)
        value = chr(ord(value) + 1)
    print('')

    # Write single bits
    value = 1
    print('Writing bits:\n     ', end='')
    for i in range(num_calls):
        print(value, end='')
        bf.put_bit(value)
        value = 1 - value
    print('')

    # Write some bits from an integer (LSByte to MSByte).
    value = 0x111
    print('Writing 12 bits LS byte to MS byte:')
    for i in range(num_calls):
        print('    ', hex(value))
        bf.put_bits(value, 12)
        value = value + 0x111

    # Write single bits
    value = 1
    print('Writing bits:\n     ', end='')
    for i in range(num_calls):
        print(value, end='')
        bf.put_bit(value)
        value = 1 - value
    print('')

    # Write out any remaining bits.
    bf.flush()

def read_test(bf, num_calls):
    # Read chars
    print('Reading characters:\n     ', end='')
    expected = 'A'
    for i in range(num_calls):
        try:
            value = bf.get_char()
            if value != expected:
                print('\nError: Got:', value, 'Expected:', expected, '\n')
        except:
            print('Error: reading char')
            bf.close()
            exit()
        else:
            print(value, end='')
        expected = chr(ord(expected) + 1)
    print('')

    # Read single bits
    print('Reading bits:\n     ', end='')
    for i in range(num_calls):
        try:
            value = bf.get_bit()
        except:
            print('Error: reading bits')
            bf.close()
            exit()
        else:
            print(value, end='')
    print('')

    # Read some bits into an integer (LSByte to MSByte).
    expected = 0x111
    print('Reading 12 bits MS byte to LS byte:')
    for i in range(num_calls):
        try:
            value = bf.get_bits(12)
            if value != expected:
                print('\nError: Got:', value, 'Expected:', expected, '\n')
        except:
            print('Error: reading bits from LSByte to MSByte')
            bf.close()
            exit()
        else:
            print('    ', hex(value))
        expected = expected + 0x111

    # Read single bits
    print('Reading bits:\n     ', end='')
    for i in range(num_calls):
        try:
            value = bf.get_bit()
        except:
            print('Error: reading bits')
            bf.close()
            exit()
        else:
            print(value, end='')
    print('')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
