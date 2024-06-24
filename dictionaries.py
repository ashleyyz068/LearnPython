band = {
    "vocals": "plant",
    "guitar": "page"
}
#this is teh constructor function for dictionaries ; same as the output of the code above 
band2 = dict(vocals="Plant", guitar ="Page")
print(band2)
print(band["vocals"])
print(band.get("guitar"))
print("guitar" in band)
band["vocals"] = "coverdale"
band.update({"bass": "JPJ"})


#make a copy 
band3 = dict(band)

#sets 
nums = {1,2,3,4,}
nums2 = set((1,2,3,4))
#no duplicates allowed ; true is a dupe of 1 and false is a dupe of 0; a set just ignores the dupes 
# you cannot refer to an element in the set with an index position or a key 

one ={1,2,3}
two = {3,4,5}
mynewset = one.union(two)
print(mynewset)
one.intersection_update(two)
print(one)
