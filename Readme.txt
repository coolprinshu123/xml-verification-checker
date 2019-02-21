The following package checks for the validity of the xml file. The xml file name is given as the command line argument. The output is a single line stating whether the file is well formed or not. The following package checks three condition in order to produce the output. How the checking is done for the conditions is clearly mentioned in the documentation file. The three conditions are as following :

1. The beginning and ending tags are correctly nested with nothing missing and nothing overlapping.
2. The elements tags does contain only characters [a-z][A-Z].
3. All the tags are contained within the root tag.
NOTE - The following package does not cosider this as correct closing : <abc/>

The following package contains : 
1. xyz.py
2. test.xml
3. Readme.txt
4. Documentation.txt

How to run the package :
$ python xyz.py test.xml

output will be a single line stating "Well formed" or "Not well formed".
 
---------------------------------------------------------------------------
Sejal Nanda
