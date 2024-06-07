# Personal Assistant Robot - Bachelor's Thesis

![robot-oblique](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/Structure/Images/wisey-front%20(2).jpg)

# 1. Objective 
The main goal of this work is the development of an assistive robotic system capable of serving as an alternative for the care of elderly individuals with motor limitations. The robot will feature hardware and software resources related to artificial intelligence and computer vision applications to navigate through a domestic environment. Through voice commands, it will perform three tasks: recognize and deliver objects (Finder Mode), provide information and interact with users (Conversation Mode), and follow individuals (Follow Mode).

# 2. Tecnical Features
Internally, the robot operates using a modular design. It employs a micro-controller STM32F41106 to control the motors and the ultrasonic sensor. A microcontroller Sipeed Maixduino, responsible for running the neural network, image processing, and embedded machine learning. And finally, a Raspberry Pi 3, as a central data management unit that coordinates both of these separate modules. The robot's structure consists of a rover track belt connected to each motor, an aluminum chassis, and an external 3D structure.

# 3. Research Method 
In order to achieve the general and specific objectives of the work, the construction of the proposed system was divided into six basic stages: (i) Requirements and References Study, (ii) Development of microcontroller's firmware, (iii) Software Validation and Integration, (iv) PCB Development, (v) Design and Printing of the 3D Structure, (vi) Final Tests.

# 3.1 Requirements Study: 
- An analysis of relevant literature and projects to determine the project's approach and identify the tools necessary to achieve its goals.

# 3.2 Development of Microcontroller's firmware:
- Development of Raspberry Pi 3 firmware, involving speech recognition and serial communication software to send commands and data to other microcontrollers.
- Development of STM32 firmware, responsible for controlling motors and the ultrasonic sensor, as well as receiving commands and data from the Raspberry Pi controller.
- Development of Maixduino firmware responsible for object and face detection, and reception of commands and data from the Maixduino microcontroller.

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

# 4. Results

# 4.1 Software Design: 
The objective of developing the specific embedded firmwares for the system was successfully achieved. The image below shows a diagram illustrating the functionality, peripherals, and the relationship established by the programs between the MCUs.

imagem

# 4.2 PCB Development: 
A Printed Circuit Board (PCB) compatible with all the hardware resources used in the system, from MCUs to sensors, motors, LEDs, etc., was designed using the KiCad software. After being designed, the board was manufactured by JLC PCB. Below are images of the board layers as well as the board already fabricated and assembled. The files for reproduction and more information about this part of the project can be found in the PCB folder.

imagem

# 4.3 Structue Design
A modular structure was designed using the 3D modeling software Fusion 360 and was subsequently manufactured using 3D printing technology. All parts were designed to be compatible with the physical components of the system, as well as adapted to enhance the system's performance. The .SLT, .F3D files, and more images can be found in the Structure folder.

![PCB_FRONT](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/front-pcb-1-nobk.jpg)
![PCB_BACK](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/back-pcb-1-nbk.jpg)
![PCB_MANUFACTURED](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/pcb.jpg)
![PCB_MOUNTED_1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/pcb-1.jpg)
![PCB_MOUNTED_2] (https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/pcb-with-rasp.jpg)



# 5. Robot Images:
![Personal_Assistant_Robot1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/6b0b2d2e535fad894042e1c58aada04ed1e22924/Structure/Images/wise-hook.jpeg)

![Personal_Assistant_Robot2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/6b0b2d2e535fad894042e1c58aada04ed1e22924/Structure/Images/wise-button.jpeg)

![Personal_Assistant_Robot3](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/6b0b2d2e535fad894042e1c58aada04ed1e22924/Structure/Images/wisey-top.jpeg)

In the Development Checkpoints folder, you can find the entire development process of the project, including problems, solutions, challenges, tests, failures, and successes. I found it important to document this entire process so that if anyone is interested in reproducing and improving the project, they have references.

# 6. Demonstration Video:

imagem

A demonstration video of the robot in operation is available at the following link: https://youtu.be/cWnuLTotcqo?si=knrNkCdaKpj5jtFy

# 7. References
The robot is a rover based on the project below:
https://github.com/SaralTayal123/Object-Finding-Rover/tree/master

