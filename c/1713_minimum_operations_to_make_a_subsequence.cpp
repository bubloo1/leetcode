#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& target, vector<int>& arr) {
        unordered_map<int, int> indexMap;
        for(int i = 0; i < target.size(); i++){
            indexMap[target[i]] = i;
        }  

        vector<int> seq;
        for(int num : arr) {
            if(indexMap.count(num)){
                seq.push_back(indexMap[num]);
            }
        }

        vector<int> list;

        auto lowerBoundCustom = [](vector<int>& list, int target) {
            int left = 0, right = list.size();
            while(left < right) {
                int mid = left + (right -left)/2;
                if(list[mid] < target) {
                    left = mid + 1;
                }else{
                    right = mid;
                }
            }
            return left;
        };

        for(int num : seq) {
            int pos = lowerBoundCustom(list, num);
            if(pos == list.size()) {
                list.push_back(num);
            }else{
                list[pos] = num;
            }
        }
        return target.size() - list.size();
    }
};

int main() {
    Solution sol;
    vector<int> target = {6,4,8,1,3,2};
    vector<int> arr = {4,7,6,2,3,8,6,1};
    cout << sol.minOperations(target,arr) <<endl;
    return 0;
}