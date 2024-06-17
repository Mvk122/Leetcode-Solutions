import sys

def main():
    with open(f"{sys.argv[1]}.java", "w+") as f:
        f.write("""
import java.util.Set;
import java.util.stream.Collectors;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
""")

if __name__ == "__main__":
    main()