#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *left;
    Node *right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

vector<int> verticalOrder(Node *root)
{

    if (root == nullptr)
    {
        return {};
    }

    map<int, map<int, vector<int>>> mp;
    queue<pair<Node *, pair<int, int>>> q;

    q.push(make_pair(root, make_pair(0, 0)));

    while (!q.empty())
    {

        pair<Node *, pair<int, int>> temp = q.front();
        q.pop();

        Node *frontNode = temp.first;
        int horiZontal = temp.second.first;
        int level = temp.second.second;

        mp[horiZontal][level].push_back(frontNode->data);

        if (frontNode->left)
        {
            q.push(make_pair(frontNode->left, make_pair(horiZontal - 1, level + 1)));
        }
        if (frontNode->right)
        {
            q.push(make_pair(frontNode->right, make_pair(horiZontal + 1, level + 1)));
        }
    }

    vector<int> ans;
    for (auto i : mp)
    {
        for (auto j : i.second)
        {
            for (auto k : j.second)
            {
                ans.push_back(k);
            }
        }
    }
    return ans;
}

int main()
{

    Node* root = new Node(1);
    
    root->left = new Node(2);
    root->right = new Node(3);

    root->left->left = new Node(4);
    root->left->right = new Node(6);
    
    root->right->left = new Node(5);
    root->right->right = new Node(7);
    
    root->left->right->right = new Node(8);
    root->right->right->right = new Node(7);
    
    
    vector<int> ans = verticalOrder(root);
    
    for(auto it : ans){
        cout<<it<<" ";
    }
}