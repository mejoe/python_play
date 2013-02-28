from os import system
#system('say Hello world!')

system('say Dad, I need the following items:')
grocery_list = ['Beer', 'Wine', 'socks', 'crap more crap and crap', 'and please wash and cut your hair', 'And I emphasize, cut. your. hair!']
for item in grocery_list:
    say = 'say %s' % item
    system(say)

