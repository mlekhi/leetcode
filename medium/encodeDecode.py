class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        if strs == []:
            print("")
            return ""
        elif strs == [""]:
            print(".")
            return "."

        for i in strs:
            output.append(i)  # Escape periods in the strings
            output.append(".")

        if output:
            output.pop()
        
        print(output)
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        if s == ".":
            return [""]
        elif s == "":
            return []

        parts = s.split(".")
        return parts

# was kind of annoying with some of the special cases!
# always remember to take those into account