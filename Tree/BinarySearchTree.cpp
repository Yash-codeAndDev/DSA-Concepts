#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    Node *right, *left;

    Node(int data){
        this->data = data;
        this->left = NULL;
        this->right= NULL;
    }
};


class BinarySearchTree{
    public:
    Node* root;

    BinarySearchTree(){
        this->root = NULL;
    }

    void insert(Node* &root, int data) {
        if (!root) {
            root = new Node(data);
            return;
        }

        if (data < root->data) {
            insert(root->left, data); // Recursively insert into left subtree
        }
        else if (data > root->data) {
            insert(root->right, data); // Recursively insert into right subtree
        }
    }

    void inorder(Node* root){
        if(!root){
            return;
        }
        inorder(root->left);
        cout<<root->data<<" ";
        inorder(root->right);
    }

    Node* deleteNode(Node* root, int target){

        // if element is not present
        if(!root){
            return NULL;
        }

        if(target < root->data ){
            root->left = deleteNode(root->left, target);
            return root;
        }
        else if(target > root->data){
            root->right = deleteNode(root->right, target);
            return root;
        }
        else{
            // root is target

            // root is leaf node
            if(!root->left && !root->right){
                delete root;
                return NULL;
            }
            // only one child exist of root
            else if(!root->right){
                Node* temp = root->left;
                delete root;
                return temp;
            }
            else if(!root->left){
                Node* temp = root->right;
                delete root;
                return temp;
            }
            //both child exist
            else{

                // find greatest element from left

                Node* child = root->left;
                Node* parent = root;

                while(child->right){
                    parent = child;
                    child = child->right;
                }

                if(root != parent){
                    parent->right = child->left;
                    child->left = root->left;
                    child->right = root->right;
                    delete root;
                    return child;
                }else{
                    child->right = root->right;
                    delete root;
                    return child;
                }

            }
        }
    }

    void visualizeTree(Node* root, Node* parent=NULL){

        if(!root){
            return ;
        }
        
        if(parent){
            cout << "Node: " << root->data << ", Parent: " << parent->data << endl;
        } else {
            cout << "Node: " << root->data << ", Parent: None (Root)" << endl;
        }

        // Recur for left and right children
        visualizeTree(root->left, root);
        visualizeTree(root->right, root);

    }

};

int main(){

    BinarySearchTree tree;

    tree.insert(tree.root, 50 );
    tree.insert(tree.root,30);
    tree.insert(tree.root,70);
    tree.insert(tree.root,20);
    tree.insert(tree.root,15);
    tree.insert(tree.root,25);
    tree.insert(tree.root,40);
    tree.insert(tree.root,60);
    tree.insert(tree.root,80);
    tree.insert(tree.root,38);
    tree.insert(tree.root,45);
    tree.insert(tree.root,65);
    tree.insert(tree.root,62);
    tree.insert(tree.root,67);
    

    cout<<"Before Deletion : "<<endl;
    tree.inorder(tree.root);
    cout<<endl;
    tree.visualizeTree(tree.root);
    
    tree.root = tree.deleteNode(tree.root, 30 );
    
    cout<<"After Deletion : "<<endl;
    tree.inorder(tree.root);
    cout<<endl;
    tree.visualizeTree(tree.root);

}