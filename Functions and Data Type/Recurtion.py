def permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            first_char = s[i]
            remaining_chars = s[:i] + s[i+1:]
            subperms = permutations(remaining_chars)
            for perm in subperms:
                perms.append(first_char + perm)
        return perms

# Example usage:
string = "abc"
print(permutations(string))
