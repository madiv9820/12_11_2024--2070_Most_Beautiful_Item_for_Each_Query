from typing import List

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