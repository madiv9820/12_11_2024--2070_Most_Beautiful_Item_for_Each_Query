from typing import List

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