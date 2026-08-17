# Write your solution here
def anagrams(string1: str, string2: str):
    if sorted(string1)==sorted(string2):
            return True
    return False

if __name__ == "__main__":
    anagrams(string1, string2)