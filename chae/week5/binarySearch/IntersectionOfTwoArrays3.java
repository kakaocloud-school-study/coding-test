package codingTestStudy.week5.binarySearch;

import java.util.ArrayList;
import java.util.Arrays;

public class IntersectionOfTwoArrays3 {
    public static int[] intersection(int[] nums1, int[] nums2) {
        nums1 = Arrays.stream(nums1).distinct().toArray();
        nums2 =Arrays.stream(nums2).distinct().toArray();
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        ArrayList<Integer> result = new ArrayList<>();
        for (int i=0; i<nums2.length; i++){
            int start =0;
            int end = nums1.length-1;
            while (start<=end){
                int mid = (start+end)/2;
                if(nums1[mid]==nums2[i]){
                    result.add(nums2[i]);
                    break;
                }else if (nums1[mid]>nums2[i]){
                    end = mid - 1;
                }else {
                    start = mid + 1;
                }
            }
        }
        int size = result.size();
        int[] result2 = new int[size];
        for (int i=0; i< size; i++){
            result2[i] = result.get(i);
        }
        return result2;
    }

    public static void main(String[] args) {
        int[] nums1 = {4,9,5};
        int[] nums2 = {9,4,9,8,4};
        System.out.println(Arrays.toString(intersection(nums1, nums2)));
    }
}
