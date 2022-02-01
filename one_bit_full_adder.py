
def one_bit_full_adder(A,B,Cin):
    bit_carried = (A or B) and (B or Cin) and (A or Cin)
    #result_addition = (not A or not B or Cin) and (not A or B or not Cin) and (A or B or Cin) and (not Cin or not B or A)
    result_addition = A^B^Cin
    return bit_carried, result_addition


print(one_bit_full_adder(0,0,1))
print(one_bit_full_adder(0,1,1))
print(one_bit_full_adder(1,1,1))
print(one_bit_full_adder(0,1,0))
