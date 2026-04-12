class Solution:

    def encode(self, strs: List[str]) -> str:
        code = []

        for i in strs:
            code.append(f"{len(i)}")
            code.append("#")
            code.append(i)
        
        return "".join(code)

    def decode(self, s: str) -> List[str]:
        L = []
        nb = []
        length = None
        i = 0

        while i < len(s):
            print(length)
            if length is None:
                if s[i] != "#":
                    nb.append(s[i])
                    i += 1
                else:
                    length = int("".join(nb))
                    nb = []
                    i += 1 

            if length is not None:
                
                if length == 0:
                    L.append("")
                else:
                    word = s[i:i+length]
                    L.append(word)

                i += length 
                length = None

        return L
