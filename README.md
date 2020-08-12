# monty_hall_problem
simulating many plays of monty hall problem


The Monty Hall problem goes as follows:

In a game show there are 3 doors: A, B & C. Behind one door there is a prize (e.g. a car), behind the other two there is nothing.
The game show host asks you to first pick a door e.g. A. Then they proceed to open a different door (e.g. B) and show you it is empty.

Now the host asks you if you want to stick to your choice of door, or swap to the other available door (door C).

This may initially seem like a simple problem: "There are two doors and therefore there is a 50% of winning the prize no matter which door is picked. 
Therefore I can stick with my choice."

In fact this is not the case.

Lets start with all doors being closed. We know that there is a 1/3 chance that the car is behind one of the doors.
If you pick door A, then the chance of the car being behind it is 1/3. Therefore the chance the car is behind doors B and C must then be 2/3.
When door B is revealed to have nothing in it. Then the 1/3 chance it originally had drops to 0 and must therefore be transfered on to door C. 
Therefore, by swapping from your original choice A to door C, you stand a greater chance of winning the car.

This python code shows that over a large ammount of runs the running success rates for switching doors will tend to 2/3. 
Sticking with your original choice will tend to 1/3.
