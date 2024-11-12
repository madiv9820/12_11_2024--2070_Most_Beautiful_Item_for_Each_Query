# [2070. Most Beautiful Item for Each Query](https://leetcode.com/problems/most-beautiful-item-for-each-query)

__Type:__ Medium <br>
__Topics:__ Array, Binary Search, Sorting <br>
__Companies:__ razorpay, Postmates
<hr>

You are given a 2D integer array `items` where <code>items[i] = [price<sub>i</sub>, beauty<sub>i</sub>]</code> denotes the __price__ and __beauty__ of an item respectively.

You are also given a __0-indexed__ integer array `queries`. For each `queries[j]`, you want to determine the __maximum beauty__ of an item whose price is __less than or equal__ to `queries[j]`. If no such item exists, then the answer to this query is `0`.

Return _an array_ `answer` _of the same length as queries where_ `answer[j]` _is the answer to the_ <code>j<sup>th</sup></code> _query_.
<hr>

### Examples:

- __Example 1:__ <br>
__Input:__ items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6] <br>
__Output:__ [2,4,5,5,6,6] <br>
__Explanation:__ <br> - For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2. <br> - For queries[1]=2, the items which can be considered are [1,2] and [2,4]. <br> The maximum beauty among them is 4. <br> - For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5]. <br> The maximum beauty among them is 5. <br> - For queries[4]=5 and queries[5]=6, all items can be considered. <br> Hence, the answer for them is the maximum beauty of all items, i.e., 6.

- __Example 2:__ <br>
__Input:__ items = [[1,2],[1,2],[1,3],[1,4]], queries = [1] <br>
__Output:__ [4] <br>
__Explanation:__ <br>
The price of every item is equal to 1, so we choose the item with the maximum beauty 4. <br>
Note that multiple items can have the same price and/or beauty.  

- __Example 3:__ <br>
__Input:__ items = [[10,1000]], queries = [5] <br>
__Output:__ [0] <br>
__Explanation:__ <br>
No item has a price less than or equal to 5, so no item can be chosen. <br>
Hence, the answer to the query is 0.
<hr>

### Constraints:

- <code>1 <= items.length, queries.length <= 10<sup>5</sup></code>
- `items[i].length == 2`
- <code>1 <= price<sub>i</sub>, beauty<sub>i</sub>, queries[j] <= 10<sup>9</sup></code>
<hr>

### Hints:

- Can we process the queries in a smart order to avoid repeatedly checking the same items?
- How can we use the answer to a query for other queries?