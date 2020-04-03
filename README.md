# hack-corona
Team Our Team Hack for #HackCorona

# Our goal (in draft)

Focused on projecting future results of COVID19.

* When  will be the peak of infections be reached based on different actions taken.
* What is the efficiency of each action?
	- And based on this, find out the best/worst cases
* What are other important factors (like population density, .....) effect this

------
The first iteration of the project showed signs of success within a limited time.

Some of the areas that still need attention include:

* A sustainable infrastructure to run the project long term (Deutsche Telekom's DIH could be a solution)
* Improve UI for representing the information
* More solid data from different nations and regions (finding anything truly suitable during the hackathon was a challenge)
* Improved modeling

# Our project (in video format)

[![Watch the video](video/our_team.gif)](https://drive.google.com/file/d/1k5YdFmZ9xP1IIYsrWu7-2GtWLWFYzMKG/view?usp=sharing)

## More details on modeling improvements:

SEIR models have different versions that generally simulate the infectious diseases in closed or open communities. Revising some of the existing models, it is clear that they were built with presumptions that are no longer valid.
The fact that a considerable percentage of COVID19 patients require intensive care units, or ventilators is not much of interest for most existing models. Which means, these models will continue to apply same recovery/death percentages before and after the medical system capacity in a country is reached; which is both wrong and misleading.

Another dimension that COVID19 is imposing is the nature of symptoms severity in relation to specific patients’ criteria (like patient age, already existing medical conditions, transplants, and immunity problems) It might seem of marginal importance in a normal epidemic, but in this case where we have no medication, no vaccine, and are planning to lock cities until we do; this is very important to make better decisions based on better simulation. This is because, may be with a more accurate simulation, the decision makers might have a different idea about the lock-down; age related, city related, jagged lockdown, etc. So, in general a more accurate model would consider the community as layers with different reactions to the virus. This is how countries with different demographic attributes will be able to customize community-tailored policies.

One important point in the COVID19 case is the importance of medical supplies, medical staff, and quality of the health care system. This sounds simple, but actually the problem is COVID19 causes the medical system to crash. This means, if some of the medical components is consumed faster than others, without an innovative way to replace it, the system may even crash while we still have some resources. This highlights the importance of PPE for medical staff just as one example, because the infection of doctors will both increase the total number of infected people, and will later reduce the number of doctors who can use other medical supplies to treat patients.

Because we are still learning more about COVID19, we need models that can dynamically adapt to new factors; one example in a few researches which suggest that 14% of the recovered patients might re-catch the virus in few weeks. Because we cannot be sure now what the reason behind these observations, which might be a different nature of COVID19 than its SARS family (which immunity after first infection is around 18 months), or maybe we have the wrong recovery criteria.

These were some examples of the new factors imposed by COVID19; which requires new SEIR versions.


### Meeting notes collected in:

[meeting-notes](meeting-notes) from first hackathon discussions.
