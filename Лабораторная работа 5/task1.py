list_1 = [{"bin": bin(c), "dec": c, "hex": hex(c), "oct": oct(c)} for c in range(16)]

from pprint import pprint
pprint(list_1)
