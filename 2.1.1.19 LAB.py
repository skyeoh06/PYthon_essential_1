# Objectives
# experimenting with existing Python code;
# discovering and fixing basic syntax errors;
# becoming familiar with the print() function and its formatting capabilities.
# Scenario
# We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition - learn from your mistakes and draw your own conclusions.

# Try to:

# minimize the number of print() function invocations by inserting the \n sequence into the strings
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# make the arrow twice as large (but keep the proportions)
print("     *")
print("    * *")
print("   *   *")
print("  *     *")
print(" *       *")
print("***     ***")
print("  *     *")
print("  *     *")
print("  *******")

# duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
print(("    *       ")*2)
print(("   * *      ")*2)
print(("  *   *     ")*2)
print((" *     *    ")*2)
print(("***   ***   ")*2)
print(("  *   *     ")*2)
print(("  *   *     ")*2)
print(("  *****     ")*2)

# remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
print("    *)
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
>> 
 print("    *)
                ^
SyntaxError: EOL while scanning string literal

# do the same with some of the parentheses;
print("    *"
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

>> 
print("   * *")
        ^
SyntaxError: invalid syntax     

# change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
Print("  *****")

>>
Print("  *****")
NameError: name 'Print' is not defined

# replace some of the quotes with apostrophes; watch what happens carefully.
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  ,,,**")

>> 
    *
   * *
  *   *
 *     *
***   ***
  *   *
  *   *
  ,,,**
