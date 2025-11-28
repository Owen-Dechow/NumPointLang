# NumPointLang

Read about it here: https://medium.com/@owen.dechow/emergence-and-esoteric-languages-2b356b8e5044

A small esoteric programming language implimented in python and based on [TermsLang](https://github.com/Owen-Dechow/TermsLang), BrainF*, and X86 Assembly.

## Running
```
python3 main.py [FILENAME]
```

## Example
```
(0)     jmp 0       [Always put ptr at 0]
        set 72      [h]
        fwd
        set 101     [e]
        fwd
        set 108     [l]
        fwd
        set 108     [l]
        fwd
        set 111     [o]
        fwd
        set 32      [ ]
        fwd
        set 87      [w]
        fwd
        set 111     [o]
        fwd
        set 114     [2]
        fwd
        set 108     [l]
        fwd
        set 100     [d]
        jmp 0       [put ptr at 0]
        pnt         [print Hello World]
        jmp 15      [put ptr at 15]
        inc         [increment 15 by 1]
        ieq 3       [if ptr=15 is 3]
        gto 1       [if true go to marker 1]
        gto 0       [if false go to marker 0]
(1)     ext         [exit program]
```
Output:
```
Hello World
Hello World
Hello World
```

## Commands

### fwd
Moves the pointer forward one place. Will wrap if at the end of the data array.

### bwd
Moves the pointer backward one place. Will wrap to end of array if at index 0.

### flp
Sets the value at pointer to 0 if not 0 and 1 if 0.

### inc
Increments the value at pointer by 1.

### dec
Decrements the value at pointer by 1.

### gto [int]
Jumps in the command list to the given marker.

### set [int]
Set the value at pointer to the given input.

### jmp [int]
Moves the pointer to the given index. Will wrap if greater then length of data array.

### ieq [int]
Checks if the value at pointer is equal to given input. If true the following command will run else the following command will skip.

### inz
Checks if the value at pointer is not 0. If true the following command will run else the following command will skip.

### ext
Exits the program.

### pnt
Prints the data in the array. Will splice from location of pointer to first instance of 0 in the array.

## Data
Data array length = 30,000

Data array = [0, 0, ... 0]

Prints as UTF-8
