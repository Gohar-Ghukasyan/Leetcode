class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result, m, n, k = [], len(s), len(words), len(words[0])
        if m < n * k:
            return result

        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1  # Space: O(n * k)

        for i in xrange(k):  # Time:  O(k)
            left, count = i, 0
            tmp = collections.defaultdict(int)
            for j in xrange(i, m - k + 1, k):  # Time:  O(m / k)
                s1 = s[j:j + k];  # Time:  O(k)
                if s1 in lookup:
                    tmp[s1] += 1
                    if tmp[s1] <= lookup[s1]:
                        count += 1
                    else:
                        while tmp[s1] > lookup[s1]:
                            s2 = s[left:left + k]
                            tmp[s2] -= 1
                            if tmp[s2] < lookup[s2]:
                                count -= 1
                            left += k
                    if count == n:
                        result.append(left)
                        tmp[s[left:left + k]] -= 1
                        count -= 1
                        left += k
                else:
                    tmp = collections.defaultdict(int)
                    count = 0
                    left = j + k
        return result