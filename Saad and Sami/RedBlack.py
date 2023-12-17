class Node():
    def _int_(self, value):
        self.value= value
        self.left=None
        self.right=None
        self.parent=None
        self.color=1
class RBT():
    def __int__(self):
        self.nill = Node(0)
        self.nill.color = 0
        self.nill.left = None
        self.nill.right = None
        self.Root= self.nill
        self.Root.color=0
    def Left_Rotate(self,x):
        y=x.right
        x.right=y.left
        if y.left != self.nill:
            y.left.parent =x
        y.parent=x.parent
        if x.parent == None:
            self.Root == y
        elif x==x.parent.left:
            x.parent.left=y
        else:
            x.parent.right=y
            
        y.left=x
        x.parent=y
    def Right_Rotate(self,x):
        y=x.left
        x.left=y.right
        if y.right != self.nill:
            y.right.parent =x
        y.parent=x.parent
        if x.parent == None:
            self.Root == y
        elif x==x.parent.left:
            x.parent.right=y
        else:
            x.parent.left=y
            
        y.right=x
        x.parent=y    
    def insert(self,value):
        x=self.Root
        y=self.nill
        z=Node(value)
        z.value= value
        z.left=self.nill
        z.right=self.nill
        z.color=1
        while x != self.nill :
            y=x
            if z.value<x.value:
                x=x.left
            else:
                x=x.right
        z.parent = y
        if y == self.nill:
            self.Root = z
        elif z.value<y.value:
            y.left = z
        else:
            y.right = z
        z.left = self.nill
        z.right=self.nill
        z.color = 1
        self.RBT_Insert_fix(z)
    def RBT_Insert_fix(self,z):
        while z.parent.color == 1:
            if z.parent == z.parent.parent.left:
                y=z.parent.parent.right
                if y.color == 1 :
                    z.parent.color =0
                    y.color=0
                    z.parent.parent.color=1
                    z=z.parent.parent
                else:
                    if z==z.parent.right:
                        z=z.parent
                        self.Left_Rotate(z)
                    z.parent.color = 0 
                    z.parent.parent.color = 1
                    self.Right_Rotate(z.parent.parent)
            else:
                y=z.parent.parent.left
                if y.color == 1 :
                    z.parent.color =0
                    y.color=0
                    z.parent.parent.color=1
                    z=z.parent.parent
                else:
                    if z==z.parent.left:
                        z=z.parent
                        self.Right_Rotate(z)
                    z.parent.color = 0 
                    z.parent.parent.color = 1
                    self.Left_Rotate(z.parent.parent)
        self.Root.color = 0
    def Transplant(self,u,v):
        if u.parent == self.nill:
            self.Root =v
        elif u==u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v 
        v.parent = u.parent
    def Delete(self,z):
        y=z
        y_original_color = y.color
        if z.left == self.nill :
            x=z.right
            self.Transplant(z,z.right)
        elif z.right == self.nill:
            x=z.left
            self.Transplant(z,z.left)
        else :
            y= self.Minimum(z.right)
            y_original_color = y.color
            x=y.right
            if  y != z.right:
                self.Transplant(y,y.right)
                y.right=z.right
                y.right.parent=y
            else:
                x.parent =y 
            self.Transplant(z,y)
            y.left=z.left
            y.left.parent=y
            y.color=z.color
        if y_original_color == 0:
            self.Fix_Delete(x)
    def Fix_Delete(self,x):
        while x != self.Root and x.color == 0:
            if x==x.parent.left:
                w=x.parent.right
                if w.color ==1:
                    w.color = 0
                    x.parent.color = 1
                    self.Left_Rotate(x.parent)
                    w=x.parent.right
                if w.left.color == 0 and w.right.color ==0:
                    w.color =1
                    x=x.parent
                else:
                    if w.right.color == 0:
                        w.left.color == 0
                        w.color = 1
                        self.Right_Rotate(w)
                        w=x.parent.right
                    w.color =x.parent.color
                    x.parent.color =0
                    w.right.color   =0
                    self.Left_Rotate(x.parent)
                    x=self.Root
            else :
                w=x.parent.left
                if w.color ==1:
                    w.color = 0
                    x.parent.color = 1
                    self.Right_Rotate(x.parent)
                    w=x.parent.left
                if w.left.color == 0 and w.right.color ==0:
                    w.color =1
                    x=x.parent
                else:
                    if w.left.color == 0:
                        w.right.color == 0
                        w.color = 1
                        self.Left_Rotate(w)
                        w=x.parent.left
                    w.color =x.parent.color
                    x.parent.color =0
                    w.left.color   =0
                    self.Right_Rotate(x.parent)
                    x=self.Root
        x.color = 0
    def inOrderTraversal(self,T):

        if T != self.nill:

            self.inOrderTraversal(T.left)
            print (" ",T.value," ")
            self.inOrderTraversal(T.right)

    def Minimum(self,x):
        while x.left != self.nill:
            x= x.left
        return x 
    def Maximum(self,x):
        while x.right != self.nill:
            x= x.right
        return x 
    def getTree(self):
        return self.Root
    def search(self, key):
        return self._search_recursive(self.Root, key)

    def _search_recursive(self, node, value):
        if node == self.nill or value == node.value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)