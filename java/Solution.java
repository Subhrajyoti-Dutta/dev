import java.util.*;

public class Solution {
	public static int[] twoSum(int[] nums, int target) {
		int inverse;
		Map<Integer, Integer> myMap = new HashMap<>();
		for (int i = 0; i < nums.length - 1; i++) {
			inverse = target - nums[i];
			if (myMap.containsKey(inverse)) {
				System.out.println(i);
				return new int[] { myMap.get(inverse), i };
			} else {
				System.out.println(i);
				myMap.put(nums[i], i);
			}
		}
		return new int[2];
	}

	public static void main(String[] args) {
		int[] nums = { 3, 2, 4 };
		int target = 6;
		System.out.println(Arrays.toString(twoSum(nums, target)));

	}
}