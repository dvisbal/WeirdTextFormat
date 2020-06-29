# lookup table to find intearleved representation of chars in one of 4 byte positions
# usage: interleave[byte position][printable 128bit char]
# eg. interleave[0]['F'] returns 16777488
interleave = [
	{
		'\0': 0,
		' ': 1048576,
		'!': 1048577,
		'"': 1048592,
		'#': 1048593,
		'$': 1048832,
		'%': 1048833,
		'&': 1048848,
		"'": 1048849,
		'(': 1052672,
		')': 1052673,
		'*': 1052688,
		'+': 1052689,
		',': 1052928,
		'-': 1052929,
		'.': 1052944,
		'/': 1052945,
		'0': 1114112,
		'1': 1114113,
		'2': 1114128,
		'3': 1114129,
		'4': 1114368,
		'5': 1114369,
		'6': 1114384,
		'7': 1114385,
		'8': 1118208,
		'9': 1118209,
		':': 1118224,
		';': 1118225,
		'<': 1118464,
		'=': 1118465,
		'>': 1118480,
		'?': 1118481,
		'@': 16777216,
		'A': 16777217,
		'B': 16777232,
		'C': 16777233,
		'D': 16777472,
		'E': 16777473,
		'F': 16777488,
		'G': 16777489,
		'H': 16781312,
		'I': 16781313,
		'J': 16781328,
		'K': 16781329,
		'L': 16781568,
		'M': 16781569,
		'N': 16781584,
		'O': 16781585,
		'P': 16842752,
		'Q': 16842753,
		'R': 16842768,
		'S': 16842769,
		'T': 16843008,
		'U': 16843009,
		'V': 16843024,
		'W': 16843025,
		'X': 16846848,
		'Y': 16846849,
		'Z': 16846864,
		'[': 16846865,
		'\\': 16847104,
		']': 16847105,
		'^': 16847120,
		'_': 16847121,
		'`': 17825792,
		'a': 17825793,
		'b': 17825808,
		'c': 17825809,
		'd': 17826048,
		'e': 17826049,
		'f': 17826064,
		'g': 17826065,
		'h': 17829888,
		'i': 17829889,
		'j': 17829904,
		'k': 17829905,
		'l': 17830144,
		'm': 17830145,
		'n': 17830160,
		'o': 17830161,
		'p': 17891328,
		'q': 17891329,
		'r': 17891344,
		's': 17891345,
		't': 17891584,
		'u': 17891585,
		'v': 17891600,
		'w': 17891601,
		'x': 17895424,
		'y': 17895425,
		'z': 17895440,
		'{': 17895441,
		'|': 17895680,
		'}': 17895681,
		'~': 17895696,
	},
	{
		'\0': 0,
		' ': 2097152,
		'!': 2097154,
		'"': 2097184,
		'#': 2097186,
		'$': 2097664,
		'%': 2097666,
		'&': 2097696,
		"'": 2097698,
		'(': 2105344,
		')': 2105346,
		'*': 2105376,
		'+': 2105378,
		',': 2105856,
		'-': 2105858,
		'.': 2105888,
		'/': 2105890,
		'0': 2228224,
		'1': 2228226,
		'2': 2228256,
		'3': 2228258,
		'4': 2228736,
		'5': 2228738,
		'6': 2228768,
		'7': 2228770,
		'8': 2236416,
		'9': 2236418,
		':': 2236448,
		';': 2236450,
		'<': 2236928,
		'=': 2236930,
		'>': 2236960,
		'?': 2236962,
		'@': 33554432,
		'A': 33554434,
		'B': 33554464,
		'C': 33554466,
		'D': 33554944,
		'E': 33554946,
		'F': 33554976,
		'G': 33554978,
		'H': 33562624,
		'I': 33562626,
		'J': 33562656,
		'K': 33562658,
		'L': 33563136,
		'M': 33563138,
		'N': 33563168,
		'O': 33563170,
		'P': 33685504,
		'Q': 33685506,
		'R': 33685536,
		'S': 33685538,
		'T': 33686016,
		'U': 33686018,
		'V': 33686048,
		'W': 33686050,
		'X': 33693696,
		'Y': 33693698,
		'Z': 33693728,
		'[': 33693730,
		'\\': 33694208,
		']': 33694210,
		'^': 33694240,
		'_': 33694242,
		'`': 35651584,
		'a': 35651586,
		'b': 35651616,
		'c': 35651618,
		'd': 35652096,
		'e': 35652098,
		'f': 35652128,
		'g': 35652130,
		'h': 35659776,
		'i': 35659778,
		'j': 35659808,
		'k': 35659810,
		'l': 35660288,
		'm': 35660290,
		'n': 35660320,
		'o': 35660322,
		'p': 35782656,
		'q': 35782658,
		'r': 35782688,
		's': 35782690,
		't': 35783168,
		'u': 35783170,
		'v': 35783200,
		'w': 35783202,
		'x': 35790848,
		'y': 35790850,
		'z': 35790880,
		'{': 35790882,
		'|': 35791360,
		'}': 35791362,
		'~': 35791392,
	},
	{
		'\0': 0,
		' ': 4194304,
		'!': 4194308,
		'"': 4194368,
		'#': 4194372,
		'$': 4195328,
		'%': 4195332,
		'&': 4195392,
		"'": 4195396,
		'(': 4210688,
		')': 4210692,
		'*': 4210752,
		'+': 4210756,
		',': 4211712,
		'-': 4211716,
		'.': 4211776,
		'/': 4211780,
		'0': 4456448,
		'1': 4456452,
		'2': 4456512,
		'3': 4456516,
		'4': 4457472,
		'5': 4457476,
		'6': 4457536,
		'7': 4457540,
		'8': 4472832,
		'9': 4472836,
		':': 4472896,
		';': 4472900,
		'<': 4473856,
		'=': 4473860,
		'>': 4473920,
		'?': 4473924,
		'@': 67108864,
		'A': 67108868,
		'B': 67108928,
		'C': 67108932,
		'D': 67109888,
		'E': 67109892,
		'F': 67109952,
		'G': 67109956,
		'H': 67125248,
		'I': 67125252,
		'J': 67125312,
		'K': 67125316,
		'L': 67126272,
		'M': 67126276,
		'N': 67126336,
		'O': 67126340,
		'P': 67371008,
		'Q': 67371012,
		'R': 67371072,
		'S': 67371076,
		'T': 67372032,
		'U': 67372036,
		'V': 67372096,
		'W': 67372100,
		'X': 67387392,
		'Y': 67387396,
		'Z': 67387456,
		'[': 67387460,
		'\\': 67388416,
		']': 67388420,
		'^': 67388480,
		'_': 67388484,
		'`': 71303168,
		'a': 71303172,
		'b': 71303232,
		'c': 71303236,
		'd': 71304192,
		'e': 71304196,
		'f': 71304256,
		'g': 71304260,
		'h': 71319552,
		'i': 71319556,
		'j': 71319616,
		'k': 71319620,
		'l': 71320576,
		'm': 71320580,
		'n': 71320640,
		'o': 71320644,
		'p': 71565312,
		'q': 71565316,
		'r': 71565376,
		's': 71565380,
		't': 71566336,
		'u': 71566340,
		'v': 71566400,
		'w': 71566404,
		'x': 71581696,
		'y': 71581700,
		'z': 71581760,
		'{': 71581764,
		'|': 71582720,
		'}': 71582724,
		'~': 71582784,
	},
	{
		'\0': 0,
		' ': 8388608,
		'!': 8388616,
		'"': 8388736,
		'#': 8388744,
		'$': 8390656,
		'%': 8390664,
		'&': 8390784,
		"'": 8390792,
		'(': 8421376,
		')': 8421384,
		'*': 8421504,
		'+': 8421512,
		',': 8423424,
		'-': 8423432,
		'.': 8423552,
		'/': 8423560,
		'0': 8912896,
		'1': 8912904,
		'2': 8913024,
		'3': 8913032,
		'4': 8914944,
		'5': 8914952,
		'6': 8915072,
		'7': 8915080,
		'8': 8945664,
		'9': 8945672,
		':': 8945792,
		';': 8945800,
		'<': 8947712,
		'=': 8947720,
		'>': 8947840,
		'?': 8947848,
		'@': 134217728,
		'A': 134217736,
		'B': 134217856,
		'C': 134217864,
		'D': 134219776,
		'E': 134219784,
		'F': 134219904,
		'G': 134219912,
		'H': 134250496,
		'I': 134250504,
		'J': 134250624,
		'K': 134250632,
		'L': 134252544,
		'M': 134252552,
		'N': 134252672,
		'O': 134252680,
		'P': 134742016,
		'Q': 134742024,
		'R': 134742144,
		'S': 134742152,
		'T': 134744064,
		'U': 134744072,
		'V': 134744192,
		'W': 134744200,
		'X': 134774784,
		'Y': 134774792,
		'Z': 134774912,
		'[': 134774920,
		'\\': 134776832,
		']': 134776840,
		'^': 134776960,
		'_': 134776968,
		'`': 142606336,
		'a': 142606344,
		'b': 142606464,
		'c': 142606472,
		'd': 142608384,
		'e': 142608392,
		'f': 142608512,
		'g': 142608520,
		'h': 142639104,
		'i': 142639112,
		'j': 142639232,
		'k': 142639240,
		'l': 142641152,
		'm': 142641160,
		'n': 142641280,
		'o': 142641288,
		'p': 143130624,
		'q': 143130632,
		'r': 143130752,
		's': 143130760,
		't': 143132672,
		'u': 143132680,
		'v': 143132800,
		'w': 143132808,
		'x': 143163392,
		'y': 143163400,
		'z': 143163520,
		'{': 143163528,
		'|': 143165440,
		'}': 143165448,
		'~': 143165568,
	}
]

