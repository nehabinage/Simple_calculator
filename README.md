# Steps involved

1. START the program
2. DEFINE the name of the history file (e.g., "history.txt")
3. LOOP forever (while True):
    * ASK the user to enter a calculation (like 8 + 5)
    OR a command (history, clear, exit)
    * IF user enters "exit":
        > PRINT a goodbye message
        > BREAK the loop
    * IF user enters "history":
        > TRY to open the history file for reading
        > IF file exists and not empty, PRINT each line (calculation) 
        > IF file doesn't exist or is empty, PRINT "No history found" 
        > CONTINUE to the next loop
    * IF user enters "clear":
        > OPEN the history file and overwrite it with nothing (empty it). 
        > PRINT "History cleared"
        > CONTINUE to the next loop
    * OTHERWISE (assume user entered a calculation):
        > TRY to parse the input to get the numbers and the operator (You can split the input by space, e.g., "8 + 5")
        > IF input is not valid, PRINT "Invalid input" and CONTINUE
        > PERFORM the calculation using if/elif:
            >> If +, add
            >> If -, subtract
            >> If *, multiply
            >> If /, divide (and check for divide by zero)
        > SHOW the result to the user
        > WRITE the calculation and result to the history file (e.g., "8+ 5 = 13")
4. END the program