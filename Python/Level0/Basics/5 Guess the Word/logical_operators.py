
go_out = False

# 'and' operator
I_have_finished_howework = False
friend_has_finished_howework = True

go_out = I_have_finished_howework and friend_has_finished_howework
print(go_out)
if go_out:
    print("We can go out :)")
else:
    print("We have to stay home :(")

# 'or' operator
weekend = True
holiday = True

go_out = weekend or holiday
print(go_out)
if go_out:
    print("We can go out :)")
else:
    print("We have to stay home :(")

# 'not' operator
raining = True

go_out = not raining
print(go_out)
if go_out:
    print("We can go out :)")
else:
    print("We have to stay home :(")
