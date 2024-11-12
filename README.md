- ## Approach 4:- Optimized Binary Search (Space)
    
    - ### Problem Intuition
        The task is to determine the maximum beauty of an item that can be bought given a list of items, where each item has a price and a beauty value. For each query (which represents the maximum price the user is willing to spend), we need to return the maximum beauty of items that are affordable within the given price limit.

    - ### Intuition:
        1. **Sort the items by price**: This allows us to use binary search to efficiently find the most beautiful item that can be bought within a given price.
        2. **Track the maximum beauty**: As we iterate through the sorted items, we track the most beautiful item that can be bought at or below each price point.
        3. **Use binary search**: For each query (maximum price), we perform a binary search to find the maximum beauty of items that can be bought within that price.

    - ### Approach
        1. **Sorting the Items**:
            - First, we sort the items by price. If two items have the same price, we sort them by beauty in non-decreasing order. Sorting helps to quickly find the items that can be bought within a given price using binary search.
        2. **Tracking Maximum Beauty for Each Price**:
            - As we iterate through the sorted items, we maintain a dictionary `max_Beauty_At_Price` that maps each price to the maximum beauty seen so far. This allows us to efficiently retrieve the best possible beauty for a given price.
        3. **Binary Search for Each Query**:
            - For each query, we perform binary search on the sorted list of items to find the highest price that is less than or equal to the query price. Using this index, we return the corresponding maximum beauty for that price.
        4. **Returning the Results**:
            - After processing all queries, we return a list of results, where each result corresponds to the maximum beauty that can be bought for the respective price query.

    - ### Time Complexity
        1. **Sorting Step**:
            - Sorting the items by price takes **O(N log N)**, where `N` is the number of items.
        2. **Binary Search Step**:
            - For each query, performing binary search takes **O(log N)**, where `N` is the number of items.
        3. **Total Complexity**:
            - Since we perform binary search for each of the `Q` queries, the overall time complexity is:
                - **O(N log N + Q log N)**, where `N` is the number of items and `Q` is the number of queries.

        The **O(N log N)** is for sorting the items, and **O(Q log N)** is for processing each query using binary search.

    - ### Space Complexity
        1. **Space for Sorted Items**:
            - Sorting the items does not require extra space, so space complexity is dominated by the storage used for the result list.
        2. **Space for Dictionary**:
            - The dictionary `max_Beauty_At_Price` requires **O(N)** space, as we store the maximum beauty for each distinct price.
        3. **Total Space Complexity**:
            - The overall space complexity is **O(N)**, where `N` is the number of items, due to the space used by the dictionary.
    
    - ### Code
        - **Python Solution**

            ```python3 [] 
            class Solution:
                def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
                    # Initialize an empty list to store the result for each query
                    results = []
                    
                    # Get the total number of items in the input list
                    num_items = len(items)
                    
                    # Sort the items list first by price, and then by beauty (in case of ties on price)
                    items.sort(key = lambda item: (item[0], item[1]))

                    # Dictionary to store the maximum beauty found for each price point
                    max_Beauty_At_Price = {}
                    max_Beauty = 0

                    # Iterate through each item to track the maximum beauty found for each price point
                    for price, beauty in items:
                        # Update the maximum beauty seen so far
                        max_Beauty = max(max_Beauty, beauty)
                        # Store the maximum beauty for the current price in the dictionary
                        max_Beauty_At_Price[price] = max_Beauty 

                    # Helper function to perform binary search to find the maximum beauty for a given maxPrice
                    def findMaxBeauty(startIndex: int, endIndex: int, maxPrice: int) -> int:
                        max_Beauty = 0  # Initialize the variable to store the best beauty found within the price limit
                        
                        # Perform binary search to find the most beautiful item that is affordable within maxPrice
                        while startIndex <= endIndex:
                            midIndex = (startIndex + endIndex) // 2  # Find the middle index
                            price, beauty = items[midIndex]  # Get the price and beauty of the item at the mid index

                            # If the item price is less than or equal to the max price, consider it
                            if price <= maxPrice:
                                # Update the maximum beauty found so far
                                max_Beauty = max(max_Beauty, max_Beauty_At_Price[price])
                                # Search the right half of the list to find better (more expensive) items
                                startIndex = midIndex + 1
                            else:
                                # If the price of the item is greater than the max price, search the left half
                                endIndex = midIndex - 1

                        # Return the maximum beauty found within the given price limit
                        return max_Beauty

                    # For each query (maxPrice), find the maximum beauty of the items that can be bought
                    for maxPrice in queries:
                        # Perform binary search for each query to find the max beauty for that price and store the result
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
                        
                        // Sort the items first by price, and then by beauty in non-decreasing order
                        // If two items have the same price, sort them by beauty in non-decreasing order
                        sort(items.begin(), items.end(), [](const vector<int>& a, const vector<int>& b) {
                            return (a[0] < b[0] || (a[0] == b[0] && a[1] <= b[1]));
                        });

                        // Dictionary to store the maximum beauty found for each price point
                        unordered_map<int, int> max_Beauty_At_Price;
                        int max_Beauty = 0; // Variable to keep track of the maximum beauty seen so far
                        
                        // Iterate through the sorted items to fill the dictionary with max beauty for each price point
                        for(auto& item: items) {
                            int price = item[0], beauty = item[1];
                            // Update the maximum beauty encountered so far
                            max_Beauty = max(max_Beauty, beauty);
                            // Store the maximum beauty for the current price
                            max_Beauty_At_Price[price] = max_Beauty;
                        }

                        // Lambda function to perform binary search to find the maximum beauty for a given maxPrice
                        function<int(int, int, int)> findMaxBeauty = [&](int startIndex, 
                                                                            int endIndex, 
                                                                            int maxPrice) -> int {
                            int max_Beauty = 0; // Initialize to zero as we are looking for the best beauty
                            
                            // Perform binary search on the sorted items to find the best item within the price limit
                            while(startIndex <= endIndex) {
                                int midIndex = (startIndex + endIndex) / 2; // Find the middle index
                                int price = items[midIndex][0]; // Get the price of the item at the middle index

                                // If the price of the current item is less than or equal to maxPrice, consider this item
                                if(price <= maxPrice) {
                                    // Update max_Beauty to the maximum beauty found so far within the price limit
                                    max_Beauty = max(max_Beauty, max_Beauty_At_Price[price]);
                                    // Since the list is sorted, we can search the right half for items with higher prices
                                    startIndex = midIndex + 1;
                                }
                                else {
                                    // If the price is greater than maxPrice, search the left half (lower prices)
                                    endIndex = midIndex - 1;
                                }
                            }

                            return max_Beauty; // Return the best beauty found within the max price
                        };

                        // For each query, find the maximum beauty for that price using binary search
                        for (const int& maxPrice : queries) {
                            // Call the binary search function for the current query price
                            results.emplace_back(findMaxBeauty(0, items.size() - 1, maxPrice));
                        }

                        // Return the results vector, which contains the maximum beauty for each query
                        return results;
                    }
            };
            ```