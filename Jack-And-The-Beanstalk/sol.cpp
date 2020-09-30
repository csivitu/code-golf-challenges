// C++ program to print BST in given range 
#include<bits/stdc++.h> 
using namespace std; 

/* A Binary Tree node */
class TNode 
{ 
	public: 
	int data; 
  	int level;
	TNode* left; 
	TNode* right; 
}; 

TNode* newNode(int data, int level); 

/* A function that constructs Balanced 
Binary Search Tree from a sorted array */
TNode* sortedArrayToBST(int arr[], 
						int start, int end, int level=0) 
{ 
	/* Base Case */
	if (start > end) 
	return NULL; 

	/* Get the middle element and make it root */
	int mid = (start + end)/2; 
	TNode *root = newNode(arr[mid],level); 
	
  	if(level&1){
     	/* Recursively construct the left subtree 
		and make it left child of root */
		root->right = sortedArrayToBST(arr, start, mid - 1,++level); 

		/* Recursively construct the right subtree 
		and make it right child of root */
		root->left = sortedArrayToBST(arr, mid + 1, end,level); 
    }
  	else{
      	/* Recursively construct the left subtree 
		and make it left child of root */
		root->left = sortedArrayToBST(arr, start, mid - 1,++level); 
	
		/* Recursively construct the right subtree 
		and make it right child of root */
		root->right = sortedArrayToBST(arr, mid + 1, end,level); 
    }

	return root; 
} 

/* Helper function that allocates a new node 
with the given data and NULL left and right 
pointers. */
TNode* newNode(int data, int level) 
{ 
	TNode* node = new TNode(); 
  	node->level = level;
	node->data = data; 
	node->left = NULL; 
	node->right = NULL; 

	return node; 
} 

void Inorder(TNode* node) 
{ 
    if (node == NULL)  
        return;  
	Inorder(node->left); 
	cout << node->data << " ";
	Inorder(node->right); 
} 


// Driver Code 
int main() 
{ 
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

	TNode *root = sortedArrayToBST(arr, 0, n-1,0); 
	Inorder(root); 

	return 0; 
} 

// This code is contributed by rathbhupendra
