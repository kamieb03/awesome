# import special libraries already already built in python
import random
# list of options to select from
possible_activities = ['a','b','c']
# choice of what we are going to do 
the_activity =  random.choice(possible_activities)
# displays the results to the end user
print "Possible actiities are: " + str(possible_activities)
print "What are we going to do: " + the_activity
