# Copyright (c) 2008 Art & Logic, Inc. All Rights Reserved.

# generate code to instantiate two python dict objects
# 
# interleave is a dict object that can be used to lookup a 32bit integer with 
# an interleaved format from an 8bit char in one of four byte positions (0-3)
#
# uninterleave is a dict object that can be used to lookup an 8bit char using 
# a 32bit integer corresponding to the interleaved 32bit integer for one 8bit 
# char in one of 4 possible byte positions (0-3)

def GetNthBitFromChar(n, c):
   """
   Returns nth bit n from char c, shifted to the least significant bit
   example: GetNthBitFromChar(6, 'F') returns 0x1
   """
   nthBit = (2 ** n) & c
   return nthBit >> n # shift the bit right to the least significant bit

generateInterleaveDict = 'interleave = [\n'
generateUninterleaveDict = 'uninterleave = [\n'
for bits in range(0, 4):
   generateInterleaveDict += ' {\n'
   generateUninterleaveDict += ' {\n'
   for c in range(0, 127): # skip last 8bit char because it is not printable
      if chr(c).isprintable() or c == 0:
         # to create the interleaved format, for each 8bit char use 2 bits to
         # create one of four bytes coorasonding to significant digits 0-3
         firstByte = ((GetNthBitFromChar(0, c) << bits) + 
          (GetNthBitFromChar(1, c) << (bits + 4)))
         secondByte = ((GetNthBitFromChar(2, c) << bits) + 
          (GetNthBitFromChar(3, c) << (bits + 4))) << 8
         thirdByte = ((GetNthBitFromChar(4, c) << bits) + 
          (GetNthBitFromChar(5, c) << (bits + 4))) << 16
         forthByte = ((GetNthBitFromChar(6, c) << bits) + 
          (GetNthBitFromChar(7, c) << (bits + 4))) << 24
         
         # create one 32bit int in interleaved format coorasponding to one
         # 8 bit char
         interleaved32bitInt = firstByte + secondByte + thirdByte + forthByte
         if c == 0: #escape null
            generateInterleaveDict += ("  " + "'" + '\\0' + "'" + ': ' + 
             str(interleaved32bitInt) + ',\n')
            generateUninterleaveDict += ("  " + str(interleaved32bitInt) + 
             ': ' + "'" + '\\0' + "'" + ',\n')
         elif c == 39: # escape single quote
            generateInterleaveDict += ("  " + '"' + chr(c) + '"' + ': ' + 
             str(interleaved32bitInt) + ',\n')
            generateUninterleaveDict += ("  " + str(interleaved32bitInt) + 
             ': ' + '"' + chr(c) + '"' + ',\n')
         elif c == 92: # escape back slash
            generateInterleaveDict += ("  " + "'\\" + chr(c) + "'" + ': ' + 
             str(interleaved32bitInt) + ',\n')
            generateUninterleaveDict += ("  " + str(interleaved32bitInt) + 
             ': ' + "'\\" + chr(c) + "'" + ',\n')
         elif c != 126:
            generateInterleaveDict += ("  " + "'" + chr(c) + "'" + ': ' + 
             str(interleaved32bitInt) + ',\n')
            generateUninterleaveDict += ("  " + str(interleaved32bitInt) + 
             ': ' + "'" + chr(c) + "'" + ',\n')
         else:
            generateInterleaveDict += ("  " + "'" + chr(c) + "'" + ': ' + 
             str(interleaved32bitInt) + '\n')
            generateUninterleaveDict += ("  " + str(interleaved32bitInt) + 
             ': ' + "'" + chr(c) + "'\n")
   if bits != 3:
      generateInterleaveDict += ' },\n'
      generateUninterleaveDict += ' },\n'
   else:
      generateInterleaveDict += ' }\n'
      generateUninterleaveDict += ' }\n'
generateInterleaveDict += ']\n'
generateUninterleaveDict += ']\n'

print(generateInterleaveDict)
print('')
print(generateUninterleaveDict)
