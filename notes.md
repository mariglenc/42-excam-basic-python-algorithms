issues:
ex1-3
    for i in range(len(text)) -> forgot about this kind of iteration
    also forgot about -1 in iteration
    isdigit function -> forgot at all how to check if a char is nr
    forgot to convert string to int int(text[i])

ex2-1
    today i frogot string.alnum()

ex2-2
    today i frogot what is list[::-1]

ex2-4
    what is sorted function

ex3-2
    frogot about replace function


new concpets
    function sorted()   -> sorted([1, 3, 5, 2, 4, 3]):   returns -> [1, 2, 3, 3, 4, 5]
    function max()      -> max(10, 2, 8):                returns -> 10
    list concatination  -> [1, 3, 5] + [2, 4, 3]:        returns -> [1, 2, 3, 3, 4, 5]
    variable scope
        if, else, for, while, try does not have scope
        Functions, Classes, Modules have scope
    how does sorted work with key param in case we put there soem tuples iwth 3 params 
        Compare param 0 (length).
        ├─ different? → decided, STOP.
        └─ tied?      → compare param 1 (word).
                            ├─ different? → decided, STOP.
                            └─ tied?      → compare param 2 (vowels).
                                            └─ smallest wins.

