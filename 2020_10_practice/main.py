


# Given a string s, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    seen_letters_to_their_last_seen_index = {}
    longest_streak = 0
    left_i = 0
    i = 0
    left_i_has_been_untouched = True
    while i < len(s):
        if s[i] in seen_letters_to_their_last_seen_index:
            longest_streak = max(longest_streak, i - left_i)
            if left_i <= seen_letters_to_their_last_seen_index[s[i]] + 1:
                left_i = seen_letters_to_their_last_seen_index[s[i]] + 1
            left_i_has_been_untouched = False
        seen_letters_to_their_last_seen_index[s[i]] = i
        i = i + 1
        if left_i_has_been_untouched or i == len(s):
            longest_streak = max(longest_streak, i - left_i)
    return longest_streak

if __name__ == '__main__':

    var1 = "abcabcbb"
    print(lengthOfLongestSubstring(var1)) # should print 3, from finding "abc"
    var2 = "bbbbb"
    print(lengthOfLongestSubstring(var2)) # should print 1, from finding "b"
    var3 = "pwwkew"
    print(lengthOfLongestSubstring(var3)) # should print 3, from finding "wke"
    var4 = ""
    print(lengthOfLongestSubstring(var4)) # should print 0, from finding ""
    var5 = " "
    print(lengthOfLongestSubstring(var5)) # should print 1, from finding " "
    var6 = "abba"
    print(lengthOfLongestSubstring(var6)) # should print 2, from finding "ab"
    var7 = "au"
    print(lengthOfLongestSubstring(var7)) # should print 2, from finding "au"
    var8 = "aab"
    print(lengthOfLongestSubstring(var8)) # should print 2, from finding "ab"
