Keylogger Program  

📖 Description  
This repository contains a basic **keylogger program** built using Python. The program captures keyboard inputs (keystrokes) and logs them to a text file. This project is designed for **educational purposes only** to demonstrate the functionality of keyboard event handling.

🚀 Features  
- Logs alphanumeric keys and special keys.  
- Saves the logs to a file (`key_log.txt`).  
- Stops logging when the `Esc` key is pressed.  

⚙️ How It Works  
1. The keylogger uses the `pynput` library to listen for keyboard events.  
2. It captures both normal and special keys and writes them to a log file.  
3. The `Esc` key acts as a termination key to stop the program.

 📝 Installation and Usage  
 Prerequisites  
- Python 3.x  
- `pynput` library (install it with `pip install pynput`)

 Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/keylogger.git
   cd keylogger
   ```
2. Install the required dependency:  
   ```bash
   pip install pynput
   ```
3. Run the program:  
   ```bash
   python keylogger.py
   ```
4. Press the `Esc` key to stop logging.

 Output  
- The keystrokes will be saved in the `key_log.txt` file in the same directory.

 ⚠️ Ethical and Legal Disclaimer  
This program is for **educational purposes only**.  
- Do not use this software without explicit consent from users.  
- Unauthorized use of keyloggers is illegal and unethical.  
- Ensure compliance with all applicable laws and ethical guidelines.  

 🛠️ File Structure  
- `keylogger.py`: The Python script containing the keylogger code.  
- `key_log.txt`: The file where the logged keystrokes will be stored.  

👩‍💻 Author  
- [VENU MEKAPOTHULA](https://www.linkedin.com/in/venumekapothula/)  

Feel free to connect and share your feedback!

 📄 License  
This project is licensed under the MIT License. See the `LICENSE` file for details. 
