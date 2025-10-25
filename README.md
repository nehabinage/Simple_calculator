# Steps involved

1. START the program
2. DEFINE the name of the history file (e.g., "history.txt")
3. LOOP forever (while True):
    a. ASK the user to enter a calculation (like 8 + 5)
    OR a command (history, clear, exit)
    b. IF user enters "exit":
        i. PRINT a goodbye message
        ii. BREAK the loop
    c. IF user enters "history":
        i. TRY to open the history file for reading
        ii. IF file exists and not empty, PRINT each line (calculation) 
        iii. IF file doesn't exist or is empty, PRINT "No history found" 
        iv. CONTINUE to the next loop
    d. IF user enters "clear":
        i.OPEN the history file and overwrite it with nothing (empty it). 
        ii. PRINT "History cleared"
        iii. CONTINUE to the next loop
    e. OTHERWISE (assume user entered a calculation):
        i. TRY to parse the input to get the numbers and the operator (You can split the input by space, e.g., "8 + 5")
        ii. IF input is not valid, PRINT "Invalid input" and CONTINUE
        iii. PERFORM the calculation using if/elif:
            - If +, add
            - If -, subtract
            - If *, multiply
            - If /, divide (and check for divide by zero)
        iv. SHOW the result to the user
        V. WRITE the calculation and result to the history file (e.g., "8+ 5 = 13")
4. END the program