uninterleave = [
	{
		0: '\0',
		1048576: ' ',
		1048577: '!',
		1048592: '"',
		1048593: '#',
		1048832: '$',
		1048833: '%',
		1048848: '&',
		1048849: "'",
		1052672: '(',
		1052673: ')',
		1052688: '*',
		1052689: '+',
		1052928: ',',
		1052929: '-',
		1052944: '.',
		1052945: '/',
		1114112: '0',
		1114113: '1',
		1114128: '2',
		1114129: '3',
		1114368: '4',
		1114369: '5',
		1114384: '6',
		1114385: '7',
		1118208: '8',
		1118209: '9',
		1118224: ':',
		1118225: ';',
		1118464: '<',
		1118465: '=',
		1118480: '>',
		1118481: '?',
		16777216: '@',
		16777217: 'A',
		16777232: 'B',
		16777233: 'C',
		16777472: 'D',
		16777473: 'E',
		16777488: 'F',
		16777489: 'G',
		16781312: 'H',
		16781313: 'I',
		16781328: 'J',
		16781329: 'K',
		16781568: 'L',
		16781569: 'M',
		16781584: 'N',
		16781585: 'O',
		16842752: 'P',
		16842753: 'Q',
		16842768: 'R',
		16842769: 'S',
		16843008: 'T',
		16843009: 'U',
		16843024: 'V',
		16843025: 'W',
		16846848: 'X',
		16846849: 'Y',
		16846864: 'Z',
		16846865: '[',
		16847104: '\\',
		16847105: ']',
		16847120: '^',
		16847121: '_',
		17825792: '`',
		17825793: 'a',
		17825808: 'b',
		17825809: 'c',
		17826048: 'd',
		17826049: 'e',
		17826064: 'f',
		17826065: 'g',
		17829888: 'h',
		17829889: 'i',
		17829904: 'j',
		17829905: 'k',
		17830144: 'l',
		17830145: 'm',
		17830160: 'n',
		17830161: 'o',
		17891328: 'p',
		17891329: 'q',
		17891344: 'r',
		17891345: 's',
		17891584: 't',
		17891585: 'u',
		17891600: 'v',
		17891601: 'w',
		17895424: 'x',
		17895425: 'y',
		17895440: 'z',
		17895441: '{',
		17895680: '|',
		17895681: '}',
		17895696: '~',
	},
	{
		0: '\0',
		2097152: ' ',
		2097154: '!',
		2097184: '"',
		2097186: '#',
		2097664: '$',
		2097666: '%',
		2097696: '&',
		2097698: "'",
		2105344: '(',
		2105346: ')',
		2105376: '*',
		2105378: '+',
		2105856: ',',
		2105858: '-',
		2105888: '.',
		2105890: '/',
		2228224: '0',
		2228226: '1',
		2228256: '2',
		2228258: '3',
		2228736: '4',
		2228738: '5',
		2228768: '6',
		2228770: '7',
		2236416: '8',
		2236418: '9',
		2236448: ':',
		2236450: ';',
		2236928: '<',
		2236930: '=',
		2236960: '>',
		2236962: '?',
		33554432: '@',
		33554434: 'A',
		33554464: 'B',
		33554466: 'C',
		33554944: 'D',
		33554946: 'E',
		33554976: 'F',
		33554978: 'G',
		33562624: 'H',
		33562626: 'I',
		33562656: 'J',
		33562658: 'K',
		33563136: 'L',
		33563138: 'M',
		33563168: 'N',
		33563170: 'O',
		33685504: 'P',
		33685506: 'Q',
		33685536: 'R',
		33685538: 'S',
		33686016: 'T',
		33686018: 'U',
		33686048: 'V',
		33686050: 'W',
		33693696: 'X',
		33693698: 'Y',
		33693728: 'Z',
		33693730: '[',
		33694208: '\\',
		33694210: ']',
		33694240: '^',
		33694242: '_',
		35651584: '`',
		35651586: 'a',
		35651616: 'b',
		35651618: 'c',
		35652096: 'd',
		35652098: 'e',
		35652128: 'f',
		35652130: 'g',
		35659776: 'h',
		35659778: 'i',
		35659808: 'j',
		35659810: 'k',
		35660288: 'l',
		35660290: 'm',
		35660320: 'n',
		35660322: 'o',
		35782656: 'p',
		35782658: 'q',
		35782688: 'r',
		35782690: 's',
		35783168: 't',
		35783170: 'u',
		35783200: 'v',
		35783202: 'w',
		35790848: 'x',
		35790850: 'y',
		35790880: 'z',
		35790882: '{',
		35791360: '|',
		35791362: '}',
		35791392: '~',
	},
	{
		0: '\0',
		4194304: ' ',
		4194308: '!',
		4194368: '"',
		4194372: '#',
		4195328: '$',
		4195332: '%',
		4195392: '&',
		4195396: "'",
		4210688: '(',
		4210692: ')',
		4210752: '*',
		4210756: '+',
		4211712: ',',
		4211716: '-',
		4211776: '.',
		4211780: '/',
		4456448: '0',
		4456452: '1',
		4456512: '2',
		4456516: '3',
		4457472: '4',
		4457476: '5',
		4457536: '6',
		4457540: '7',
		4472832: '8',
		4472836: '9',
		4472896: ':',
		4472900: ';',
		4473856: '<',
		4473860: '=',
		4473920: '>',
		4473924: '?',
		67108864: '@',
		67108868: 'A',
		67108928: 'B',
		67108932: 'C',
		67109888: 'D',
		67109892: 'E',
		67109952: 'F',
		67109956: 'G',
		67125248: 'H',
		67125252: 'I',
		67125312: 'J',
		67125316: 'K',
		67126272: 'L',
		67126276: 'M',
		67126336: 'N',
		67126340: 'O',
		67371008: 'P',
		67371012: 'Q',
		67371072: 'R',
		67371076: 'S',
		67372032: 'T',
		67372036: 'U',
		67372096: 'V',
		67372100: 'W',
		67387392: 'X',
		67387396: 'Y',
		67387456: 'Z',
		67387460: '[',
		67388416: '\\',
		67388420: ']',
		67388480: '^',
		67388484: '_',
		71303168: '`',
		71303172: 'a',
		71303232: 'b',
		71303236: 'c',
		71304192: 'd',
		71304196: 'e',
		71304256: 'f',
		71304260: 'g',
		71319552: 'h',
		71319556: 'i',
		71319616: 'j',
		71319620: 'k',
		71320576: 'l',
		71320580: 'm',
		71320640: 'n',
		71320644: 'o',
		71565312: 'p',
		71565316: 'q',
		71565376: 'r',
		71565380: 's',
		71566336: 't',
		71566340: 'u',
		71566400: 'v',
		71566404: 'w',
		71581696: 'x',
		71581700: 'y',
		71581760: 'z',
		71581764: '{',
		71582720: '|',
		71582724: '}',
		71582784: '~',
	},
	{
		0: '\0',
		8388608: ' ',
		8388616: '!',
		8388736: '"',
		8388744: '#',
		8390656: '$',
		8390664: '%',
		8390784: '&',
		8390792: "'",
		8421376: '(',
		8421384: ')',
		8421504: '*',
		8421512: '+',
		8423424: ',',
		8423432: '-',
		8423552: '.',
		8423560: '/',
		8912896: '0',
		8912904: '1',
		8913024: '2',
		8913032: '3',
		8914944: '4',
		8914952: '5',
		8915072: '6',
		8915080: '7',
		8945664: '8',
		8945672: '9',
		8945792: ':',
		8945800: ';',
		8947712: '<',
		8947720: '=',
		8947840: '>',
		8947848: '?',
		134217728: '@',
		134217736: 'A',
		134217856: 'B',
		134217864: 'C',
		134219776: 'D',
		134219784: 'E',
		134219904: 'F',
		134219912: 'G',
		134250496: 'H',
		134250504: 'I',
		134250624: 'J',
		134250632: 'K',
		134252544: 'L',
		134252552: 'M',
		134252672: 'N',
		134252680: 'O',
		134742016: 'P',
		134742024: 'Q',
		134742144: 'R',
		134742152: 'S',
		134744064: 'T',
		134744072: 'U',
		134744192: 'V',
		134744200: 'W',
		134774784: 'X',
		134774792: 'Y',
		134774912: 'Z',
		134774920: '[',
		134776832: '\\',
		134776840: ']',
		134776960: '^',
		134776968: '_',
		142606336: '`',
		142606344: 'a',
		142606464: 'b',
		142606472: 'c',
		142608384: 'd',
		142608392: 'e',
		142608512: 'f',
		142608520: 'g',
		142639104: 'h',
		142639112: 'i',
		142639232: 'j',
		142639240: 'k',
		142641152: 'l',
		142641160: 'm',
		142641280: 'n',
		142641288: 'o',
		143130624: 'p',
		143130632: 'q',
		143130752: 'r',
		143130760: 's',
		143132672: 't',
		143132680: 'u',
		143132800: 'v',
		143132808: 'w',
		143163392: 'x',
		143163400: 'y',
		143163520: 'z',
		143163528: '{',
		143165440: '|',
		143165448: '}',
		143165568: '~',
	}
]

def encode(s):
    
    s = s.ljust(4, '\0') # pad input with null, which is ascii 0
    a = interleave[0][s[0]] + interleave[1][s[1]] + interleave[2][s[2]] + interleave[3][s[3]]
    
    return a

def decode(l):
	result = ''
	for i in l:
		first_byte = i & 0b00010001000100010001000100010001
		first_char = uninterleave[0][first_byte]
		
		second_byte = i & 0b00100010001000100010001000100010
		second_char = uninterleave[1][second_byte]
		
		third_byte = i & 0b01000100010001000100010001000100
		third_char = uninterleave[2][third_byte]
		
		forth_byte = i & 0b10001000100010001000100010001000
		forth_char = uninterleave[3][forth_byte]
	
		result += first_char + second_char + third_char + forth_char
	return result

print(decode([267657050, 233917524, 234374596, 250875466, 17830160]))
