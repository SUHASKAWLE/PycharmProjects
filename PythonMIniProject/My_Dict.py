
#my dictionary for software information

My_Dict={"python":"programming language","mysql":"relational database management system","tablue":"visualization tool", "beautifulsuop":"web scrapper"}
print("Enter the software name")
soft_ware=(input())
soft_ware=soft_ware.lower()
if soft_ware in My_Dict:
    print(My_Dict[soft_ware])
else:
    print('Information not found')
