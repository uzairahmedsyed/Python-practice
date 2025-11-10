
# ### 03/11/25

# ## TASK (task1, task2, task3)

# ##Step 1: Data Preparation Aur Cleaning =====================================================================================
#     ## --Aapke paas yeh raw data ek Tuple ki shakal mein hai, jismein har item ID, Name, aur Sale Amount hai. Magar ismein thodi gadbadi (inconsistencies) hai.
#     ## 1.1 : Cleaning (String Method .replace()): item_to_clean ID102_FARAH_45000 se _ ko - se replace karen.
#     ## 1.2 : Conversion (String Method .split()): replace karne ke baad, is string ko - ki buniyad par split kar ke ek temporary List mein save karen. 
# ###=======================================================================================================================
# raw_data_tuple = (
#     "ID101-ALI-50000",
#     "ID102_FARAH_45000", # Yahan '-' ki jagah '_' hai
#     "ID103-UZR-120,000"  # Yahan comma (,) hai
# )

# ## puray tuple ko list mein convert kra
# list_raw_data_tuple = list(raw_data_tuple)
# ## list ki index(1) ki value to variable mein save krwaya
# string_list_raw_data_tuple = list_raw_data_tuple[1]
# # print(type(string_list_raw_data_tuple))
# print("value of string_list_raw_data_tuple: ",string_list_raw_data_tuple)

# ##  "_" ko replace krwa k "-" se ek new variable mein save krwaya   
# replace_string_list_raw_data_tuple = string_list_raw_data_tuple.replace("_", "-", -1)
# ## print karwaya variable
# print("value of replace_string_list_raw_data_tuple: ",replace_string_list_raw_data_tuple)
# ## variable ki value dobara list ki index[1] per assign krdi
# list_raw_data_tuple[1] = replace_string_list_raw_data_tuple
# ## list print krwai
# print(list_raw_data_tuple)
# ## replacing k baad  (replace_string_list_raw_data_tuple) isko .split() zariya list mein convert kra... [ .split() method jo hai wo datatype string ka method hai , jo k string ko split kar k list mein convert kr deta hai]
# temp_list_raw_data_tuple = replace_string_list_raw_data_tuple.split("-")
# # print(type(temp_list_raw_data_tuple))
# print("value of temp_list_raw_data_tuple: ", temp_list_raw_data_tuple)


# ### Step 2: String Length Check Aur Validation  =====================================================================================
#     ## 2.1: Tricky len(): tricky_item ki total length nikalen (len(tricky_item)) aur print karen.
#     ## 2.2: Validation (If-Else):
#     ## 2.2.1: if tricky_item mein comma (,) maujood ho (in operator se check karen):
#     ## 2.2.1.a : Us comma ko .replace() kar ke hatayen (string ko clean karen)
#     ## 2.2.1.b : clean hone ke baad, string ki nai length nikalen aur print karen.
#     ## 2.2.2 : else: Print karen: "Data is already clean."
# ### ========================================================================================================================================


# ## list ki index[2] ki value ko variable mein save krwai
# third_index_list_raw_data_tuple = list_raw_data_tuple[2]
# ## lenght check krne ka phela tareeqa
# # lenght_check_third_index_list_raw_data_tuple = len(third_index_list_raw_data_tuple)
# ## length check krne ka dosra tareeqa
# print(len(third_index_list_raw_data_tuple))

# ## variable create kara tak k usko IF condition mein use krskun
# comma = ","
# ## variable to dosray variable k check krwaya 
# if (comma in third_index_list_raw_data_tuple):
#         ## remove krwaya "," ko string mein se [120,000]  
#         remove_comma = third_index_list_raw_data_tuple.replace(",", "")
#         ## lenght print karwai after removing the ","
#         print(len(remove_comma))
#         print(remove_comma)
# else:
#         print("Data is already clean.")


# #### Step 3: Final Output Aur Summarization ========================================================================================================================================
#     ## 3.1 : Tuple to List: Puri raw_data_tuple ko ek final_list mein convert karen.
#     ## 3.2 : List Length: final_list ki length nikalen (total records).
#     ## 3.3 : List to Tuple: final_list ko wapis Tuple mein convert karen (final_tuple) aur use print karen.
# ### ========================================================================================================================================


# ## comma remove krwanay k baad wapis list k index[2] ko assign krdi
# list_raw_data_tuple[2] = remove_comma
# ## lenght print krwai
# print(len(list_raw_data_tuple))
# ## type print krwai
# # print(type(list_raw_data_tuple))


# ## list ko tuple mein convert kar k new variable mein save krwai
# final_tuple = tuple(list_raw_data_tuple)
# ## lenght print krwai
# print(len(final_tuple))
# ## type print krwai
# # print(type(final_tuple))
# ## final Tuple print krwai
# print(final_tuple)


#####============================================================================##############





numbers = [2,1,3,4,5,1]

print(f"original list: {numbers}")

numbers.sort()
print(f"sorted list: {numbers}")

numbers.reverse()
print(f"reversed list: {numbers}")

x = numbers.count(1)
print(f"count the occurance(kitni bar aya) of 1 is the list: {x}")

numbers.remove(1)
print(f"remove 1 first occurance form the list: {numbers} ")

numbers.insert(6, 7)
print(f"insert 7 : {numbers}")

y = numbers.count(1)
print(f"count the occurance(kitni bar aya) of 1 is the list: {y}")

z =numbers.copy()
print(type(numbers))




# numbers = ["b","A","c","d"]

# print(f"original list: {numbers}")

# numbers.sort()
# print(f"sorted list: {numbers}")

# numbers.reverse()
# print(f"reversed list: {numbers}")

# numbers.remove("A")
# print(f"remove 1 first occurance form the list: {numbers} ")

# numbers.insert(4,"e")
# print(f"insert 7 : {numbers}")