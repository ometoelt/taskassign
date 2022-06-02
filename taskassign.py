import random



person = ["Name1", "Name2", "Name3", "Name4"]
cnames = [""task1", "task2", "task3", "task4", "task5", "task6", "task7", "task8", "task9"]



ideas = [i for i in range(len(cnames))]
random.shuffle(person)



for i in range(len(cnames)):
theone = i % len(person)
assign = random.choice(ideas)
ideas.remove(assign)
print (person[theone] + " assigned to " + cnames[assign])