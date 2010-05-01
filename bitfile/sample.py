"""
This is the BitFile class sample module.  It's sole purpose to to
provide sample usages for the methods in the BitFile class.

Here's a doctest that verifies the BitFile class.  To see the full
output use the command "python sample.py -v":

>>> example(5)
Writing characters:
     A B C D E
Writing bits:
     1 0 1 0 1
Writing characters:
     F G H I J
Writing 96 bits MS byte to LS byte:
     0x11111111
     0x22222222
     0x33333333
     0x44444444
     0x55555555
Writing 12 bits LS byte to MS byte:
     0x111
     0x222
     0x333
     0x444
     0x555
Reading characters:
     A B C D E
Reading bits:
     1 0 1 0 1
Reading characters:
     F G H I J
Reading 96 bits MS byte to LS byte:
     0x11111111
     0x22222222
     0x33333333
     0x44444444
     0x55555555
Reading 12 bits MS byte to LS byte:
     0x111
     0x222
     0x333
     0x444
     0x555
Writing characters:
     A B C D E
Writing bits:
     1 0 1 0 1
Writing characters:
     F G H I J
Writing 96 bits MS byte to LS byte:
     0x11111111
     0x22222222
     0x33333333
     0x44444444
     0x55555555
Writing 12 bits LS byte to MS byte:
     0x111
     0x222
     0x333
     0x444
     0x555
Reading characters:
     A B C D E
Reading bits:
     1 0 1 0 1
Reading characters:
     F G H I J
Reading 96 bits MS byte to LS byte:
     0x11111111
     0x22222222
     0x33333333
     0x44444444
     0x55555555
Reading 12 bits MS byte to LS byte:
     0x111
     0x222
     0x333
     0x444
     0x555
"""

import sys
import bitfile

NUM_CALLS = 5

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

def write_test(bf, num_calls):
    # Write chars
    value = 'A'
    print 'Writing characters:\n    ',
    for i in xrange(num_calls):
        print value,
        bf.put_char(value)
        value = chr(ord(value) + 1)
    print

    # Write single bits
    value = 1
    print 'Writing bits:\n    ',
    for i in xrange(num_calls):
        print value,
        bf.put_bit(value)
        value = 1 - value
    print

    # Write chars
    value = chr(ord('A') + num_calls)
    print 'Writing characters:\n    ',
    for i in xrange(num_calls):
        print value,
        bf.put_char(value)
        value = chr(ord(value) + 1)
    print

    # Write some bits from an integer (MSByte to LSByte).
    value = 0x11111111
    print 'Writing', 8 * sys.getsizeof(value), 'bits MS byte to LS byte:'
    for i in xrange(num_calls):
        print '    ', hex(value)
        bf.put_bits_mtol(value, 8 * sys.getsizeof(value))
        value = value + 0x11111111

    # Write some bits from an integer (LSByte to MSByte).
    value = 0x111
    print 'Writing 12 bits LS byte to MS byte:'
    for i in xrange(num_calls):
        print '    ', hex(value)
        bf.put_bits_ltom(value, 12)
        value = value + 0x111

    # Write out any remaining bits.
    bf.flush()

def read_test(bf, num_calls):
    # Read chars
    print 'Reading characters:\n    ',
    expected = 'A'
    for i in xrange(num_calls):
        try:
            value = bf.get_char()
            if value != expected:
                print '\nError: Got:', value, 'Expected:', expected, '\n'
        except:
            print 'Error: reading char'
            bf.close()
            exit()
        else:
            print value,
        expected = chr(ord(expected) + 1)
    print

    # Read single bits
    print 'Reading bits:\n    ',
    for i in xrange(num_calls):
        try:
            value = bf.get_bit()
        except:
            print 'Error: reading char'
            bf.close()
            exit()
        else:
            print value,
    print

    # Read chars
    expected = chr(ord('A') + num_calls)
    print 'Reading characters:\n    ',
    for i in xrange(num_calls):
        try:
            value = bf.get_char()
            if value != expected:
                print '\nError: Got:', value, 'Expected:', expected, '\n'
        except:
            print 'Error: reading char'
            bf.close()
            exit()
        else:
            print value,
        expected = chr(ord(expected) + 1)
    print

    # Read some bits into an integer (MSByte to LSByte).
    expected = 0x11111111
    print 'Reading', 8 * sys.getsizeof(expected), 'bits MS byte to LS byte:'
    for i in xrange(num_calls):
        try:
            value = bf.get_bits_mtol(8 * sys.getsizeof(expected))
            if value != expected:
                print '\nError: Got:', value, 'Expected:', expected, '\n'
        except:
            print 'Error: reading bits from MSByte to LSByte'
            bf.close()
            exit()
        else:
            print '    ', hex(value)
        expected = expected + 0x11111111

    # Read some bits into an integer (LSByte to MSByte).
    expected = 0x111
    print 'Reading 12 bits MS byte to LS byte:'
    for i in xrange(num_calls):
        try:
            value = bf.get_bits_ltom(12)
            if value != expected:
                print '\nError: Got:', value, 'Expected:', expected, '\n'
        except:
            print 'Error: reading bits from LSByte to MSByte'
            bf.close()
            exit()
        else:
            print '    ', hex(value)
        expected = expected + 0x111

if __name__ == "__main__":
    import doctest
    doctest.testmod()
