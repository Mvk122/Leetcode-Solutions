import java.util.Set;
import java.util.stream.Collectors;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;


class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        HashSet<Integer> nums1set = Arrays.stream(nums1).boxed().collect(Collectors.toCollection(HashSet::new));
        HashSet<Integer> nums2set = Arrays.stream(nums2).boxed().collect(Collectors.toCollection(HashSet::new));

        ArrayList<Integer> in_nums1 = new ArrayList<Integer>();
        ArrayList<Integer> in_nums2 = new ArrayList<Integer>();

        for (Integer num: nums1set) {
            if (!nums2set.contains(num)) {
                in_nums1.add(num);
            }
        }
        for (Integer num: nums2set) {
            if (!nums1set.contains(num)) {
                in_nums2.add(num);
            }
        }
        return Arrays.asList(in_nums1, in_nums2);  
    }
}