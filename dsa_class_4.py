##> r
dsa_class_4 = print
dsa_class_4("Class_4")


def defangIPaddr(address):
    return address.replace(".", "[.]")


dsa_class_4(defangIPaddr("1.1.1.1"))
dsa_class_4(defangIPaddr("255.100.50.0"))


def finalValueAfterOperations(operations):
    X = 0
    for operation in operations:
        if operation == "X++" or operation == "++X":
            X += 1
        elif operation == "X--" or operation == "--X":
            X -= 1
    return X


X_1 = finalValueAfterOperations(["--X", "X++", "X++"])
X_2 = finalValueAfterOperations(["++X", "++X", "X++"])
X_3 = finalValueAfterOperations(["X++", "++X", "--X", "X--"])

dsa_class_4(X_1)
dsa_class_4(X_2)
dsa_class_4(X_3)


"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""


##> r
def interpret(command):
    replace_1 = command.replace("()", "o")
    replace_2 = replace_1.replace("(al)", "al")
    return replace_2;
test_1 = interpret("G()(al)");
test_2=interpret("G()()()()(al)");
test_3=interpret("(al)G(al)()()G");

dsa_class_4(test_1);
dsa_class_4(test_2);
dsa_class_4(test_3);

'''
2114. Maximum Number of Words Found in Sentences
Easy
Topics
Companies
Hint
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

 

Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
Example 2:

Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
Explanation: It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.
 

Constraints:

1 <= sentences.length <= 100
1 <= sentences[i].length <= 100
sentences[i] consists only of lowercase English letters and ' ' only.
sentences[i] does not have leading or trailing spaces.
All the words in sentences[i] are separated by a single space.
'''

##Solution
def mostWordsFound(sentences):
    maxLength=0;
    for sentence in sentences:
        split_size=sentence.split()
        LengthOfSplit=len(split_size);
        if LengthOfSplit >maxLength:
            maxLength=LengthOfSplit;
    return maxLength;

cou=mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
dsa_class_4(cou);



def FindingMostWords(Sentences):
    MaxWords = 0
    MinWords = float('inf')  # Initialize MinWords with positive infinity
    MaxSentence = ""
    MinSentence = ""
    
    for sentence in Sentences:
        Sentence_Split = sentence.split()
        Split_sentence_Length = len(Sentence_Split)
        
        if Split_sentence_Length > MaxWords:
            MaxWords = Split_sentence_Length
            MaxSentence = sentence
        if Split_sentence_Length < MinWords:
            MinWords = Split_sentence_Length
            MinSentence = sentence
    
    return MaxSentence, MinSentence

MaxSentence, MinSentence = FindingMostWords(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
print("Sentence with the maximum words:", MaxSentence)
print("Sentence with the minimum words:", MinSentence)
