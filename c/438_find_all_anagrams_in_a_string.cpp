#include<iostream>
#include<vector>
#include<string>
#include<unordered_set>
using namespace std;


class Solution {
    public:
        vector<int> findAnagrams(string s, string p){
            vector<int> result;
            if (s.size() < p.size()) return result;

            vector<int> pFreq(26, 0), windowFreq(26, 0);
            int windowSize = p.size();

            // Count frequency of characters in p
            for (char c : p) {
                pFreq[c - 'a']++;
            }

            for (int i = 0; i < s.size(); i++) {
                // Add current character to window
                windowFreq[s[i] - 'a']++;

                // Remove character left of the window
                if (i >= windowSize) {
                    windowFreq[s[i - windowSize] - 'a']--;
                }

                // Compare frequency arrays
                if (windowFreq == pFreq) {
                    result.push_back(i - windowSize + 1);
                }
            }

            return result;
        }
};


int main() {
    Solution sol;
    vector<int> res = sol.findAnagrams("cbaebabacd", "abc");
    for(int num : res){
        cout << num << endl;
    }
    return 0;
}