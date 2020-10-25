import math

def onesComplement(n):

    # Find number of bits in
    # the given integer
    number_of_bits = (int)(math.floor(math.log(n) /
                                math.log(2))) + 1;

    # XOR the given integer with poe(2,
    # number_of_bits-1 and print the result
    return ((1 << number_of_bits) - 1) ^ n;

# Driver code
n = 22
print(onesComplement(78)) 
