
import java.util.Set;
import java.util.stream.Collectors;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;


class Solution {
    public int largestAltitude(int[] gain) {
        int current = 0; 
        int highest = 0;

        for (int g: gain) {
            current += g;
            highest = Math.max(current, highest); 
        }
        return highest;
    }
}