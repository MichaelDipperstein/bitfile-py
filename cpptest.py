import sys
import bitfile

NUM_CALLS = 5

if __name__ == "__main__":

    bf = bitfile.BitFile()

    # Open bit file for reading.
    bf.open('testfile', 'r')

    # Read chars
    for i in xrange(NUM_CALLS):
        try:
            value = bf.get_char()
        except:
            print 'Error: reading char'
            bf.close()
            exit()
        else:
            print 'read char',  value

    # Read single bits
    for i in xrange(NUM_CALLS):
        try:
            value = bf.get_bit()
        except:
            print 'Error: reading char'
            bf.close()
            exit()
        else:
            print 'read bit',  value

    # Read some bits into an integer (MSByte to LSByte).
    value = 0
    for i in xrange(NUM_CALLS):
        try:
            value = bf.get_bits_mtol(32)
        except:
            print 'Error: reading bits from MSByte to LSByte'
            bf.close()
            exit()
        else:
            print 'read bits MSByte to LSByte',  hex(value)

    # Read some bits into an integer (LSByte to MSByte).
    value = 0
    for i in xrange(NUM_CALLS):
        try:
            value = bf.get_bits_ltom(12)
        except:
            print 'Error: reading bits from LSByte to MSByte'
            bf.close()
            exit()
        else:
            print 'read 12 bits LSByte to MSByte',  hex(value)

    bf.close()
