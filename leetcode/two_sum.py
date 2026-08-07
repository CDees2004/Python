def twoSum(nums: list[int], target: int) -> list[int]:
        for value in nums: 
            inverse: int = target - value
            if (inverse in nums and nums.index(value) != nums.index(inverse)):
                results = [nums.index(value), nums.index(inverse)]
            else:
                continue
        return results
        
if __name__ == "__main__":
    test_list = [3, 3]
    target: int = 9
    print(f"List: {test_list}\tTarget: {target}\tResult: {twoSum(test_list, target)}")