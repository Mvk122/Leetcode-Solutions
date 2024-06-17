import java.util.Set;
import java.util.stream.Collectors;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;


class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> occurences = new HashMap<>();

        for (int a: arr) {
            if (occurences.containsKey(a)) {
                occurences.put(a, occurences.get(a) + 1);
            } else {
                occurences.put(a, 1);
            }
        }

        HashSet<Integer> unique = new HashSet<>();

        for (Map.Entry<Integer, Integer> entry : occurences.entrySet()) {
            unique.add(entry.getValue());
        }

        return unique.size() == occurences.size();

    }
}