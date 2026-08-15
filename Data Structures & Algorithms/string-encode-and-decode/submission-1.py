class Solution:

    def encode(self, strs: list[str]) -> str:
        en_str: str = ""
        for i in strs:
            en_str += f"{len(i)}${i}"
        return en_str
    
    def decode(self, msg: str) -> list[str]:
        de_str: list[str] = []
        size: int = 0
        i: int = 0

        while i < len(msg):
            if msg[i].isdigit():
                size = size * 10 + int(msg[i])
                i += 1
            elif msg[i] == "$":
                message: str = ""
                for j in range(i+1, i+size+1):
                    message += msg[j]
                de_str.append(message) 
                i += size + 1
                size = 0
            
        return de_str   