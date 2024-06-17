
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;


class Solution {
    public int pivotIndex(int[] nums) {
        int right = IntStream.of(nums).sum();
        int left = 0;


        for (int i=0; i<nums.length; i++) {
            right -= nums[i];
            if (left == right) {
                return i;
            }
            left += nums[i];
        }

        return -1;

    }
}