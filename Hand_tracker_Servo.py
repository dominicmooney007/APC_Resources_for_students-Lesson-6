from cvzone.HandTrackingModule import HandDetector
import cv2
from gpiozero import Servo
import cvzone
import threading
import time

# Initialize Servo on GPIO pin 18 (you can change this to any available PWM-capable GPIO pin)
servo = Servo(12)

# Initialize the webcam to capture video
# Use 0 for the default camera on Raspberry Pi
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Servo status flags
servo_sweeping = False
sweep_thread = None
stop_sweep = False

def sweep_servo():
    """Function to sweep servo from 0 to 180 degrees and back"""
    global stop_sweep
    stop_sweep = False
    
    while not stop_sweep:
        # Sweep from -1 to 1 (0 to 180 degrees)
        for angle in range(-100, 101, 5):  # -1 to 1 in 0.05 increments
            if stop_sweep:
                break
            servo.value = angle / 100.0  # Convert to -1 to 1 range
            time.sleep(0.05)  # Small delay for smooth movement
        
        # Sweep back from 1 to -1 (180 to 0 degrees)
        for angle in range(100, -101, -5):  # 1 to -1 in 0.05 decrements
            if stop_sweep:
                break
            servo.value = angle / 100.0  # Convert to -1 to 1 range
            time.sleep(0.05)  # Small delay for smooth movement

def start_servo_sweep():
    """Start the servo sweeping in a separate thread"""
    global servo_sweeping, sweep_thread, stop_sweep
    
    if not servo_sweeping:
        servo_sweeping = True
        stop_sweep = False
        sweep_thread = threading.Thread(target=sweep_servo)
        sweep_thread.daemon = True  # Dies when main program exits
        sweep_thread.start()

def stop_servo_sweep():
    """Stop the servo sweeping"""
    global servo_sweeping, stop_sweep
    
    if servo_sweeping:
        stop_sweep = True
        servo_sweeping = False
        # Return servo to center position
        servo.value = 0
        time.sleep(0.1)  # Brief pause to reach center

try:
    # Continuously get frames from the webcam
    while True:
        # Capture each frame from the webcam
        success, img = cap.read()
        
        if not success:
            print("Failed to read from camera")
            break
        
        # Find hands in the current frame
        hands, img = detector.findHands(img, draw=True, flipType=True)
        
        # Check if any hands are detected
        if hands:
            # Information for the first hand detected
            hand1 = hands[0]
            
            # Count the number of fingers up for the first hand
            fingers1 = detector.fingersUp(hand1)
            finger_count = fingers1.count(1)
            
            # Control Servo based on finger count
            if finger_count == 3:
                if not servo_sweeping:
                    start_servo_sweep()
                servo_color = (0, 255, 0)  # Green when servo is sweeping
            else:
                if servo_sweeping:
                    stop_servo_sweep()
                servo_color = (0, 0, 255)  # Red when servo is stopped
            
            # Display finger count on screen
            cvzone.putTextRect(img, f"Fingers: {finger_count}", (50, 50), 
                             scale=2, thickness=2, 
                             colorT=(255, 255, 255), colorR=(255, 0, 255))
            
            # Display servo status
            status_text = "Servo: SWEEPING" if servo_sweeping else "Servo: STOPPED"
            cvzone.putTextRect(img, status_text, (50, 100), 
                             scale=2, thickness=2,
                             colorT=(255, 255, 255), colorR=servo_color)
            
            # Visual indicator circle
            cv2.circle(img, (300, 75), 20, servo_color, cv2.FILLED)
            
            # Display current servo position (approximate)
            current_pos = int((servo.value + 1) * 90)  # Convert -1,1 to 0,180 degrees
            cvzone.putTextRect(img, f"Servo Angle: {current_pos}°", (50, 150), 
                             scale=1.5, thickness=2,
                             colorT=(255, 255, 255), colorR=(0, 255, 255))
            
            # Print to console
            print(f"Fingers: {finger_count} | Servo: {'SWEEPING' if servo_sweeping else 'STOPPED'}")
            
            # Check if a second hand is detected
            if len(hands) == 2:
                hand2 = hands[1]
                fingers2 = detector.fingersUp(hand2)
                print(f"Hand 2: {fingers2.count(1)} fingers")
        else:
            # No hands detected - stop servo
            if servo_sweeping:
                stop_servo_sweep()
            
            # Display status when no hands detected
            cvzone.putTextRect(img, "No hands detected", (50, 50),
                             scale=2, thickness=2,
                             colorT=(255, 255, 255), colorR=(128, 128, 128))
            cvzone.putTextRect(img, "Servo: STOPPED", (50, 100),
                             scale=2, thickness=2,
                             colorT=(255, 255, 255), colorR=(0, 0, 255))
        
        # Display the image in a window
        cv2.imshow("Hand Tracking - Servo Control", img)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("\nProgram interrupted by user")

finally:
    # Clean up
    stop_sweep = True  # Stop any ongoing sweep
    servo.value = 0    # Return servo to center
    time.sleep(0.2)    # Give time to reach center
    servo.close()
    cap.release()
    cv2.destroyAllWindows()
    print("Cleanup complete - Servo stopped and resources released")
