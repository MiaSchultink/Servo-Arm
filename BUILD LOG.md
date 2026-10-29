# Why I built it
My professional environment lacked robotics and hands-on making. I felt that this was missing from my life and wanted to bring it back in by pursuing small robotics projects at home.

# Project research process
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


# Building (and redesigning along the way)
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

<img width="575" height="507" alt="image" src="https://github.com/user-attachments/assets/b28b5e14-e182-466d-8fc4-f1ecf738ebd8" />


To fix the issue I redesigned the servo holder as 2 seperate parts - a gap in the base and an additional plate on top.

<img width="560" height="598" alt="image" src="https://github.com/user-attachments/assets/da49e4ac-b870-4164-8111-b3bc10fc043c" />

<img width="540" height="527" alt="image" src="https://github.com/user-attachments/assets/5d0a48da-439d-4647-9ae2-200b1441ffe1" />


I anticipated a similar issue with all the other servo holders on the arm so I went a heaed and redesgined that as well. The new design had the holder as 2 halfs that could be put together with screws.
The old one

<img width="496" height="449" alt="image" src="https://github.com/user-attachments/assets/e7799188-1a01-42cc-8a8b-a36bf9d3a10d" />

The new one

<img width="605" height="475" alt="image" src="https://github.com/user-attachments/assets/d8e5fcb7-26fd-48f4-81c6-ac12c4496f35" />

<img width="584" height="395" alt="image" src="https://github.com/user-attachments/assets/50925a41-b47c-4f8b-87ba-f75b213d0d66" />

<img width="479" height="375" alt="image" src="https://github.com/user-attachments/assets/742c8368-3983-4cab-a4a3-e7b3f4022939" />


I redesigned the first bottom joint to accomidate the changes and printed it.

<img width="522" height="455" alt="image" src="https://github.com/user-attachments/assets/481bf827-26c6-402b-bef1-07ca6f5002a5" />

<img width="436" height="606" alt="image" src="https://github.com/user-attachments/assets/bdafb75e-5982-4f3b-8cb6-fcd02c02445a" />


I adjusted some of the middle joints to the new servo holders and printed them as well.

<img width="570" height="743" alt="image" src="https://github.com/user-attachments/assets/45488bda-c50a-47a7-9fda-2a666337e27d" />

When I tried to simulate putting them together I realized that I had forgotten to enlarge the hole at the bottom of the bottom joint to fit the appropriate servo head. This took a long time to print and I did not want to do it again unless absolutely necessary so I decided to risk just drilling it out to the appropriate size. I had nothing to lose honesrly. After my dad found an old drill in the wearhouse I got to work. After some drilling and scraping the edges of the hole clean with nail scissors, it worked.

<img width="524" height="730" alt="image" src="https://github.com/user-attachments/assets/2f5b5769-9572-4f1d-9c29-ea4cb26e7a20" />

<img width="605" height="714" alt="image" src="https://github.com/user-attachments/assets/ec9d4b6d-0f51-4e59-bd89-ae02c818f296" />


I also decided to remove the joint that allows the claw of the arm to spin. The motors I will use to operate the arm are small and weak as it is and I predict that they will have trouble bearing the load so I decided to remove unneccesary weight. This made the parts involved a lot simpler. I could just attach the base of the claw to the last joint.

<img width="798" height="1008" alt="image" src="https://github.com/user-attachments/assets/3856b4f2-880e-4184-9c1e-a45e69b806a7" />


The was arm starting to come together!

<img width="589" height="807" alt="image" src="https://github.com/user-attachments/assets/ce5cc577-ebb0-49d1-9b28-a6989a230689" />

<img width="497" height="763" alt="image" src="https://github.com/user-attachments/assets/b1f9ad54-8ede-476e-8ba1-03900ad6821f" />

One problem, I had no screws, allen keys or wrenches to put it together.
So I ordered some online from a store in Rishon LeZion.
This is what some of the shopping list looked like.

<img width="1518" height="1082" alt="image" src="https://github.com/user-attachments/assets/ca3e6900-d75e-4a9e-9ade-4bd2e4a32b87" />

I couldn't find a 5.5 wrench for the 3mm screws so I visited a few hardware stores in Herzliya. I didn't find one there but I did end up buying a few other things that came in handy. Files, project box, cutters...

<img width="1024" height="768" alt="AE31EE3C-37D9-4CE3-966C-7031910290E2_1_105_c" src="https://github.com/user-attachments/assets/0454984d-1f02-42e0-9661-243dad7509d8" />

When the screws arrived I got to work actually putting it all together.

<img width="5712" height="4284" alt="DBD82D98-77D2-4663-A282-A237B054DB27_1_201_a" src="https://github.com/user-attachments/assets/81c31d2b-59a9-45e7-aef5-9c8d624811a5" />

<img width="1024" height="768" alt="774375F0-BA89-4827-8DFB-B253E76FBC81_1_105_c" src="https://github.com/user-attachments/assets/7e011717-0e15-4de5-9ad9-98eae6898c14" />

