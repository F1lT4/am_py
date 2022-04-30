class Node:

    def __init__(self, data, left=None, right=None):

        self.data = data

        self.left = left

        self.right = right

    def __str__(self):

        if not self.left:

            st_1 = "_"

        else:

            st_1 = self.left

        if not self.right:

            st_2 = "_"

        else:

            st_2 = self.right

        return f"[{self.data}({st_1} , {st_2})]"


class Tree:

    def __init__(self):

        self.root = None

    def insert_root(self, data):

        if self.root:

            return "the tree already hawa root"

        else:

            self.root = Node(data)

    def the_search(self, node, pos):

        lefty = pos.left

        if lefty is None:

            pass

        elif lefty.data == node:

            return lefty

        else:

            self.the_search(node, lefty)



        righty = pos.right

        if righty is None:

            return None

        elif righty.data == node:

            return righty

        else:

            self.the_search(node, righty)

    def insert_left(self, data, node):

        if not self.root:

            self.insert_root(data)

        else:

            cur_index = self.root

            if self.root.data == node:

                if self.root.left:

                    print("The space is already occupied")

                    return

                else:

                    self.root.left = Node(data)

            else:

                the_node = self.the_search(node, cur_index)

                if the_node is None:

                    print("not a node found")

                    return

                else:

                    if the_node.left is None:

                        the_node.left = Node(data)

                    else:

                        print("the space is occupied")

    def insert_right(self, data, node):

        if not self.root:

            self.insert_root(data)

        else:

            cur_index = self.root

            if self.root.data == node:

                if self.root.right:

                    print("the space is occupied")

                    return

                else:

                    self.root.right = Node(data)

            else:

                the_node = self.the_search(node, cur_index)

                if the_node is None:

                    print("not a node found")

                    return

                else:

                    if the_node.right is None:

                        the_node.right = Node(data)

                    else:

                        print("the space is occupied")

    def __str__(self):
        return f"{self.root}"

