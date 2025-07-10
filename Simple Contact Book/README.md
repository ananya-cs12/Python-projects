#  Contact Book – Python

A beginner-friendly CLI Contact Book that allows users to manage names, phone numbers, and email addresses. Built using basic Python and file handling, with full CRUD operations and a neat tab-separated storage system.

---

## Features

-  Add contact (name, phone, and email required)
-  View all contacts in a clear, readable format
-  Search by name or phone (case-insensitive, partial match)
-  Delete contact by name or phone
-  Edit existing contact (retain existing data if left blank)
-  All data saved to `contacts.txt` in tab-separated format
-  Looping menu with clean user experience

---

## Sample Output
=====Contact Book Menu=====<br>
1. Add Contact<br>
2. View All Contacts<br>
3. Search Contact<br>
4. Delete Contact<br>
5. Edit Contact<br>
6. Exit<br>
Enter your choice (1-6):2<br>
------ All Contacts ------<br>
Name: Ananya Singh, Phone: 9876543210, Email: ananya@email.com<br>
Name: Ravi Verma, Phone: 9123456789, Email: ravi@email.com<br>

=====Contact Book Menu=====<br>
1. Add Contact<br>
2. View All Contacts<br>
3. Search Contact<br>
4. Delete Contact<br>
5. Edit Contact<br>
6. Exit<br>
Enter your choice (1-6):5<br>
Enter name or phone to edit: Anita<br>
Found contact to edit:<br>
Current — Name: Anita, Phone: 1234567890, Email: anshu@gmail.com<br>
Enter new name (or press Enter to keep current):<br>
Enter new phone (or press Enter to keep current): 1242483513<br>
Enter new email (or press Enter to keep current):<br> 
Contact updated successfully.<br>

=====Contact Book Menu=====<br>
1. Add Contact<br>
2. View All Contacts<br>
3. Search Contact<br>
4. Delete Contact<br>
5. Edit Contact<br>
6. Exit<br>
Enter your choice (1-6): 6<br>
Exited Contact Book.<br>

