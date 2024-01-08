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

01/10/23: Basic Hardware and Software Tests Stage - The robot is now capable of moving through the environment and avoiding obstacles using the ultrasonic sensor. I'm currently focused on ensuring communication between the ST Microcontroller and the Raspberry Pi."

# (NOW) 30/12/23: Writing and formalization of the preliminary project to be submitted to the evaluation committee of the Electrical and Computer Engineering Department.


# 5. Current Robot Images:
![Personal_Assistant_Robot1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/assets/22446244/e5b46cf7-b34e-46e4-ad61-13eb81d811cc)

![Personal_Assistant_Robot2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/assets/22446244/65def04f-73bd-4eb1-a230-806fc0ca966d)


# 6. References
The robot is a rover based on the project below:
https://github.com/SaralTayal123/Object-Finding-Rover/tree/master

