#include<bits/stdc++.h>
using namespace std;

long getMaxProfit(vector<int> pni, int k){
    int n = pni.size();

    long maxProfit = 0;
    long currMax = 0;
    long currentWindowProfit = 0;

    for (int i = 0; i < k; i++) {
        currentWindowProfit += pni[i];
        currMax = max(currMax, currentWindowProfit);
    }

    for (int i = k; i < n; i++) {
        currentWindowProfit = currentWindowProfit - pni[i - k] + pni[i];
        currMax = max(currMax, currentWindowProfit);
        if (currMax > maxProfit) {
            maxProfit = currMax;
        }
    }

    return maxProfit;
}

int main(){

    int n1;
    cin>>n1;

    
    vector<int> pnl(n1);

    for(int i =0; i<n1; i++){
        cin>>pnl[i];
    }

    int k;
    cin>>k;

    long ans = getMaxProfit(pnl, k);
    cout<<ans<< "\n";

    return 0;
    
}