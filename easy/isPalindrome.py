class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while right > left:
            # print(right)
            # print(right, left, s[right], s[left])
            while right >= 0 and not s[right].isalnum():
                right -= 1
            while left < len(s) and not s[left].isalnum():
                left += 1

            if right <= left:
                break

            if s[left].lower() != s[right].lower():
                print(s[left], s[right])
                return False
            
            left += 1
            right -= 1

        return True
    

# two pointer approach was good cuz you ate up space complexity
# start memorizing criteria of when to use two pointer