# Homework # 1

The Text of the e-mail that I sent to Allison: 

Dear Allison,

It's time for homework: You will find my thoughts about Pro Publica's "Machine Bias" project below. 

Best wishes, Mathias

P.s.: I just built an own database and tried to import existing data (CSV) with the COPY command. Unfortunately, I didn't get the job done: I struggled with the right command and probably the user rights (postgres is running under the user postgres, but this user doesn't have access to the main $USER space where the CSV is lying). Could you maybe give us in one of your next classes a short insight how we could import existing tabular data? 


---

"Machine Bias" by Julia Angwin, Jeff Larson, Surya Mattu and Lauren Kirchner, published in ProPublica May 23, 2016

Software can predict a person's risk to commit future crimes. That is what the makers of these products claim. In some US states, such software is already in use. There are even some judges relying on them. Julia Angin, Jeff Larson, Surya Mattu and Lauren Kirchner from the non profit news organization Pro Publica carried out a detailed analysis of data from 7,000 legal cases from the Broward County in Florida. More than that: They talked to a lot of the offenders some years after they had been sentenced. And finally, they wrote a comprehensive article about it mixing the data analysis with the personal stories of the (former) criminals. Their main finding: The software seems to be biased against blacks. The article was likely to raise a big controversy in the United States, where the discussion about equality between the ethnical groups is omnipresent. 
It is indeed astonishing that in the strongly regulated field of law enforcement authorities apparently make use of barely tested and more or less undocumented technical means. Surely, it is hard to resist to a new promising technology. There might be a lot of good reasons to implement it quickly. In most fields, that does not pose big problems -- as long as we are aware of it, understand and control it. Even in the euphoria of the quick technological change, we should not forget that there are some sensible fields in society. One of them is law enforcement: a balancing act between security for the society and the human rights of the accused person. Before implementing new technologies, we need to discuss and decide whether it should be permitted to use or not. If it is allowed to use: by whom and at what point? 
Instead of embracing new technologies, sometimes it is more professional to first keep a healthy distance. When in 2002 the news was spread about the Nasa still trying to buy Intel's old 8086 chips, the self taught techies made fun of these engineers. But maybe, at this point it was still the best option to use the very stable and well known old chip. [1] But let's hop over to a more similar example: Recently, there were discussions in Germany and Switzerland about so called dash cams. In court, should it be allowed to use the videos of -- for example an accident -- made with a camera that was installed in the car? The video could be helpful. But since it is forbidden to steadily film in public, the video is basically illegal. It is not until now that the courts define a procedure about it.[1]
Before implementing a software that gives a forecast about how an accused person is likely to act in future, we need specialists to conduct studies about the new tool. A blackbox like software is not acceptable. At least, a group of specialist needs to get insights in how the software works. Even better would be to make the code open source, so that everybody has the possibility to check it. If judges are allowed to use the software, they need to have a broad understanding of what it can do -- and what it can not provide. 
And of course: journalists need to be sensible for the increasingly importance of algorithms in our society. Some of them need to acquire the skills to understand the concepts of the software or even to read its code. Or they need the skills to do surveys -- like the journalists of Pro Publica did it in an impressive manner. Their article gives some ideas for own, smaller journalistic projects -- even if probably a quite different approach would be needed: In Switzerland it would be very hard to get a data set like the one Pro Publica received and it would certainly not contain the names and the pictures of the convicted persons for privacy reasons.

[1] William J. Broad: For Old Parts, NASA Boldly Goes . . . on eBay. http://www.nytimes.com/2002/05/12/technology/ebusiness/12NASA.html
[2] Sebastian Ertel: Nord-Süd-Gefälle bei der Verwertbarkeit von Dashcam-Aufzeichnungen? https://www.datenschutz-notizen.de/nord-sued-gefaelle-bei-der-verwertbarkeit-von-dashcam-aufzeichnungen-3111202/

