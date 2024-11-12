- ## Approach 2:- Binary Search (Time Limit Exceeded)
    
    - ### Problem Intuition
        The problem involves finding the maximum beauty of items that can be bought, where each item has a `price` and a `beauty` value. For each query, which represents the maximum price a user is willing to spend, we need to determine the most beautiful item that can be purchased for that price.

    - ### Intuition:
        For each query, we:
        1. Sort the list of items by price to efficiently search for items that the user can afford.
        2. Use binary search to find the most expensive item within the price range for each query.
        3. Recursively search to find the highest beauty item that can be bought for the current price limit, considering both the left and right sides of the array.

    - ### Approach
        1. **Sort the items**: First, we sort the items based on their price. If two items have the same price, they are sorted by beauty in ascending order.
        2. **Binary Search Helper**: For each query, we perform a binary search to find the highest-priced item within the given maximum price. The binary search works by recursively splitting the range of items to find the maximum beauty.
            - If the price of the current item is less than or equal to the query price, we compare the beauty of the current item with the best beauty found in the left and right halves of the range.
            - If the price exceeds the query price, we search only the left half of the range.
        3. **Recursive Search**: The binary search helper function is called recursively to explore both the left and right ranges for higher beauty items, ultimately returning the maximum beauty found within the valid price range.
        4. **Repeat for all queries**: We repeat the binary search for each query and store the results.

    - ### Time Complexity:
        - **Sorting the Items**: Sorting the list of `N` items by price takes **O(N log N)**.
        - **Binary Search**: For each query, the binary search operates on the sorted list of `N` items. The binary search takes **O(log N)** time for each query.
        - **Total Complexity**: If there are `Q` queries, the total time complexity is **O(N log N + Q log N)**, where:
            - `N` is the number of items.
            - `Q` is the number of queries.

    - ### Space Complexity:
        - **Input Data Storage**: We store the `items` list and `queries` list, which take **O(N)** and **O(Q)** space respectively.
        - **Auxiliary Space for Recursion**: The recursion depth of the binary search is **O(log N)**, which is the maximum space needed for the recursion stack.
        - **Total Space Complexity**: The overall space complexity is **O(N + Q)**, where:
        - `N` is the number of items.
        - `Q` is the number of queries.
    
    - ### Code
        - **Python Solution**

            ```python3 []
            class Solution:
                def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
                    # Initialize an empty list to store the result for each query
                    results = []
                    
                    # Get the number of items
                    num_items = len(items)
                    
                    # Sort the items first by price, then by beauty in case of ties on price
                    items.sort(key = lambda item: (item[0], item[1]))

                    # Helper function to perform binary search to find the maximum beauty
                    def findMaxBeauty(startIndex: int, endIndex: int, maxPrice: int) -> int:
                        # Base case: if the search range is invalid (start index is greater than end index), return 0
                        if startIndex > endIndex:
                            return 0

                        # Find the middle index of the current range
                        midIndex = (startIndex + endIndex) // 2
                        price, beauty = items[midIndex]

                        # If the price of the current item is less than or equal to the max price, we consider it
                        if price <= maxPrice:
                            # Recursively search the left and right halves for potentially higher beauty items
                            leftBeauty = findMaxBeauty(startIndex, midIndex - 1, maxPrice)
                            rightBeauty = findMaxBeauty(midIndex + 1, endIndex, maxPrice)

                            # Return the maximum beauty from the current item and the left and right sides
                            return max(beauty, leftBeauty, rightBeauty)

                        # If the current item's price is greater than the max price, we only search the left side
                        return findMaxBeauty(startIndex, midIndex - 1, maxPrice)

                    # For each query, find the maximum beauty that can be bought with the given max price
                    for maxPrice in queries:
                        # Call the binary search helper function for each query and store the result
                        results.append(findMaxBeauty(0, num_items - 1, maxPrice))
                    
                    # Return the list of results for all queries
                    return results
            ```
        
        - **C++ Solution**

            ```C++ []
            class Solution {
                public:
                    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
                        // Create a vector to store the result for each query
                        vector<int> results;
                        
                        // Sort the items by price first, and then by beauty in non-increasing order (if price is the same)
                        sort(items.begin(), items.end(), [](const vector<int>& a, const vector<int>& b) {
                            return (a[0] < b[0] || (a[0] == b[0] && a[1] <= b[1]));
                        });

                        // Lambda function to find the maximum beauty for a given max price using binary search
                        function<int(int, int, int)> findMaxBeauty = [&](int startIndex, 
                                                                            int endIndex, 
                                                                            int maxPrice) -> int {
                            // Base case: if the search range is invalid (startIndex > endIndex), return 0
                            if (startIndex > endIndex)
                                return 0;

                            // Find the middle index in the current search range
                            int midIndex = (startIndex + endIndex) / 2;
                            int price = items[midIndex][0];  // Price of the item at midIndex
                            int beauty = items[midIndex][1]; // Beauty of the item at midIndex

                            // If the price of the current item is less than or equal to the maxPrice, we consider this item
                            if (price <= maxPrice) {
                                // Recursively search both the left and right sides of the list for items that may have higher beauty
                                int leftBeauty = findMaxBeauty(startIndex, midIndex - 1, maxPrice);  // Search left half
                                int rightBeauty = findMaxBeauty(midIndex + 1, endIndex, maxPrice);  // Search right half
                                // Return the maximum beauty from the current item and the left and right halves
                                return max(beauty, max(leftBeauty, rightBeauty));
                            }
                            
                            // If the current item's price is higher than the maxPrice, search the left side only
                            return findMaxBeauty(startIndex, midIndex - 1, maxPrice);
                        };

                        // For each query, call the findMaxBeauty function to find the max beauty within the given price limit
                        for (const int& maxPrice : queries) {
                            // Append the result of the query to the results vector
                            results.emplace_back(findMaxBeauty(0, items.size() - 1, maxPrice));
                        }

                        // Return the list of results for all queries
                        return results;
                    }
            };
            ```