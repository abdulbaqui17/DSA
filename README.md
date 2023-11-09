Single Linked List Implementation
Overview
This repository contains a Python implementation of a Single Linked List (SLL). The sll class provides a simple and efficient way to work with linked lists, allowing you to perform various operations such as insertion, deletion, and display.

Features
Insertion Operations:

insert_first(data): Insert a node with the given data at the beginning of the list.
insert_last(data): Insert a node with the given data at the end of the list.
insert_value(target, data): Insert a node with the given data after the node with the target value.
Deletion Operations:

delete_first(): Delete the first node in the list.
delete_last(): Delete the last node in the list.
delete_value(data): Delete the node with the specified data.
Display:

display(): Display the elements of the linked list.
Iteration:

The linked list is iterable, allowing you to iterate over its elements using a loop.
Usage
Clone the repository to your local machine.

bash
Copy code
git clone https://github.com/yourusername/single-linked-list.git
Navigate to the project directory.

bash
Copy code
cd single-linked-list
Use the sll class in your Python code.

python
Copy code
from sll import sll

# Create a new linked list
l = sll()

# Insert nodes
l.insert_first(50)
l.insert_last(60)
l.insert_value(50, 55)
l.insert_value(60, 65)
l.insert_value(55, 56)

# Perform other operations (uncomment as needed)
# l.delete_first()
# l.delete_value(65)

# Display the linked list
l.display()

# Iterate over the linked list
for item in l:
    print(item, end=" ")
Contribution
Contributions are welcome! If you have ideas for improvements or new features, please create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Happy coding with your Single Linked List! 🚀
