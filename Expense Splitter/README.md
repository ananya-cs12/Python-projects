# Expense Splitter – Python CLI App  
A simple and practical command-line tool that helps you split expenses fairly among friends or groups. You enter the total amount, the names of people, and who paid — the app calculates how much everyone owes or gets back. It also allows you to view all past splits saved with timestamps.

---

## Features
-  Split bills between 2 or more people
-  Automatically calculates how much each person owes
-  Saves each session with payer name, total amount, per person share, and timestamp
-  Stores all data in a simple `expenses.txt` file
-  Option to view all past expense splits
-  Smart validations and clear prompts

---

## Sample text file(expenses.txt)


--- Expense Split Summary ---<br>
Date: 09-07-2025 19:48<br>
Payer: Lia, Total: ₹2500.0, Each: ₹833.33<br>
Lia gets ₹1666.67<br>
Lucy owes ₹833.33<br>
Ryan owes ₹833.33<br>
-----------------------------<br>

--- Expense Split Summary --<br>-
Date: 09-07-2025 19:49<br>
Payer: Charles, Total: ₹4500.0, Each: ₹1125.0<br>
Charles gets ₹3375.0<br>
Smith owes ₹1125.0<br>
Richard owes ₹1125.0<br>
Susan owes ₹1125.0<br>
----------------------------<br>-


## Sample Output<br>
********** Welcome to the Expense Splitter! **********<br>

Main Menu:<br>
1. Split a new expense<br>
2. View past splits<br>
3. Exit<br>
Enter your choice (1-3): 1<br>
How many people are there? 4<br>
Enter names one by one:<br>
> Smith<br>
> Charles<br>
> Richard<br>
> Susan<br>
Who paid the bill? Charles<br>
Total amount? ₹4500<br>

Each person should pay: ₹1125.0<br>

----- Final Balances -----<br>
Charles gets ₹3375.0<br>
Smith owes ₹1125.0<br>
Richard owes ₹1125.0<br>
Susan owes ₹1125.0<br>

Save this split to file? (Y/N): Y<br>
Saved!<br>

Main Menu:<br>
1. Split a new expense<br>
2. View past splits<br>
3. Exit<br>
Enter your choice (1-3): 2<br>

----- Past Expense Splits -----<br>


--- Expense Split Summary ---<br>
Date: 09-07-2025 19:48<br>
Payer: Lia, Total: ₹2500.0, Each: ₹833.33<br>
Lia gets ₹1666.67<br>
Lucy owes ₹833.33<br>
Ryan owes ₹833.33<br>
-----------------------------<br>

--- Expense Split Summary ---<br>
Date: 09-07-2025 19:49<br>
Payer: Charles, Total: ₹4500.0, Each: ₹1125.0<br>
Charles gets ₹3375.0<br>
Smith owes ₹1125.0<br>
Richard owes ₹1125.0<br>
Susan owes ₹1125.0<br>
-----------------------------<br>


-------------------------------<br>

Press Enter to return to the menu...<br>

Main Menu:<br>
1. Split a new expense<br>
2. View past splits<br>
3. Exit<br>
Enter your choice (1-3): 3<br>
Exited

