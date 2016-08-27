# import special libraries already already built in python
import random, urllib2


# list of options to select from
the_url = 'https://raw.githubusercontent.com/kamieb03/awesome/master/activities.lst'
list_raw_text = urllib2.urlopen(the_url).read()
possible_activities = ['a','b','c']


# choice of what we are going to do 
print "DEBUG" + str(list_raw_text.split())
the_activity =  random.choice(possible_activities)


# displays the results to the end user
print "Possible actiities are: " + str(possible_activities)
print "What are we going to do: " + the_activity
