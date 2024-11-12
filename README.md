# Most Beautiful Item for Each Query (All Approaches)

- ## Approach 1:- Linear Search (Time Limit Exceeded)

    - ### Problem Intuition
        The task is to find the maximum beauty of items that can be bought given a list of items, where each item has a `price` and a `beauty` value. For each query, which represents the maximum price a user is willing to spend, we need to determine the most beautiful item that can be purchased for that price.

    - ### Intuition:
        For each query, we:
        1. Iterate through the list of items.
        2. Identify which items have a price less than or equal to the query price.
        3. Track the maximum beauty among these items.
        4. After processing all items for a query, store the maximum beauty found for that query.

        This approach is repeated for each query in the list of queries.

    - ### Approach
        1. **Iterate over each query**: For each query (representing the maximum affordable price), we will check all items to see which ones the user can afford.
        2. **Find the maximum beauty**: For each item, check if the item's price is less than or equal to the query price. If it is, compare the beauty of the item with the current maximum beauty and update it if necessary.
        3. **Store the result**: After processing all items for a given query, store the result (maximum beauty found for that query).
        4. **Return the result**: Once all queries have been processed, return the list of results (maximum beauties corresponding to each query).

        This approach ensures that we efficiently calculate the maximum beauty for each query, even though the solution is a brute-force one.

    - ### Time Complexity:
        - **Outer loop (queries)**: We iterate through all `Q` queries.
        - **Inner loop (items)**: For each query, we iterate through all `N` items.

        Thus, the overall time complexity is: __O(N * Q)__, where:
            - `N` is the number of items.
            - `Q` is the number of queries.

    - ### Space Complexity:
        - The space complexity is determined by the storage of the result list (which stores the maximum beauty for each query).
        - We need `O(Q)` space for storing the results.

        Thus, the space complexity is: __O(Q)__, where `Q` is the number of queries.

    - ### Code
        - **Python Code**

            ```python3 []
            class Solution:
                def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
                    # Initialize an empty list to store the results for each query
                    results = []

                    # Loop through each query price
                    for max_price in queries:
                        # Initialize the maximum beauty for the current query as 0
                        max_beauty = 0
                        
                        # Loop through each item (price, beauty) in the 'items' list
                        for price, beauty in items:
                            # If the item's price is less than or equal to the current query price
                            if price <= max_price:
                                # Update max_beauty if the current item's beauty is greater
                                max_beauty = max(max_beauty, beauty)
                        
                        # Append the result (maximum beauty) for the current query to the 'results' list
                        results.append(max_beauty)
                    
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
                        
                        // Iterate through each query (max price for the current query)
                        for(const int& max_price: queries) {
                            int max_Beauty = 0; // Initialize the maximum beauty for the current query
                            
                            // Iterate through each item in the items list (price, beauty)
                            for(auto& item: items)  {
                                int price = item[0], beauty = item[1];
                                
                                // If the price is less than or equal to the current query price
                                // Update maxBeauty if the current item's beauty is greater
                                max_Beauty = (price <= max_price) ? max(max_Beauty, beauty) : max_Beauty;
                            }
                            
                            // Add the maximum beauty found for the current query to the result
                            results.emplace_back(max_Beauty);
                        }

                        // Return the result for all queries
                        return results;
                    }
            };
            ```

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