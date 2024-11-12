#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

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