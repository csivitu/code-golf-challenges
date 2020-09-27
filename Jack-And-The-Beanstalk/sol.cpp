#include <iostream> 
#include <vector>
using namespace std; 

class BST 
{ 
	int data; 
    int level;
	BST *left, *right; 

	public: 
	BST(); 
	
	// Parameterized constructor. 
	BST(int, int); 
	
	// Insert function. 
	BST* Insert(BST *, int, int); 
	// Inorder traversal. 
	void Inorder(BST *); 
}; 

// Default Constructor definition. 
BST :: BST() : data(0), level(0), left(NULL), right(NULL){} 

// Parameterized Constructor definition. 
BST :: BST(int value, int l) 
{ 
	data = value; 
    level = l;
	left = right = NULL; 
} 

// Insert function definition. 
BST* BST :: Insert(BST *root, int value, int level=0) 
{ 
	if(!root) 
	{ 
        
		// Insert the first node, if root is NULL. 
		return new BST(value, level); 
	} 

    if(level&1){
        //odd
    if(value > root->data) 
	{ 
		// Insert right node data, if the 'value' 
		// to be inserted is greater than 'root' node data. 
		
		// Process right nodes. 
		root->left = Insert(root->left, value, ++level); 
	} 
	else
	{ 
		// Insert left node data, if the 'value' 
		// to be inserted is greater than 'root' node data. 
		
		// Process left nodes. 
		root->right = Insert(root->right, value, ++level); 
	} 


    }
    else{
        //even = NOTMAL BST


        if(value > root->data) 
        { 
            // Insert right node data, if the 'value' 
            // to be inserted is greater than 'root' node data. 
            
            // Process right nodes. 
            root->right = Insert(root->right, value, ++level); 
        } 
        else
        { 
            // Insert left node data, if the 'value' 
            // to be inserted is greater than 'root' node data. 
            
            // Process left nodes. 
            root->left = Insert(root->left, value, ++level); 
        } 

    }

	
	// Return 'root' node, after insertion. 
	return root; 
} 

// Inorder traversal function. 
// This gives data in sorted order. 
void BST :: Inorder(BST *root) 
{ 
	if(!root) 
	{ 
		return; 
	} 
	Inorder(root->left); 
	cout << root->data << " ";
    // cout << root->data << ", level: "<<root->level<<endl; 
	Inorder(root->right); 
} 

// Driver code 
int main() 
{ 
	cin.tie(0);
	cout.tie(0);
	std::ios::sync_with_stdio(false);
    int n;
	BST b, *root = NULL; 

    cin>>n;

    int first_ele;
    cin>>first_ele;

	root= b.Insert(root, first_ele); 
    
    for(int i=1;i<n;i++){
        int x;
        cin>>x;
	    b.Insert(root, x); 
        
    }
	// root = b.Insert(root, 50); 
	// b.Insert(root, 20); 
	// b.Insert(root, 40); 
	// b.Insert(root, 70); 
	// b.Insert(root, 60); 
	// b.Insert(root, 80); 

    // b.Insert(root, 90); 
    // b.Insert(root, 15); 
    // b.Insert(root, 21); 
    // b.Insert(root, 45); 

    // b.Insert(root, 55); 
    // b.Insert(root, 17); 
    // b.Insert(root, 47); 

	b.Inorder(root); 
    cout<<"\n";

    // construct a new BST and call it JTree
    // BST jt , *jtroot = NULL;



	return 0; 
} 

// This code is contributed by pkthapa 
