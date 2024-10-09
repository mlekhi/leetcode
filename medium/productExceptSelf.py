class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = []
        zero = 0

        for i in nums:
            if i == 0:
                zero += 1
            else:
                product *= i

        # print(product)

        for i in nums:
            if zero == 1:
                # print("one zero", i)
                if i == 0:
                    output.append(product)
                else:
                    output.append(0)
            elif zero > 1:
                output.append(0)
            else:
                output.append(product//i)

        return output