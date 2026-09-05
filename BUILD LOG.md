# Motivation
I wanted to build something of my own because I enjoy it and my professional environment lacked robotics and building in general

# Project Research
Searched the net for small projects that I could do at home with minimal tools and heavy machinery.
Watched youtube videos, read blogs, read social media accounts.
Most things I found were small 3D printed arduino run devices including: small arms, drones, RC cars, smart home electronics and more.
These all seemed like great ideas so I did some research on the necessary materials, costs and build processes to asses if the project could realistically be built in an ardinary bedroom with the tools I have.

**Samples from the research spreadsheet**
<img width="2758" height="712" alt="image" src="https://github.com/user-attachments/assets/1e227b98-4ddf-4b32-9767-9b655bf3b122" />
<img width="2772" height="686" alt="image" src="https://github.com/user-attachments/assets/3de69670-2201-494c-8cf2-32a93ebd6ed1" />
<img width="2748" height="862" alt="image" src="https://github.com/user-attachments/assets/dc3b543a-8413-4c8e-8fda-db6c7d159fc3" />

This process forced me to explore areas I did not go into in FRC that much. Primarily electronics. I soon discovered there was a whole community of hobbyists that build these kinds of things for fun.
It naturally led me to 2 attainable projects: a small servo powered arm and a small RC car.
I chose to start with the arm and plan to build the car later on.
I decided that I would run it using arduino and a few servos to begin with. I may but a Jetson later on to add some interesting vision based capabilities.
I ordered some servos and an arduino R4 from a local store and collected them.

# Design process
I was inspired by a couple of simple, bare bones, designs I found online.

<img width="372" height="427" alt="image" src="https://github.com/user-attachments/assets/7fb0b5ef-5faa-4ebc-affe-bd3940646b17" />
<img width="415" height="401" alt="image" src="https://github.com/user-attachments/assets/b8a9d816-3af6-4033-91a4-0d0e932d9d22" />

I was looking for somehthing that would be easy to design and I could get to building and tinkering with as soon as possible.

Next, I began to make rough sketches of what my design would look like.
I had to figure out a few things. How would I mount the servos to create the joints? What would the gripping mechanism look like? What would the overall structure look like? How big would it be? How many joints would it have? What would I use to connect the different bits and pieces?

<img width="1912" height="1482" alt="image" src="https://github.com/user-attachments/assets/9c32e04d-4852-4fdb-acaa-80a45663141e" />
<img width="1980" height="1108" alt="image" src="https://github.com/user-attachments/assets/c8c760ac-1ea6-4840-9eda-915dac9e2bb7" />

Then I started designing it in Fusion 360, a software I was familiar with from FRC.

**Sample Designs**

<img width="596" height="552" alt="image" src="https://github.com/user-attachments/assets/c996221f-8324-4f23-b560-2727b5d39ebf" />
<img width="635" height="530" alt="image" src="https://github.com/user-attachments/assets/b7c26798-a80a-40f0-847d-1b8638322628" />
<img width="629" height="494" alt="image" src="https://github.com/user-attachments/assets/c6bc7416-f76a-457a-b833-865edbf95ee3" />
<img width="361" height="609" alt="image" src="https://github.com/user-attachments/assets/2c10717a-bc11-42cd-afb3-3efbe8d74015" />
<img width="285" height="584" alt="image" src="https://github.com/user-attachments/assets/a569c97f-a190-4e41-9bd5-abf08a60e823" />

*All design files can be found in the design section of the repo*


# Manufacturing
Initially, I was hoping to get the 3D printing done at the robotics lab in my old high school.
Unfortunately, I didn't visit it very often and it was rarely open during my free time which would make printing difficult especially as I expected there would be some redesigns following unexpected problems which would require multiple printing sessions.

Therefore, after some consideration, I decided to buy my own 3D printer.
After conducting some research on small, affordable, at home printers I was on the fence between the BambuLab A1 Mini and the BambuLab A1 and eventually went with the A1.


A few weeks later it arrived and I began assembling it.

<img width="768" height="1024" alt="38DD6340-E659-4301-9512-B60C4362C64C_1_105_c" src="https://github.com/user-attachments/assets/7ddabbce-2e0c-46bf-a4f3-bed2692b496d" />


Printed my first Benchi on it!

<img width="768" height="1024" alt="4DBE9703-CD98-49ED-BAF4-426CE5AF0174_1_105_c" src="https://github.com/user-attachments/assets/84041878-a6f9-44fa-93ff-7dbaba4e883e" />


Then I got to printing the first parts of the arm I designed.
I will admit they were much smaller than I imagined they would be.

<img width="768" height="1024" alt="4F11367C-69A9-4DA9-83DC-9FFC51F4AC98_1_105_c" src="https://github.com/user-attachments/assets/2bffc4f1-7eac-4eac-a417-6ae208674ed7" />


I then encountered this concept called tolerance. I printed a few parts to figure out the ideal hole tolerance for the design.

<img width="768" height="1024" alt="BFB75307-9957-414A-9733-DA5323CDD01B_1_105_c" src="https://github.com/user-attachments/assets/d42e1c4c-67db-4280-99eb-c5e526507942" />


Finally, I managed to produce the first parts of the claw.

<img width="768" height="1024" alt="1B74D84E-F05B-4FDB-B70B-7D81E4293CED_1_105_c" src="https://github.com/user-attachments/assets/3c493a4f-f3b3-496a-980b-423da00f64e9" />

As I printed more parts I stumbled upon a few issues that required a take 2.
The base design did't account for the wires coming out of the servo resulting in a motor that fir only half way into the space I made for it.

<img width="1148" height="1014" alt="image" src="https://github.com/user-attachments/assets/b28b5e14-e182-466d-8fc4-f1ecf738ebd8" />


To fix the issue I redesigned the servo holder as 2 seperate parts - a gap in the base and an additional plate on top.

<img width="1220" height="1196" alt="image" src="https://github.com/user-attachments/assets/da49e4ac-b870-4164-8111-b3bc10fc043c" />

<img width="1080" height="1054" alt="image" src="https://github.com/user-attachments/assets/5d0a48da-439d-4647-9ae2-200b1441ffe1" />


I anticipated a similar issue with all the other servo holders on the arm so I went a heaed and redesgined that as well. The new design had the holder as 2 halfs that could be put together with screws.
The old one

<img width="992" height="898" alt="image" src="https://github.com/user-attachments/assets/e7799188-1a01-42cc-8a8b-a36bf9d3a10d" />

The new one

<img width="1210" height="950" alt="image" src="https://github.com/user-attachments/assets/d8e5fcb7-26fd-48f4-81c6-ac12c4496f35" />

<img width="1168" height="790" alt="image" src="https://github.com/user-attachments/assets/50925a41-b47c-4f8b-87ba-f75b213d0d66" />

<img width="958" height="750" alt="image" src="https://github.com/user-attachments/assets/742c8368-3983-4cab-a4a3-e7b3f4022939" />


I redesigned the first bottom joint to accomidate the changes and printed it.

<img width="1044" height="910" alt="image" src="https://github.com/user-attachments/assets/481bf827-26c6-402b-bef1-07ca6f5002a5" />

<img width="872" height="1212" alt="image" src="https://github.com/user-attachments/assets/bdafb75e-5982-4f3b-8cb6-fcd02c02445a" />













