#include<iostream>
using namespace std;

class Node{
    public:

    int data , height;
    Node *left, *right;

    Node(int value){
        this->data = value;
        height = 1;
        left = right = NULL;
    }
};

int getHeight(Node *root){
    if(!root){
        return 0;
    }
    return root->height;
}

int getBalance(Node *root){
    return getHeight(root->left) - getHeight(root->right); 
}

Node* rightRotation(Node* root){

     if (!root || !root->left) return root; 

    Node* child = root->left;
    Node* childRight = child->right;

    child->right = root;
    root->left = childRight;
    
    // update height   
    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
    child->height = 1 + max(getHeight(child->left), getHeight(child->right));
    return child;
}

Node* leftRotation(Node* root){
    if (!root || !root->right) return root;

    Node* child = root->right;
    Node* childLeft = child->left;

    child->left = root;
    root->right = childLeft;

    // update height
    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
    child->height = 1 + max(getHeight(child->left), getHeight(child->right));
    return child;
}

Node* insert(Node *root, int key){

    if(!root){
        return new Node(key);
    }

    if(key < root->data){
        root->left = insert(root->left, key);
    }else if(key > root->data){
        root->right = insert(root->right, key);
    }
    else{
        return root;
    }

    // updating height
    root->height = 1 + max(getHeight(root->left),getHeight(root->right));


    // checking balanced or not
    int balance_factor = getBalance(root);

    // left left imbalance
    if(balance_factor > 1 && key < root->left->data){
        return rightRotation(root);
    }
    // right right imbalance
    else if(balance_factor < -1 && key > root->right->data){
        return leftRotation(root);
    }
    // left right imbalance
    else if(balance_factor > 1 && key > root->left->data){
        root->left = leftRotation(root->left);
        return rightRotation(root);
    }
    // right left imbalance
    else if(balance_factor < -1 && key < root->right->data){
        root->right = rightRotation(root->right);
        return leftRotation(root);
    }
    else{
        return root;
    }
    
} 

void preorder(Node* root){
    if(!root)
        return;

    cout<<root->data<<" "; 
    preorder(root->left);
    preorder(root->right);
}
int main(){

    Node *root = NULL;

    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 50);
    root = insert(root, 70);
    root = insert(root, 5);
    root = insert(root, 100);
    root = insert(root, 95);


    cout<<"Preorder : "<<endl;
    preorder(root);

}   