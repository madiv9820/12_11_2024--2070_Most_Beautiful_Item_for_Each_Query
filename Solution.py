from typing import List

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