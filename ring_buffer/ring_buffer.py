from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if storage is full, remove the head(oldest) to free up space, add item to tail(newest)
        elif self.storage.length == self.capacity:
            rmv_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            # if current is at the head, set the current to tail
            if rmv_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        start = self.current
        list_buffer_contents.append(start.value)
        # loop through nodes and append values
        # if start.next, set nextItem to start next, else set nextItem to storage head
        if start.next:
            nextItem = start.next
        else:
            nextItem = self.storage.head
        # while nextItem is not equal to start, append nextItem value to contents
        while nextItem != start:
            list_buffer_contents.append(nextItem.value)
            # if nextItem then set nextItem to nextItem next, else nextItem to storage head
            if nextItem.next:
                nextItem = nextItem.next
            else:
                nextItem = self.storage.head
        # return contents
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
