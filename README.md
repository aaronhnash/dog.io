# dog.io
Continued work for the quadrupedal robot dog project from last semester. Viva la revolucion robotica!

## Existing Documentation
Documentation from the developer, most important links being documentatio referring to serial communication and the developer mode.
- https://www.xgorobot.com/XgoWiki-en/wiki/1%20XGO-Mini/Hardware%20overview/
- https://www.xgorobot.com/XgoWiki-en/wiki/1%20XGO-Mini/For%20XGO%20developer/Serial%20protocol/
- https://www.xgorobot.com/XgoWiki-en/wiki/1%20XGO-Mini/For%20XGO%20developer/Develop%20mode/
- https://www.xgorobot.com/XgoWiki-en/wiki/1%20XGO-Mini/For%20XGO%20developer/Python%20Lib/

## Video Demonstration
https://drive.google.com/file/d/1dwJAyGvHu0s48ufkFITGkstINDWe5Ncc/view?usp=sharing

## Goals for development
### Modifications to be made
- Replace current AI module with Raspberry Pi (presumably Pi Zero W)
- Re-create key MicroPython code to Python, if needed

### Features to add
- Autonomous walk cycle
- Obstacle avoidance (via ultrasonic sense, or similar module)
- Hand, Face recognition via OpenCV
- Voice recognition & commands
- Gesture control
- Fixed (static) ultrasonic sensor, and non-fixed (z-axis) mounted camera module

## Visual Demo Goals
1. Can walk around without any input from users
2. Can avoid obstacles/walls, turn around, and keep walking in a different direction
3. Voice commands as primary means of control
4. Say "come", and the dog begins looking for a face or a specific gesture. Will walk towards the recognized face, and then sit. 
5. Can follow somebody it recognizes
6. "Eyes" (camera) can move up/down in order to see more of environment
7. Can recognize and pick up ball (specific command "fetch" to make it search for ball?

## Hardware needed
- Raspberry Pi Zero W
- Raspberry Pi Cam
- Pi Cam Zero cable (separate)
- Ultrasonic sensor
- Additional servos
