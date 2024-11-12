from typing import List

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