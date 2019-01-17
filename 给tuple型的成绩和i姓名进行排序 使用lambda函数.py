ls_t = [("Boy",95), ("Fire",86), ("Allbout",92), ("Distmem", 80)]

new_name = sorted(ls_t, key= lambda x: x[0])
print(new_name)

new_score = sorted(ls_t, key= lambda x: x[1], reverse=True)
print(list(new_score))

new_name_a = sorted(ls_t, key= lambda x: x[0] ,reverse=True)
print(new_name_a)

new_score_a = sorted(ls_t, key= lambda x: x[1])
print(new_score_a)