class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_val(arr, ind):
            if ind == -1:
                return float(-inf)
            if ind == len(arr):
                return float(inf)
            return arr[ind]

        def get_ind(r_short, short_arr, long_arr):
            mid = (len(short_arr) + len(long_arr)) // 2
            r_long = mid - r_short
            return r_short - 1, r_short, r_long - 1, r_long

        def get_direction(l_short, r_short, l_long, r_long, short_arr, long_arr):
            if get_val(long_arr, r_long) < get_val(short_arr, l_short):
                return -1
            if get_val(long_arr, l_long) > get_val(short_arr, r_short):
                return 1
            return 0

        def get_result(l_short, r_short, l_long, r_long, short_arr, long_arr):
            if (len(short_arr) + len(long_arr)) % 2:
                return min(get_val(long_arr, r_long), get_val(short_arr, r_short))
            return (min(get_val(long_arr, r_long), get_val(short_arr, r_short)) + max(get_val(long_arr, l_long),
                                                                                      get_val(short_arr,
                                                                                              l_short))) / 2.0

        long_arr = nums1
        short_arr = nums2
        if len(nums1) < len(nums2):
            long_arr = nums2
            short_arr = nums1

        l, r = 0, len(short_arr)
        l_short = r_short = l_long = r_long = 1
        direction = 1
        while direction != 0:
            mid = (l + r) // 2
            l_short, r_short, l_long, r_long = get_ind(mid, short_arr, long_arr)
            direction = get_direction(l_short, r_short, l_long, r_long, short_arr, long_arr)
            if direction == 1:
                l = mid + 1
            elif direction == -1:
                r = mid - 1
        return get_result(l_short, r_short, l_long, r_long, short_arr, long_arr)