from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if capacity has been reached
        if self.storage.length == self.capacity:
            # if the current one exists && it's previous node is not the head
            if self.current and self.current is not self.storage.head:
                # replace value of previous node
                self.current.prev.value = item
                # update where the current node is
                self.current = self.current.prev
            else:
                # remove from tail and set current position
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.tail
        else:
            self.storage.add_to_head(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # starting at tail
        current_node = self.storage.tail

        # iterate through DLL
        for node in range(self.storage.length):
            # add current value and go to previous node
            list_buffer_contents.append(current_node.value)
            if current_node.prev:
                current_node = current_node.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