<img width="1024" height="768" alt="662EB8AA-EF15-4E16-AFA8-F800E1FBE512_1_105_c" src="https://github.com/user-attachments/assets/f617717b-c3e2-41cd-84c6-84e8ac035aaa" />

<img width="768" height="1024" alt="B6E7BA14-E7FF-4E2F-A757-EB76F752C362_1_105_c" src="https://github.com/user-attachments/assets/b2898668-4ee9-43d4-ae3e-ea82b9d77efe" />

<img width="768" height="1024" alt="EC40B266-CA52-4867-B92D-4562C4B3B49A_1_105_c" src="https://github.com/user-attachments/assets/70d39e13-bc28-4eea-a93d-d25f1cede2a8" />

<img width="768" height="1024" alt="E494D4E1-9E5E-498D-8398-CF5EFE38BA11_1_105_c" src="https://github.com/user-attachments/assets/79631fc2-d0cf-44ab-8e12-a1b2ef17e1eb" />

Some of the tolerances were a little tight...

<img width="384" height="512" alt="9C400DE0-82A8-4D97-BE1F-8F8D08747BD7_1_105_c" src="https://github.com/user-attachments/assets/a2383dcb-d3e4-4dbf-8320-cc40f4dd384f" />

In some cases I didn't quite think about how a screw driver would reach the screw.

<img width="1536" height="2048" alt="D0A1B4E0-D637-44A2-AA66-349C93E9F30B_1_102_o" src="https://github.com/user-attachments/assets/7560b440-7e7e-4b3f-8e13-483d42b6d47a" />


This is how it turned out.

<img width="1536" height="2048" alt="B90166F0-E5AD-4C2B-A5A3-98A2119FB0B2_1_102_o" src="https://github.com/user-attachments/assets/3ba171b0-791a-4cc2-b1f3-5596de137b91" />


# Electronics

I started with one servo. I hooked it up to the 5V pin on the arduino R4 and plugged it into my computer.
It moved but often got stuck. After reading up on Arduino electronics I identified that this is definitely a power issue. The servo was drawing too much currnet. It became clear that if one servo drew too much current the 4 I planned to use on the arm would definitely do the same.

Turns out I needed a breadboard and an external power supply. Apparently it had to be at least 5V 3A.
I hadn't really wokred with Arduino electronics before so I did a little research and found [this helpful video] (https://www.youtube.com/watch?v=TkA2LJctU1c).

I wanted to draw out the wiring. I discovered this site called Tinkercad and decided to plan the basic wiring there.

https://github.com/user<img width="1080" height="1920" alt="532EA392-8BC7-4AEC-9766-2FD8D4E85CAC_1_102_o" src="https://github.com/user-attachments/assets/6b9f3787-896e-477f-8772-3ff37c0272ab" />
-attachments/assets/efcd9235-8b87-46f3-bb40-af65f36d5bae

<img width="2862" height="1334" alt="image" src="https://github.com/user-attachments/assets/c060a61d-b3a7-4216-8473-5662ae90a63b" />

I then proceeded to dig through my dad's cable closet to try and find such a wall outlet power supply. Sadly I did't find one.
There was another problem. Even if I did buy a wall outlet I had no way of supplying the power to the breadboard.

I did some research and found out about this component. I ordered it locally.

<img width="990" height="628" alt="image" src="https://github.com/user-attachments/assets/99380ae4-8b41-4b56-ac55-8e25ba6855d9" />

When I initially tried to controlservos with it they were a little jittery and buzzed quite a bit. I couldn't figure out why until I happened to stumble upon a video that explained that you needed to move a little cover from one pin to the other to make the adaptor supply 5V instead of 3.3V. [Video] (https://www.youtube.com/shorts/smU1wqvF5vg)

After a little more research I also found that it is actually better to feed the adaptor a power supply between 6-12V and let it convert it back down to 5V. I Dug through my dad's pile of cables again and found an 8.4V power supply.

The little yellow cap here

<img width="3024" height="4032" alt="218F58B5-D702-473D-B1D2-E589834A4D7E" src="https://github.com/user-attachments/assets/16337efa-a7d3-4b2c-8515-08b286697181" />

The setup ended up looking something like this. The Arduino was connected to my laptop and the breadboard was connected to a wall outlet through the adaptor.

<img width="384" height="512" alt="F7A3FE65-3F26-457C-9B66-8D0666B4167D_1_105_c" src="https://github.com/user-attachments/assets/22570b47-6c79-48aa-93bd-18c9172d78f3" />

I started by controlling one servo with the setup.

https://github.com/user-attachments/assets/3f21eb10-715f-4965-9a04-bfb45c7e197d


I also wondered how I would control the arm. Naturally, given my FRC + previous gaming experience the first thing that came to mind was a playstation controller.

I consulted claude on how I would connect a playstation controller to my setup. It suggested either using an ESP 32 for proper bluetooth or a USB host shield to connect the controller to the Arduino. I ended up buying a host shield but sadly it arrived without the pins and I didn't have much soldering equipment.












