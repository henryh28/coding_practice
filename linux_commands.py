# ================ BASH RELATED =======================
# Spaces are important
# https://unix.stackexchange.com/questions/306111/what-is-the-difference-between-the-bash-operators-vs-vs-vs

# Print to screen
echo "HELLO"


# Print odd numbers from 1 to 99
for value in {1..99..2}
do
  echo $value
done


# Print argument as part of string
read name
echo "Welcome $name"


# Print result of math operations of 2 arguments
read x
read y

echo $((x+y))
echo $((x-y))
echo $((x*y))
echo $((x/y))


# Print result of comparison between 2 arguments
read x
read y

(($x > $y)) && echo "X is greater than Y"
(($x == $y)) && echo "X is equal to Y"
(($x < $y)) && echo "X is less than Y"


# Conditional check of argument
read input

[[ $input == [yY] ]] && echo "YES" || echo "NO"


# Conditional output based on uniqueness of inputs
unique=$( cat | sort -u | wc -l )

[ $unique == 1 ] && echo "EQUILATERAL"
[ $unique == 2 ] && echo "ISOSCELES"
[ $unique == 3 ] && echo "SCALENE"



# ================ TEXT PROCESSING =======================
# Spaces are important

# Print 3rd character of a line
cut -c3


# Display 2nd and 7th character of a line
cut -c2,7


# Display 2nd through 7th character of a line
cut -c2-7


# Print first 3 fields of a tab delimited file
cut -f1-3


# Print from 13th character to the end
cut -c13-


# Print the 4th word of a space delimited line
cut -d " " -f4


# Print first 3 words on a space delimited line
cut -d " " -f1-3


# Print 2nd to last fields in a tab delimited file
cut -f2-


# Print first 20 lines of a file
head -n 20


# Print first 20 characters of a file
head -c 20


# Print line 12 to 22 of a file
head -n 22 | tail -n 11


# Print last 20 lines of a file
tail -n 20


# Replace parenthesis with brackets in text input
tr "()" "[]"


# Delete all lowercase a-z from text fragment
tr -d a-z


# Sort numericall(-n) and in reverse(-r)
sort -rn


# Sort TSV (-t $'\t') text by 2nd column (-k2,2), numercially and in reverse
sort -t $'\t' -nr -k2,2


# Provide count (-c) of and remove redundant lines, ignore case (-i)
uniq -ci


# Displays only line that are not duplicate adjacent. (sort first if true unique)
uniq -u


# 2 ways to replace newlines with tabs in a CSV file
paste -sd $'\t'  #(tab is default so paste -s is same)
tr '\n' '\t'


# Fold CSV city, state pairs into 3 entries per line, separated by tab
paste - - -
paste -sd $'\t\t\n'


# Fold CSV city, state pairs into 3 entries per line, separated by semicolon
paste -d';' - - -
paste - - - | tr '\t' ';'


# ================ Arrays in Bash =======================

# Read lines of input into an array, then display them separated by a space
array=$(cat)
echo ${array[*]}


# Read lines of input into an array, then display 3rd through 7 values
countries=($(cat))
echo ${countries[*]:3:5}


# Read input into array, display length of array
array=($(cat))
echo ${#array[*]}


# ================ Grep =======================

# Search for a word, not substring
grep -w "test"

# case insensitive search
grep -i "test"

# Invert match
grep -v "test"

# Search for multiple words (not substrings)
grep -iw "the\|that\|then\|those"
