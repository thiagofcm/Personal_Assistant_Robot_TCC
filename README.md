# Personal Assistant Robot - Bachelor's Thesis

This project aims to build an intelligent Personal Assistant Robot capable of receiving voice commands and performing simple tasks, including following a specific person (Follow Mode), retrieving objects (Find Object Mode), and providing information (Info Mode).

Internally, the robot operates using a modular design. It employs a micro-controller STM32F41106 to control the motors and the ultrasonic sensor, and a micro-controller Sipeed Maixduino is responsible for running the neural network, image processing, and embedded machine learning. Finally, a Raspberry Pi 3 serves as a central data management unit that coordinates both of these separate modules.

The robot's structure consists of a rover track belt connected to each motor, an aluminum chassis, and an external 3D finish.

I've organized the development of this project into nine basic stages:

1. Development of Raspberry Pi 3 firmware, involving speech recognition and serial communication software to send commands and data to other microcontrollers.
2. Development of STM32 firmware, responsible for controlling motors and the ultrasonic sensor, as well as receiving commands and data from the Raspberry Pi controller.
3. Development of Maixduino firmware responsible for object and face detection, and reception of commands and data from the Raspberry Pi controller.
4. Basic Hardware and Software Tests: Examination of sensors and microcontroller firmware, validating each software and component separately before integration.
5. Development of the Integrated System: Testing and further development after the initial integration of peripheral systems.
6. Software Improvements: Evaluation of software features for potential additions, removals, or enhancements to optimize the complete system.
7. Hardware Improvements: Investigation of hardware requirements for building PCB versions and subsequent implementation.
8. 3D Printed Structure: Design and fabrication of a 3D printed structure for the robot, considering both functional and aesthetic aspects.
9. Final Tests and Adjustments: Final phase where rigorous testing is conducted to ensure the seamless integration of all components, functional accuracy, and optimal performance of the robot.

Recent updates and checkpoints:

01/08/23: Basic Hardware and Software Tests Stage - Motor Control tests.

11/08/23: Basic Hardware and Software Tests Stage - Ultrasonic sensor tests.

20/08/23: Basic Hardware and Software Tests Stage - Motor Control and Ultrasonic sensor Integration.

02/09/23: Basic Hardware and Software Tests Stage - Temporary PCB added to the circuit.

01/10/23: Basic Hardware and Software Tests Stage - The robot is now capable of moving through the environment and avoiding obstacles using the ultrasonic sensor. I'm currently focused on ensuring communication between the ST Microcontroller and the Raspberry Pi."

(NOW) 30/12/23: Writing and formalization of the preliminary project to be submitted to the evaluation committee of the Electrical and Computer Engineering Department.


Current Robot Images:
![Personal_Assistant_Robot1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/assets/22446244/e5b46cf7-b34e-46e4-ad61-13eb81d811cc)

![Personal_Assistant_Robot2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/assets/22446244/65def04f-73bd-4eb1-a230-806fc0ca966d)


The robot is a rover based on the project below:
https://github.com/SaralTayal123/Object-Finding-Rover/tree/master

