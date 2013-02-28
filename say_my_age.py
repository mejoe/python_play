from os import system
#system('say Hello world!')

family = {'Dad': 35, 'Mom': 32, 'Ceci': 12, 'Ana Camila': '2 months', 'Woodstock': 3, 'Charlie': 1.5}
number_family_members = len(family)

say = "There are %i family members." % number_family_members
print say
system("say " + say)

for name, age in family.iteritems():
    if isinstance(age, basestring):
        say = "%s is %s old." % (name, age)
    else:
        say = "%s is %s years old." % (name, age)
    print say
    system("say " + say)

