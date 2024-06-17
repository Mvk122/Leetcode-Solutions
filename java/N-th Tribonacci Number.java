
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
    public int tribonacci(int n) {
        int[] prevs = {0, 1, 1};

        if (n < 3) {
            return prevs[n];
        }

        for (int i=2; i<n; i++) {
            int current = IntStream.of(prevs).sum();
            prevs[0] = prevs[1];
            prevs[1] = prevs[2];
            prevs[2] = current;
        }

        return prevs[2];
    }
}