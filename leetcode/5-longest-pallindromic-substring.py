"""5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return _longest_pallindrome_dp(s=s)


def _longest_pallindrome_dp(s: str) -> str:
    if len(s) <= 1:
        return s
    if len(s) == 2:
        return s if s[0] == s[1] else s[0]
    n = len(s)
    # A dict that maps (start_ix, end_ix) -> is_pallindrome
    # We will build this bottoms up. So all str of sz 1 start at each index
    # Then all chars of sz 2, starting at each ix and so on.
    # When we want to check if s="ababa" if s[0]=a to s[4]=a is a pallindrome,
    # we check if s[0]==s[4] and s[1] to s[3] was a pallindrome.
    is_pal_map = [[None] * n for _ in range(n)]
    max_pal = (0, 0)
    for sz in range(0, n):
        for start_ix in range(0, n):
            end_ix = start_ix + sz
            if end_ix == n:
                break
            if sz == 0:
                is_pal = True
            elif sz == 1:
                is_pal = s[start_ix] == s[end_ix]
            else:
                is_pal = (s[start_ix] == s[end_ix]) and is_pal_map[start_ix + 1][
                    end_ix - 1
                ]
            is_pal_map[start_ix][end_ix] = is_pal
            if is_pal and ((end_ix - start_ix) > (max_pal[1] - max_pal[0])):
                max_pal = (start_ix, end_ix)
    return s[max_pal[0] : max_pal[1] + 1]


def _longest_pallindrome_expansion(s: str) -> str:
    if len(s) <= 1:
        return s
    n = len(s)
    max_pal = (0, 0)
    for center in range(n):
        max_pal = _max_pal_from_center(s=s, center=center, max_pal_so_far=max_pal)
    return s[max_pal[0] : (max_pal[1] + 1)]


def _max_pal_from_center(s, center, max_pal_so_far):
    max_pal = max_pal_so_far
    for lt in (center, center - 1):
        # lt, rt = i-1, i+1 odd arrays
        # lt, rt = i, i+1 even arrays
        rt = center + 1
        max_pal_center = _max_pal_from_center_helper(lt=lt, rt=rt, s=s)
        max_pal = _update_max_pal(
            max_pal=max_pal, lt=max_pal_center[0], rt=max_pal_center[1]
        )
    return max_pal


def _max_pal_from_center_helper(s, lt, rt):
    """Expands from center and checks for pallindrome"""
    n = len(s)
    while (lt >= 0 and rt < n) and (s[lt] == s[rt]):
        lt -= 1
        rt += 1
    return (lt + 1, rt - 1)


def _update_max_pal(
    max_pal: Optional[Tuple[int, int]],
    lt,
    rt,
):
    if lt > rt:
        # Ex: a[0] != a[1], lt = lt+1=1, rt=rt-1=0
        return max_pal
    elif rt - lt > max_pal[1] - max_pal[0]:
        return (lt, rt)
    else:
        return max_pal


########################################################################################
#                           Revision 1
########################################################################################


def _longest_pallindromic_sub_dp_r1(s: str) -> str:
    n = len(s)
    # Stores if s[i:j+1] is a pallindrome in is_pall[i][j].
    is_pall = [[False] * n for _ in range(n)]
    max_lt, max_rt = 0, 0
    for sz in range(n):
        for lt in range(n - sz):
            rt = lt + sz
            if lt == rt:
                pal = True
            elif sz == 1:
                pal = s[lt] == s[rt]
            else:
                pal = (s[lt] == s[rt]) and is_pall[lt + 1][rt - 1]
            is_pall[lt][rt] = pal
            if pal and ((rt - lt) > (max_rt - max_lt)):
                max_lt, max_rt = lt, rt
    return s[max_lt : max_rt + 1]


def _longest_pall_subs_sw_r1(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    max_pal = (0, 0)
    for center in range(n - 1):
        # even len pal
        even_max = _find_max_pal_at_center(s=s, lt=center, rt=center + 1)
        # odd len pal
        odd_max = _find_max_pal_at_center(s=s, lt=center - 1, rt=center + 1)
        max_pal = _update_max_pal_2(
            max_pal=_update_max_pal_2(max_pal=max_pal, contender=even_max),
            contender=odd_max,
        )
    return s[max_pal[0] : max_pal[1] + 1]


def _find_max_pal_at_center(s: str, lt: int, rt: int) -> Optional[Tuple[int, int]]:
    n = len(s)
    if (lt < 0 or rt >= n) or (s[lt] != s[rt]):
        return None
    while lt > 0 and rt < n:
        if s[lt] == s[rt]:
            lt -= 1
            rt += 1
        else:
            break
    return (lt + 1, rt - 1)


def _update_max_pal_2(
    max_pal: Tuple[int, int], contender: Optional[Tuple[int, int]]
) -> Tuple[int, int]:
    if contender is None:
        return max_pal
    elif (contender[1] - contender[0]) > (max_pal[1] - max_pal[0]):
        return contender
    else:
        return max_pal
