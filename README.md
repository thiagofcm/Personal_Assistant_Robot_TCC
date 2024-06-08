# Personal Assistant Robot - Bachelor's Thesis

![robot-oblique](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/4ae8f0512d489891ea1428c4595c266894abef41/Structure/Images/wisey-oblique.jpg)

# 1. Objective 
The main goal of this work is the development of an assistive robotic system capable of serving as an alternative for the care of elderly individuals with motor limitations. The robot will feature hardware and software resources related to artificial intelligence and computer vision applications to navigate through a domestic environment. Through voice commands, it will perform three tasks: recognize and deliver objects (Finder Mode), provide information and interact with users (Conversation Mode), and follow individuals (Follow Mode).

# 2. Methods

# 2.1 Development of MCUs firmwares:
- Development of Raspberry Pi 3 firmware, involving speech recognition and serial communication to send commands to the Maixduino MCU.
- Development of Maixduino firmware responsible for object and face detection, and reception of commands and data from the Raspberry Pi.
- Development of STM32 firmware, responsible for controlling motors and the ultrasonic sensor, as well as receiving commands and data from the Maixduino MCU.

# 2.2 Development of a PCB:
A professional PCB was designed on KiCad to ensure robust hardware-level functionality

# 2.3 Development of a robust structure:
- The robot's structure consists of a rover track belt connected to each motor, an aluminum chassis, and an external 3D structure.

# 3. Results

# 3.1 Software Design: 
Internally, the robot's functionallity is based on 3 embedded firmwares in 3 MCUs: 

- Raspberry Pi 3: This firmware responsible for Wi-Fi connectivity, processing audio data via the Google Speech-to-Text API, and transmitting data via UART to the Maixduino MCU. Basically, the Raspberry Pi will listen to voice commands and look for specific keywords, like "follow" or "bring me". Depending on which word/expression was detected, the Raspberry will send a UART message to Maixduino defining which AI it has to run
- Maixduino Sipeed: This MCU houses the neural network, camera, and embedded machine learning models. More especifically, this Maixduino's firmware runs AI models for object and face recognition under UART commands from the Raspberry Pi, and transmit targets coordinates to a STM32 MCU. 
- STM32F41106CCEU6:  This MCU is in charge of receive UART data from the Maixduino MCU and apply PWM signals to control the robot's position. The SMT32's firmware also controls an ultrassonic sensor and a buzzer that is enable when an obstacle is detected under 20cm

The image below shows a diagram illustrating the functionality, peripherals, and the relationship established between the MCUs.

![SOFTWARE_DESIGN](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/4ae8f0512d489891ea1428c4595c266894abef41/Documents/Firmwares-Diagram.jpg)

# 3.2 PCB Development: 
A Printed Circuit Board (PCB) compatible with all the hardware resources used in the system, from MCUs to sensors, motors, LEDs, etc., was designed using the KiCad software. After being designed, the board was manufactured by JLC PCB. Below are images of the board layers as well as the board already fabricated and assembled. The files for reproduction and more information about this part of the project can be found in the PCB folder.

![PCB_FRONT](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/front-pcb-1-nobk.jpg)
![PCB_BACK](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/back-pcb-1-nbk.jpg)
![PCB_MANUFACTURED](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/pcb.jpg)
![PCB_MOUNTED_1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/pcb-1.jpg)
![PCB_MOUNTED_2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/2f672d27ba32c738436c6a25cce9a761228e0c8b/PCB/Images/pcb-with-rasp.jpg)

# 3.3 Structure Design
A modular structure was designed using the 3D modeling software Fusion 360 and was subsequently manufactured using 3D printing technology. All parts were designed to be compatible with the physical components of the system, as well as adapted to enhance the system's performance. The .SLT, .F3D files, and more images can be found in the Structure folder.

![3D-VIEW](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/4ae8f0512d489891ea1428c4595c266894abef41/Structure/3D-Images/cool-view.jpg)
![3D-VIEW_WITH_SETAS](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/4ae8f0512d489891ea1428c4595c266894abef41/Structure/Images/wisey%20-%20setas.jpg)

# 4. Robot Images:
![Personal_Assistant_Robot1](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/6b0b2d2e535fad894042e1c58aada04ed1e22924/Structure/Images/wise-hook.jpeg)

![Personal_Assistant_Robot2](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/6b0b2d2e535fad894042e1c58aada04ed1e22924/Structure/Images/wise-button.jpeg)

![Personal_Assistant_Robot3](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/6b0b2d2e535fad894042e1c58aada04ed1e22924/Structure/Images/wisey-top.jpeg)

![Personal_Assistant_Robot3](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/4ae8f0512d489891ea1428c4595c266894abef41/Structure/Images/inside1.jpg)

In the Development Checkpoints folder, you can find the entire development process of the project, including problems, solutions, challenges, tests, failures, and successes. I found it important to document this entire process so that if anyone is interested in reproducing and improving the project, they have references.

# 5. Functionallity

The images below ilustrate the current funcionality of the robot:

Follow Mode:

![face_target](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/4ae8f0512d489891ea1428c4595c266894abef41/Maixduino/Images/face-target.jpg)

![follow-test](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/b1682fc5b20dd601ce84f9977aa9d9504989ea0d/Structure/Images/folllow-mode.jpg)

Finder Mode:
![finder-test-right](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/b1682fc5b20dd601ce84f9977aa9d9504989ea0d/Structure/Images/finder-mode-right.jpg)

![finder-test-fail](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/b1682fc5b20dd601ce84f9977aa9d9504989ea0d/Structure/Images/finder-mode-fail.jpg)

# 6. Demonstration Video:

![video-screen](https://github.com/thiagofcm/Personal_Assistant_Robot_TCC/blob/4ae8f0512d489891ea1428c4595c266894abef41/Structure/Images/video-screen.jpg)

A demonstration video of the robot in operation is available at the following link: https://youtu.be/cWnuLTotcqo?si=knrNkCdaKpj5jtFy

# 7. References
The robot is a rover based on the project below:
https://github.com/SaralTayal123/Object-Finding-Rover/tree/master

Contact:
Email: thiagof1503@gmail.com
Linkedin: https://www.linkedin.com/in/thiago-cuevas/