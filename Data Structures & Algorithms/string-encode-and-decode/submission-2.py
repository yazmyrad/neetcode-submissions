class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))+'!'+s
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        i = 0
        while i < len(s):
            n = int(s[i:].split('!',1)[0])
            decoded.append(s[i+len(str(n))+1:i+len(str(n))+1+n])
            i = i+len(str(n))+1+n
        return decoded