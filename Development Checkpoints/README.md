
# Updates and checkpoints:

01/08/23: Basic Hardware and Software Tests Stage - Motor Control tests.

11/08/23: Basic Hardware and Software Tests Stage - Ultrasonic sensor tests.

20/08/23: Basic Hardware and Software Tests Stage - Motor Control and Ultrasonic sensor Integration.

02/09/23: Basic Hardware and Software Tests Stage - Temporary PCB added to the circuit.

01/10/23: Basic Hardware and Software Tests Stage - The robot is now capable of moving through the environment and avoiding obstacles using the ultrasonic sensor. 

20/12/23: Writing and formalization of the preliminary project to be submitted to the evaluation committee of the Electrical and Computer Engineering Department.

07/01/24: Finish of the preliminary project (Documents/Projeto__TCC__Thiago_Cuevas.pdf).

12/01/24: Development of the speech recognition and voice assistant firmware on Rasbperry Pi 3 (Rasp/scr). 

16/01/24: Development of a UART communication firmware test between Rasp and Maixduino.

15/01/24: Development of the tracking objects firmware on Maixduino. A servo motor is already capable of follow the movement of an object.

20/01/24: Voice assistant running with an ChatGPT API that answers questions based on OpenAI database.

22/01/24: UART communication between Rasp and Maixduino done and already capable of switch between two different AI models (face recognition, to follow people, and object detection, to deliver objects).

23/01/24: Looking for complete and make improvements in the maixduino switching_models and voice_assistant code. Some problems include:
- The voice assistant still listening during an object or face detection task, which it's annoying because the assistant tries to listen and understand what he is not supposed to listen or understand.
- The Object recognition model needs to track and get the relative position of the object. The code at this point already satisfies this requirement, but without any filter. As the user asks for an especific object, the firmware has to understand and apply an filter to track the right object.
- The Face recognition model needs to track and get the relative position of a face, and also estimate a distance based on the area of the rectangle draw around a recognized face. This feature is not complete.

24/01/24: Looking for make improvements in the IA models. Updates:
- Maixduino is running a Switching models code able to change between the object detection and face detection model by serial commands from the Raspberry Pi.
- Maixduino display a message "waiting command" when it is awaiting for a voice/serial command by the user and the Raspberry Pi.

![image_waiting_command](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/d28b8e27569ad44e4f325c1ccfb675bf6a05b32c/Maixduino/Images/waiting-command.jpg)

- Object detection function now gets the relative position only of the objects required by the user. In the example below, the object required was a car, so the rectangle red and the red circle in the center of the object represents that the model understand that is the object that has to be tracked. 

![image_car_object_detection](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/63ea011f313f0d9b6ededb7f4899f473672e66a3/Maixduino/Images/object-detection-car.jpg)

In other hand, the image of a dog, that's not a car is sourrounded by a green rectangle without any circle in the center, representing that despite recognized, the object is not being tracked.

![image_dog_object_detection](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/d28b8e27569ad44e4f325c1ccfb675bf6a05b32c/Maixduino/Images/object-detection-dog.jpg)

- Face detection function now gets the relative position of faces but just one at time. Seems like when more than one face is captured by the camera, the program doesnt know exactly wich face to track. 

25/01/24: Improvements in the Face Detection model done. Updates:
- The Face Detection model is now able to identify the face with largest area and draw a circle in the center of the rectangle area around the face. This circle is used to track de coordinates of the face's position.

![faces_recognition](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/d28b8e27569ad44e4f325c1ccfb675bf6a05b32c/Maixduino/Images/facedetection-img.jpg)

![faces_recognition_2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/63ea011f313f0d9b6ededb7f4899f473672e66a3/Maixduino/Images/face-detection-two-faces.jpg)

