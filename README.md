- ## Linear Search
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