- ## Approach 3:- Optimized Binary Search
    
    - ### Problem Intuition
        We are given a list of items, where each item consists of a price and a beauty value. Additionally, we have a list of queries, each representing a maximum price that a user is willing to spend. For each query, we need to find the item with the highest beauty that can be bought without exceeding the given price. We aim to find an efficient solution to answer multiple queries after preprocessing the item list.

    - ### Approach
        1. **Sorting the Items**:
            - First, we sort the `items` list by price in non-decreasing order. If two items have the same price, they are sorted by beauty in non-decreasing order. This sorting allows us to efficiently search for the maximum beauty that can be bought within a given price constraint.
        
        2. **Preprocessing Maximum Beauty for Each Price**:
            - As we iterate through the sorted list of items, we keep track of the maximum beauty seen so far and store it in a map `max_Beauty_At_Price`. This map will store the maximum beauty available for each price point.
            - For each price, we update the maximum beauty if the current item has a higher beauty than what we've previously encountered.

        3. **Binary Search for Each Query**:
            - For each query, which represents the maximum price a user is willing to spend, we perform a binary search on the sorted `items` list to find the maximum beauty that can be bought with the given price.
            - If the price of the item at the middle index is within the budget (i.e., less than or equal to the maximum price), we consider that item and search the right side of the list for potentially higher beauty items.
            - If the price is higher than the query price, we only search the left half of the list.

        4. **Efficient Query Resolution**:
            - Once the maximum beauty for a given price has been found, we return the result and move on to the next query.

    - ### Time Complexity
        The solution can be broken down into the following steps:

        1. **Sorting the Items**:
            - Sorting the items by price takes **O(N log N)**, where `N` is the number of items.
        2. **Preprocessing the Maximum Beauty**:
            - We loop through the sorted list of items once, updating the `max_Beauty` for each price. This takes **O(N)** time.
        3. **Binary Search for Each Query**:
            - For each query, we perform a binary search on the `items` list, which takes **O(log N)** time.
            - Given `Q` queries, the total time complexity for processing all queries is **O(Q log N)**.

        Thus, the total time complexity is: __O(N log N)__ + __O(N)__ + __O(Q log N)__ = __O(N log N + Q log N)__

    - ### Space Complexity
        The space complexity is determined by the following factors:

        1. **Storing the Sorted Items**:
            - We store the `items` list, which takes **O(N)** space.
        2. **Storing the Maximum Beauty for Each Price**:
            - The `max_Beauty_At_Price` map stores the maximum beauty for each distinct price. In the worst case, this map will store `N` entries, resulting in **O(N)** space.
        3. **Storing the Results for Queries**:
            - We store the results for each query, which requires **O(Q)** space.

        Thus, the overall space complexity is: __O(N + Q)__
    
    - ### Code
        - **Python Solution**
            ```python3 []
            class Solution:
                def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
                    # Initialize an empty list to store the result for each query
                    results = []
                    
                    # Get the total number of items
                    num_items = len(items)
                    
                    # Sort the items first by price, then by beauty in case of ties on price
                    items.sort(key = lambda item: (item[0], item[1]))

                    # Dictionary to store the maximum beauty found for each price point
                    max_Beauty_At_Price = {}
                    max_Beauty = 0

                    # Iterate over each item and track the maximum beauty for each price point
                    for price, beauty in items:
                        # Update the maximum beauty found so far
                        max_Beauty = max(max_Beauty, beauty)
                        # Store the maximum beauty found for this price in the dictionary
                        max_Beauty_At_Price[price] = max_Beauty 

                    # Helper function to perform binary search to find the maximum beauty for a given maxPrice
                    def findMaxBeauty(startIndex: int, endIndex: int, maxPrice: int) -> int:
                        # Base case: If the search range is invalid (start index > end index), return 0
                        if startIndex > endIndex:
                            return 0

                        # Find the middle index of the current search range
                        midIndex = (startIndex + endIndex) // 2
                        price, beauty = items[midIndex]

                        # If the price of the current item is less than or equal to the maxPrice, consider it
                        if price <= maxPrice:
                            # Recursively search the right side for higher beauty items that fit the maxPrice constraint
                            rightBeauty = findMaxBeauty(midIndex + 1, endIndex, maxPrice)

                            # Return the maximum beauty found between the current item and the right side
                            return max(max_Beauty_At_Price[price], rightBeauty)

                        # If the current item's price exceeds the maxPrice, search only the left side
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
                        
                        // Sort the items by price first, and then by beauty in non-increasing order
                        // (if price is the same, sort by beauty in non-decreasing order)
                        sort(items.begin(), items.end(), [](const vector<int>& a, const vector<int>& b) {
                            return (a[0] < b[0] || (a[0] == b[0] && a[1] <= b[1]));
                        });

                        // Dictionary to store the maximum beauty found for each price point
                        unordered_map<int, int> max_Beauty_At_Price;
                        int max_Beauty = 0;
                        
                        // Iterate through the sorted items to fill in the dictionary
                        for(auto& item: items) {
                            int price = item[0], beauty = item[1];
                            // Update the maximum beauty found so far
                            max_Beauty = max(max_Beauty, beauty);
                            // Store the maximum beauty for this price
                            max_Beauty_At_Price[price] = max_Beauty;
                        }

                        // Lambda function to perform binary search to find the maximum beauty for a given maxPrice
                        function<int(int, int, int)> findMaxBeauty = [&](int startIndex, 
                                                                            int endIndex, 
                                                                            int maxPrice) -> int {
                            // Base case: if the search range is invalid (startIndex > endIndex), return 0
                            if (startIndex > endIndex)
                                return 0;

                            // Find the middle index of the current search range
                            int midIndex = (startIndex + endIndex) / 2;
                            int price = items[midIndex][0];  // Price of the item at midIndex
                            int beauty = items[midIndex][1]; // Beauty of the item at midIndex

                            // If the price of the current item is less than or equal to the maxPrice, we consider this item
                            if (price <= maxPrice) {
                                // Recursively search the right half of the list for potentially better items
                                int rightBeauty = findMaxBeauty(midIndex + 1, endIndex, maxPrice);  // Search right half
                                // Return the maximum beauty found between the current item and the right half
                                return max(max_Beauty_At_Price[price], rightBeauty);
                            }
                            
                            // If the current item's price is greater than the maxPrice, search the left side
                            return findMaxBeauty(startIndex, midIndex - 1, maxPrice);
                        };

                        // For each query, call the findMaxBeauty function to find the maximum beauty within the given price limit
                        for (const int& maxPrice : queries) {
                            // Append the result of the query to the results vector
                            results.emplace_back(findMaxBeauty(0, items.size() - 1, maxPrice));
                        }

                        // Return the list of results for all queries
                        return results;
                    }
            };
            ```