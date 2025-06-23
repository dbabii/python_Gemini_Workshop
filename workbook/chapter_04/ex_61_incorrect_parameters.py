def avg(marks):
    assert len(marks) != 0
    return round(sum(marks)/len(marks), 2)

sem1_marks = [62, 65, 75]
print("Average marks for semester 1:", avg(sem1_marks)) #67.33

ranks = []
print("Average marks for semester 1:", avg(ranks)) #Assertion error