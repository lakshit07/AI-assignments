import StringIO
import sys

class parser:

    def __init__ (self, string):
        self.lno = 1
        self.string = string
        self.ch = None

    # Next character    
    def nextch (self):
        self.ch, nxt = self.string.read(1), self.ch
        if nxt is not '\n':
            return nxt
        else:
            self.lno += 1
            return nxt

    # Look ahead of 1
    def nextch_util (self):
        if self.ch is not None:
            return self.ch
        else:    
            self.ch = self.string.read (1)
            return self.ch

    # Skips Delimiters         
    def skip(self):
        delim = ' \t\r\n'
        newline = '\r\n'
        while True:
            ch = self.nextch_util()
            if not ch or ch not in delim:
                break
            else:
                self.nextch()

    # Returns an atom            
    def atomizer(self):
        result = self.nextch()
        delim = ' \t\r\n'
        paren = ')('
        while True:
            ch = self.nextch_util()
            if ch in delim or ch in paren:
                return result
            else:
                result = result + self.nextch()

    # Reads a list in (...)            
    def read_list (self):
        ans = []
        self.nextch()
        while True:
            self.skip()
            c = self.nextch_util()
            if c is not ')':
                exp = self.read()
                ans.append(exp)
            else:
                ch = self.nextch()
                fans = tuple(ans)
                return fans    

    # Main parser function            
    def read(self):
        self.skip()
        digits = '0123456789'
        ch = self.nextch_util()

        if ch in digits:
            atom = self.atomizer()
            number = True
            for ch in atom:
                if ch in digits:
                    continue
                else:    
                    number = False
                    break

            if number:
                return int(atom)
            else:
                return atom

        elif ch == '(':
            return self.read_list()        
        
        else:
            return self.atomizer()

def parse_string(s):
    strng = StringIO.StringIO (s)
    obj = parser(strng)
    return obj.read()
    
'''
def main():
    with open('rules1.txt') as fp:
        for lno in fp:
            print parse_string(lno)


if __name__ == "__main__":
    main()
'''              