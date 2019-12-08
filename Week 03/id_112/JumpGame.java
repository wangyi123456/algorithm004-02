package datastruct.greedy;

/**
 * 55. 跳跃游戏
 * 给定一个非负整数数组，你最初位于数组的第一个位置。
 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 判断你是否能够到达最后一个位置。

 示例 1:
 输入: [2,3,1,1,4]
 输出: true
 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

 示例 2:
 输入: [3,2,1,0,4]
 输出: false
 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

 */
public class JumpGame {

    /**
     * 方法一：贪心
     当我们把代码改成自底向上的模式，我们会有一个重要的发现，从某个位置出发，我们只需要找到第一个标记为 GOOD 的坐标（由跳出循环的条件可得），也就是说找到最左边的那个坐标。
     如果我们用一个单独的变量来记录最左边的 GOOD 位置，我们就可以避免搜索整个数组，进而可以省略整个 memo 数组。
     从右向左迭代，对于每个节点我们检查是否存在一步跳跃可以到达 GOOD 的位置（currPosition + nums[currPosition] >= leftmostGoodIndex）。
     如果可以到达，当前位置也标记为 GOOD ，同时，这个位置将成为新的最左边的 GOOD 位置，一直重复到数组的开头，如果第一个坐标标记为 GOOD 意味着可以从第一个位置跳到最后的位置。

     模拟一下这个操作，对于输入数组 nums = [9, 4, 2, 1, 0, 2, 0]，我们用 G 表示 GOOD，
     用 B 表示 BAD 和 U 表示 UNKNOWN。我们需要考虑所有从 0 出发的情况并判断坐标 0 是否是好坐标。由于坐标 1 是 GOOD，
     我们可以从 0 跳到 1 并且 1 最终可以跳到坐标 6，所以尽管 nums[0] 可以直接跳到最后的位置，我们只需要一种方案就可以知道结果。

     复杂度分析

     时间复杂度：O(n)，只需要访问 nums 数组一遍，共 n个位置，n是 nums 数组的长度。
     空间复杂度：O(1)，不需要额外的空间开销。
     *
     */
     public boolean canJump(int[] nums) {
         int lastPos = nums.length - 1;
         for (int i = nums.length - 1;i >= 0;i--) {
             if (i + nums[i] >= lastPos) {
                 lastPos = i;
             }
         }
         return lastPos == 0;
     }
}
