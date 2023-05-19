#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
# Idea:
# 1. Create a dictionary to store the order of each letter
# 2. Compare each word with the next word
# 3. If the first letter of the first word is greater than the first letter of the second word, return False
# 4. If the first letter of the first word is less than the first letter of the second word, return True
# 5. If the first letter of the first word is equal to the first letter of the second word, compare the second letter of the first word with the second letter of the second word
# 6. Repeat step 3 to 5 until the end of the word
# 7. If all words are in order, return True
# 8. If any word is not in order, return False

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = [0] * 26
        for i, element in enumerate(order):
            order_dict[ord(element) - ord('a')] = i
        modified_words = []
        for word in words:
            modified_word = ''.join(chr(order_dict[ord(char) - ord('a')] + ord('a')) for char in word)
            modified_words.append(modified_word)
        return modified_words == sorted(modified_words)


# @lc code=end

