# Personal Assistant Robot - Bachelor's Thesis

# 1. Objective 
The main goal of this work is the development of an assistive robotic system capable of serving as an alternative for the care of elderly individuals with motor limitations. The robot will feature hardware and software resources related to artificial intelligence and computer vision applications to navigate through a domestic environment. Through voice commands, it will perform three tasks: recognize and deliver objects, provide information, and follow individuals.

# 2. Tecnical Features
Internally, the robot operates using a modular design. It employs a micro-controller STM32F41106 to control the motors and the ultrasonic sensor, and a micro-controller Sipeed Maixduino is responsible for running the neural network, image processing, and embedded machine learning. Finally, a Raspberry Pi 3 serves as a central data management unit that coordinates both of these separate modules. The robot's structure consists of a rover track belt connected to each motor, an aluminum chassis, and an external 3D finish.

# 3. Research Method 
In order to achieve the general and specific objectives of the work, the construction of the proposed system was divided into six basic stages: (i) Requirements and References Study, (ii) Development of microcontroller's firmware, (iii) Software Validation and Integration, (iv) PCB Development, (v) Design and Printing of the 3D Structure, (vi) Final Tests.

# 3.1 Requirements Study: 
- An analysis of relevant literature and projects to determine the project's approach and identify the tools necessary to achieve its goals.

# 3.2 Development of Microcontroller's firmware:
- Development of Raspberry Pi 3 firmware, involving speech recognition and serial communication software to send commands and data to other microcontrollers.
- Development of STM32 firmware, responsible for controlling motors and the ultrasonic sensor, as well as receiving commands and data from the Raspberry Pi controller.
- Development of Maixduino firmware responsible for object and face detection, and reception of commands and data from the Raspberry Pi controller.

# 3.3 Software Validation and Integration: 
- Examination of sensors and microcontroller firmware, validating each software and component separately before integration
- Development of the Integrated System that combines each firmware developed in a unity system.
- Evaluation of software features for potential additions, removals, or enhancements to optimize the complete system.

# 3.4 PCB Development:
- Investigation of hardware requirements for building PCB versions and subsequent implementation.

# 3.5 3D Printed Structure: 
- Design and fabrication of a 3D printed structure for the robot, considering both functional and aesthetic aspects.

# 3.6 Final Tests and Adjustments: 
- Final phase where rigorous testing is conducted to ensure the seamless integration of all components, functional accuracy, and optimal performance of the robot.

# 4. Recent updates and checkpoints:

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
 


NEXT STEPS: In the next few days, my effort will be focused on designing the circuit for this system. More specifically, I will use the software KiCad to design a PCB that meets the specific needs of this robot. This is aimed at reducing physical space, ensuring hardware functionality, providing autonomy to the robot, and giving a professional look to the system.

(26/01) Rasp-Maix Circuit:

![rasp_maix_circuit](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/63ea011f313f0d9b6ededb7f4899f473672e66a3/Maixduino/Images/rasp-maix-circuit.jpg)

# 5. Current Robot Images:
![Personal_Assistant_Robot1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/assets/22446244/e5b46cf7-b34e-46e4-ad61-13eb81d811cc)

![Personal_Assistant_Robot2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/assets/22446244/65def04f-73bd-4eb1-a230-806fc0ca966d)


# 6. References
The robot is a rover based on the project below:
https://github.com/SaralTayal123/Object-Finding-Rover/tree/master

