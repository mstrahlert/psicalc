# psicalc

Python program to calculate what pressure to use in bike tires

## formula

This implements the 15% tire drop formula according to https://www.renehersecycles.com/wp-content/uploads/2015/03/BQTireDrop.pdf

It assumes 50% load on each wheel. Generally you want a bit more load on the back wheel and bit less on the front wheel. There's an option for that, --weight that sets the weight of the backwheel in percent. Setting --weight to 60 makes the load 60/40. The default is 50/50.

In my opinion the result of this formula is on the low ballpark. To that end I've added a method to set a ratio. My preferred ratio is 1.3 - 1.4 (ie 30%-40% higher than the prescribed value)
