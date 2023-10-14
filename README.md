# Personal Assistant Robot - Bachelor's Thesis

This project aims to build an intelligent Personal Assistant Robot capable of receiving voice commands and performing simple tasks, including following a specific person (Follow Mode), retrieving objects (Find Object Mode), and providing information (Info Mode).

Internally, the robot operates using a modular design. It employs a micro-controller STM32F41106 to control the motors and the ultrasonic sensor, and a micro-controller Sipeed K210 is responsible for running the neural network, image processing, and embedded machine learning. Finally, a Raspberry Pi 3 serves as a central data management unit that coordinates both of these separate modules.

The robot's structure consists of a rover track belt connected to each motor, an aluminum chassis, and an external 3D finish.

I've organized the development of this project into eight basic stages:

1. Requirements Study: A study of how the project will function and which tools will be used to achieve its goals.
2. Basic Hardware and Software Tests: An examination of the sensors and microcontrollers used, validating each component separately before integration.
3. Development of the Integrated System: Tests and further development after the initial integration of peripheral systems.
4. Software Improvements: Evaluation of software features that can be added, removed, or enhanced to optimize the complete system.
5. Hardware Improvements: An investigation of hardware requirements for building PCB versions.
6. Software and Hardware Implementations: Implementation of software and hardware following information gathering.
7. Visual and Aesthetic Finishes: Consideration of the robot's visual features.
8. Final Tests and Adjustments.

Recent updates and checkpoints:

01/08/23: Basic Hardware and Software Tests Stage - Motor Control tests.

11/08/23: Basic Hardware and Software Tests Stage - Ultrasonic sensor tests.

20/08/23: Basic Hardware and Software Tests Stage - Motor Control and Ultrasonic sensor Integration.

02/09/23: Basic Hardware and Software Tests Stage - Temporary PCB added to the circuit.

(NOW) 01/10/23: Basic Hardware and Software Tests Stage - The robot is now capable of moving through the environment and avoiding obstacles using the ultrasonic sensor. I'm currently focused on ensuring communication between the ST Microcontroller and the Raspberry Pi."

Current Robot Images:
![Personal_Assistant_Robot1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/assets/22446244/e5b46cf7-b34e-46e4-ad61-13eb81d811cc)

![Personal_Assistant_Robot2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/assets/22446244/65def04f-73bd-4eb1-a230-806fc0ca966d)


The robot is a rover based on the project below:
https://github.com/SaralTayal123/Object-Finding-Rover/tree/master

