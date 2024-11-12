#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

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

int main() {
    vector<vector<int>> items;
    vector<int> queries;

    int input;
    cin >> input;

    while(input != -1) {
        int price, beauty;
        cin >> price >> beauty;
        
        items.push_back({price, beauty});
        cin >> input;
    }
    
    cin >> input;
    while(input != -1) {
        int query;
        cin >> query;

        queries.emplace_back(query);
        cin >> input;
    }

    Solution sol;
    vector<int> result = sol.maximumBeauty(items = items, queries = queries);
    for(const int& res: result)
        cout << res << " ";
    cout << endl;
}