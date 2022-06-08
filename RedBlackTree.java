class Node {
    int data;
    Node parent;
    Node left;
    Node right;
    int colour;
}

public class RedBlackTree{
    private Node root;
    private Node TNULL;

    public RedBlackTree() {
		TNULL = new Node();
		TNULL.colour = 0;
		TNULL.left = null;
		TNULL.right = null;
		root = TNULL;
	}

    public void leftRotate(Node x){
        Node y = x.right;
        x.right = y.left;
        if (y.left != TNULL){
            y.left.parent = x;
        }
        y.parent = x.parent;
        if(x.parent == null){
            this.root = y;
        } else if(x == x.parent.left){
            x.parent.left = y;
        } else if (x == x.parent.right){
            x.parent.right = y;
        }
        x.parent = y;
        y.left = x;
    }

    public void rightRotate(Node x){
        Node y = x.left;
        x.left = y.right;
        if(y.right != TNULL){
            y.right.parent = x;
        }
        
        y.parent = x.parent;
        if(x.parent == null){
            this.root = y;
        } else if(x == x.parent.left){
            x.parent.left = y;
        } else if(x == x.parent.right){
            x.parent.right = y;
        }
        x.parent = y;
        y.right = x;
    }

    public void insert(int key){
        Node node = new Node();
        node.parent = null;
        node.data = key;
        node.left = TNULL;
        node.right = TNULL;
        node.colour = 1;  //new node red

        Node y = null;
        Node x = this.root;

        while(x != TNULL){
            y = x;
            if( node.data < x.data){
                x = x.left;
            }else{
                x = x.right;
            }
        }

        node.parent = y;
        if( y == null){
            this.root = node;
        } else if(y.data < node.data){
            y.right = node;
        } else{
            y.left = node;
        }

        if (node.parent == null){
            node.colour = 0;
            return;
        }

        if(node.parent.parent == null){
            return;
        }

        fixInsert(node);
    }

    public void fixInsert(Node x){
        Node u;
        while(x.parent.colour == 1){
            if(x.parent == x.parent.parent.left){
                u = x.parent.parent.right;
                if (u.colour == 1){
                    x.parent.colour = 0;
                    u.colour = 0;
                    x.parent.parent.colour = 1;
                    x = x.parent.parent;
                }else {
                    if(x == x.parent.right){
                        x = x.parent;
                        leftRotate(x);
                    }
                    x.parent.colour = 0;
                    x.parent.parent.colour = 1;
                    rightRotate(x.parent.parent);
                }
            }else{
                u = x.parent.parent.left;
                if (u.colour == 1){
                    x.parent.colour = 0;
                    u.colour = 0;
                    x.parent.parent.colour = 1;
                    x = x.parent.parent;
                }else {
                    if(x == x.parent.left){
                        x = x.parent;
                        rightRotate(x);
                    }
                    x.parent.colour = 0;
                    x.parent.parent.colour = 1;
                    leftRotate(x.parent.parent);
                }
            }
            if(x == this.root){
                break;
            }
        }
        root.colour = 0;
    }

    private void printHelper(Node root, String indent, boolean last) {
		// print the tree structure on the screen
	   	if (root != TNULL) {
		   System.out.print(indent);
		   if (last) {
		      System.out.print("R----");
		      indent += "     ";
		   } else {
		      System.out.print("L----");
		      indent += "|    ";
		   }
            
           String sColor = root.colour == 1?"RED":"BLACK";
		   System.out.println(root.data + "(" + sColor + ")");
		   printHelper(root.left, indent, false);
		   printHelper(root.right, indent, true);
		}
	}

    public void prettyPrint(){
        printHelper(this.root, "", true);
    }


    public static void main(String[] args) {
        RedBlackTree bst = new RedBlackTree();
        bst.insert(8);
    	bst.insert(18);
    	bst.insert(5);
    	bst.insert(15);
    	bst.insert(17);
    	bst.insert(25);
    	bst.insert(40);
    	bst.insert(80);
    	bst.prettyPrint();
    }
}