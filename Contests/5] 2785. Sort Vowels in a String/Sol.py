class Solution:
    def is_vowel(self, char):
        vowels = "aeiouAEIOU"
        return char in vowels

    def sortVowels(self, s: str) -> str:
        vowels = [char for char in s if self.is_vowel(char)]
        sorted_vowels = sorted(vowels)

        result = ""
        vowel_index = 0

        for char in s:
            if self.is_vowel(char):
                # Preserve the original case of the vowel
                if sorted_vowels[vowel_index].isupper():
                    result += sorted_vowels[vowel_index].upper()
                else:
                    result += sorted_vowels[vowel_index].lower()
                vowel_index += 1
            else:
                result += char

        return result
