#include <iostream>
#include <vector>
using namespace std;

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