29/01/24: A 3D Pan Tilt has been printed and added to see the servo tracking control. Updates:
- The tilt can follow the face with the biggest area. 
- Face detection firmware now gets the x and y relative position and send it via UART to the STM32 (UART seems to be easier to control than I2C protocol).
- The plan is make the STM32 MCU receive data in the format (x,y,area). I am trying to use the Direct Memory Access (DMA) to receive the data in order to significantly reduce the CPU load. However, I still don't know why, but the STM32 is receveing just one byte of the whole frame data from the Maixduino. Example: If I send (23,53,5432), the STM32 is able to fill one or two positions of the buffer, like '(' and sometimes '(' and '2'. I tested this STM32 firmware trying to receive data from the Raspberry Pi and it worked, but with Maixduino did not.

![tracking_faces](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/5730fe4686859f6b05fadbe6154ccdc2a8b61f4a/Maixduino/Images/tracking-objects.gif)

01/01/24: The STM32 is now receiving the complete coordinates data from Maixduino, in the format (x,y,area) and using DMA. Updates:
- A new microphone from Logitech Webcam was added. Now, the voice recognition is more accurate and the system can listen commands in a larger distance.

02/02/24: Based on the x coordinate received by the Maixduino, the STM32 is now able to adjusts the PWM signal sent to the motors and make movements like turn to the right, left, and stop ensuring the robot maintains its position consistently in front of the object or face. 
- I still need to add a function to handle the received area data and adjust a threshold parameter to maintain an optimal distance between the object/face and the robot. However, to guarantee accurate modifications and calibrations in this implementation, it is necessary to have an autonomous system and structure already working, one that does not depend on USB supply. 
 
![motor-tracking-objects](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/c0de329dd76626097e39e07f059259708d78e37e/Maixduino/Images/motor-tracking-objects.gif)

04/01/24: I developed a block diagram of the system workflow (Documents/Personal_Assistant_Diagram) to facilitate software and hardware design and development.  

07/02/24: I started the schematic of the PCB on KiCad. Software Updates:
- I made some improvements in the ST code. Now the motors stop and a buzzer is activated when an object or obstacle is within a range of 15cm of the robot.
- I added some LEDs to the Rasp Circuit. The green LED turns on when the system is initialized and ready to receive commands. The blue LED turns on when the wake-word is detected, and the red LED represents when the robot is busy on a task.
- These improvements are changes that I had already in mind since the beginning of the implementation, that I was just leaving for the end. However, the PCB design requires that all components and pinouts be counted.

27/02/24: I finished the PCB design on KiCad and have already ordered it on JLCPCB.
- I suppose to receive the PCB by mid or end of march.
- I modeled the 3D Structure on Fusion 360, and now I'm waiting to have all parts printed.

![PCB](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/cc6b8f6fa20da5be5db632fd58bd541c2c76b498/PCB/Images/Personal_Assistant_Robot_TCC.jpg)

![PCB_routing1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/d1781523850589c5f9d656b7d66d7770522fb80b/PCB/Images/back-pcb-1-nbk.jpg)

![PCB_routing2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/d1781523850589c5f9d656b7d66d7770522fb80b/PCB/Images/front-pcb-1-nobk.jpg)

![3D_Structure](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/6b0b2d2e535fad894042e1c58aada04ed1e22924/Structure/Images/3d-robot2.jpg)

20/03/24: After nearly a month of anticipation, both the PCB and the 3D printed structure have finally arrived! :)

![pcb-done](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/d1781523850589c5f9d656b7d66d7770522fb80b/PCB/Images/pcb.jpg)

- I am currently in the process of soldering the components onto the PCB, meticulously testing each one before integrating them into the entire system. 

![pcb-wout-rasp](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/605e8bc51dbbb05c4b6cf57f8b396b285ea71423/PCB/Images/pcb-1.jpg)

- The 3D structure fits flawlessly and looks quite impressive.

![robot-oblique](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/6b0b2d2e535fad894042e1c58aada04ed1e22924/Structure/Images/wisey-front.jpeg)

- Simultaneously, progress is being made on the written aspect of the project.

12/04/24: The PCB worked very well, and tests to verify the system functionality were conducted. 
- The system successfully interacted with the user, maintaining a fluent and cohesive conversation. 
- The robot also exhibited commendable performance in detecting and tracking users, although it encountered limitations in perceiving and capturing objects.
- Given that the detection model has a restricted list of recognizable objects, with not all of them being domestic items, an adapted structure with a picture of the object was devised to enhance the recognition of specific items.
- It was noted that the model is capable of recognizing objects at close range, possibly due to the camera's low resolution in this dimension.
- Also, the gripper system did not function as expected, likely due to insufficient motor torque and less effective gear system coupling. Despite this, the robot managed to detect objects under specific conditions and move towards them.
- The written part of the project has been done, and after be reviewd by the Faculty, will be available in the Documents directory.
- A video showing all the skills of the robot is under development, and will be available on Youtube.
