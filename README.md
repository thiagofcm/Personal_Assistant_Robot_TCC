# Personal Assistant Robot - Bachaleror Thesis

This project aims to build an intelligent Personal Assistant Robot capable of receiving voice commands and performing simple tasks such as: following a specific person (Follow Mode), retrieving objects (Find Object Mode), and providing information (Info Mode).

Internally the robot works in a modular operate. It uses a micro-controller STM32F41106 to control the motors and the ultrasonic sensor, and a micro-controller Sipeed K210 responsible for allocate the neural network, image processing and embedded machine learning. Lastly, a Raspberry PI 3 works as a data central that manage both of the separated modules.

The structure of the robot is made by a rover track belt coupled in each motor, a aluminum chassis and an external 3D finish.

I organized the development of this project on 8 basically stages:

1. Requirements Study: A study of how my project will works and which tools will be used to achive this goal.
2. Basic Hardware and Software Tests: A study of the sensor and microcontrollers used. Validation of each separated component before an integration.
3. Development of the Integrated System: Tests and Developments after the first integration of pheriperical systems.
4. Software Improvements: A study of what software feature can be added, excluded or improved in order to the optimization of the complete system.
5. Hardware Improvements: A study of the hardware requirments to build the PCBs versions
6. Software and Hardware Implementations: Sofware and Hardware Implementaions after the previous information gathering.
7. Visual and Aesthetic Finishes: Study of the visual robot features.
8. Final tests and changes.

Recent updates and checkpoints:
01/08/23: Basic Hardware and Software Tests Stage - Motor Control
11/08/23: Basic Hardware and Software Tests Stage - Ultrasonic sensor tests
20/08/23: Basic Hardware and Software Tests Stage - Motor Control and Ultrasonic sensor Integration
02/09/23: Basic Hardware and Software Tests Stage - Temporary PCB added to the circuit
01/10/23: Basic Hardware and Software Tests Stage - The robot now is able to move through the enviroment and avoid obstacles by the ultrasonic sensor. Now I'm interesting on ensure the communication between the ST Microcontroller and the Raspberry Pi.

Current Robot Image:

The robot is a rover based on the project below:
https://github.com/SaralTayal123/Object-Finding-Rover/tree/master

