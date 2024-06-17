import java.util.Set;
import java.util.stream.Collectors;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int current = 0;
        int right = 0;
        
        while (right < k) {
            current += nums[right];
            right += 1;
        }
        int largest = current;
        
        while (right < nums.length) {
            current += nums[right] - nums[right-k];
            largest = Math.max(largest, current);
            right += 1;
        }

        return (double) largest / k;
    }
}