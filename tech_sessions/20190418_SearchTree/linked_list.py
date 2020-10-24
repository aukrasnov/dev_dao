#
# class LinkedList:
#
#     def __init__(self, current):
#         self.current = current
#         print(self.current)
#
#     def add(self, current):
#
#         'LinkedList_2'.format(current) = current
#
#     #
#     # def delete:
#     #
#     #
#     # def find:
#
#
#
# LinkedList(1)
# LinkedList(2)
# LinkedList(3)
#
#
#
# LinkedList_2 = {'current':2, 'next':3}
# LinkedList_3 = {'current':3, 'next':4}
#


class Node:

    link = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return 'key:{0} value:{1}'.format(self.key, self.value)


node1 = Node(1, 1)
node2 = Node(2, 2)
node3 = Node(3, 3)
node4 = Node(4, 4)
node5 = Node(5, 5)
# print(node1.value)


class LinkedList:

    first_node = None
    last_node = None

    def add(self, node):

        if self.last_node:
            self.last_node.link = node

        self.last_node = node

        if not self.first_node:
            self.first_node = node

    def find(self, node_key_to_find):

        if not self.first_node:
            print('No nodes')
            return None

        current_node = self.first_node

        # проверяю, что нода в списке

        while current_node:
            if current_node.key == node_key_to_find:
                return current_node
            current_node = current_node.link

    def travers(self):

        if self.first_node:
            link = self.first_node

            while link:
                node = link
                link = node.link
                print(node, node.link)
        else:
            print('No nodes')
            return

    def delete(self, node_to_delete):

        # проверяю, что список не пустой
        if not self.first_node:
            print('No nodes')
            return

        current_node = self.first_node
        prev_node = None

        # проверяю, что нода в списке
        while current_node != node_to_delete:
            prev_node = current_node
            current_node = current_node.link

        prev_node.link = node_to_delete.link

    def update(self, node_to_update, new_value):

        # проверяю, что список не пустой
        if not self.first_node:
            print('No nodes')
            return

        L_List.find(node_key_to_find=node_to_update).value = new_value


L_List = LinkedList()
L_List.add(node=node1)
L_List.add(node=node2)
L_List.add(node=node3)
L_List.add(node=node4)
L_List.add(node=node5)

# print(L_List.first_node.link)
# print(L_List.last_node)
#
# L_List.travers()
#
# L_List.travers()
# print('\n DELETE!!!!! \n')
#
# L_List.delete(node_to_delete=node3)
# L_List.travers()


print(L_List.find(1))
L_List.update(1, 15)
print(L_List.find(1))

# node2.link.value = 15

# print(node3)


