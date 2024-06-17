import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prev = new HashMap<Integer, Integer>();

        for (int i=0; i< nums.length; i++) {
            if (prev.containsKey(target - nums[i])) {
                return new int[]{i, prev.get(target-nums[i])};
            }

            prev.put(nums[i], i);

        }
    
        return new int[]{-1, -1};
    }
}