#Data Types - Lists, Tuples & Dictionaries

#LISTS# - Lists of data

# list example integers
data = [10,20,30]

# list of strings
cats = ["Phil","Frank","Jess"]

# list of Mixed data types
mixed = [10,"Phil", True, 5.67]

#Change a list
#Change Jess for Ron
cats{-1] = "Ron"

#add jess back
cats.append("Jess")

#remove jess
cats.pop("Jess")


#check list for Jess

"Jess" in cats

#TUPLE# - READ ONLY LIST
# If you want to reference data that you never want to change

temps = (17.0, 23.0, 32.5)

#DICTIONARY# - Key value pairs
#Key value pairs

cat_bills = {"Phil":75, "Frank":120, "Jess":0}

#lookup Frank cat bill

cat_bills["Frank"]

#multiple vars
cat_bills = {"Phil":75,90, "Frank":120,90 "Jess":0,90}

#lookup one var
cat_bills["Phil"][0]

