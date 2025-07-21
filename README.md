# 🎙️ Voice Assistant (by Renamekk)

A simple and customizable voice assistant written in Python. Supports adding new commands via a configuration file and works entirely offline. Currently supports only **Russian language** voice input. Multilingual support is planned for the future.

---

## 🚀 Getting Started

### 1. Installation

1. Clone or download this repository.
2. Make sure you have **Python 3.10+** installed.
3. Install all dependencies by running:

- On **Windows**:
  ```bash
  install.bat
  ```
- On **linux/macOS**:
  ```
  install.sh
  ```

4. Launch the assistant:

   ```
   python main.py
   ```

5. Wakeword is:
   **Ассистент**
   You can change it in the **env.py** file

### 2. Editing Commands

All voice commands are configured in the **commands.yaml** file. Each command includes an action, voice confirmation sounds, and a list of trigger phrases.

#### 📸 Example: AHK Screenshot Command

```
- command:
    action: ahk                      # Indicates the use of AutoHotkey
    exe_path: ahk/screenshot.exe     # Path to the AHK executable
    exe_args:                        # Optional arguments if needed
  voice:
    sounds:
      - jarvis-og/ok1.wav
      - jarvis-og/ok2.wav
      - jarvis-og/ok3.wav
      - jarvis-og/ok4.wav
  phrases:
    - Снимок экрана                                # trigger phrases
    - Сними экран
    - сделай скриншот
```

#### 🌐 Example: Open Website Command

```
- command:
    action: url                      # Indicates this command opens a URL
    url_path: https://www.youtube.com/  # Url of website
  voice:
    sounds:
      - jarvis-og/ok1.wav
      - jarvis-og/ok2.wav
      - jarvis-og/ok3.wav
      - jarvis-og/ok4.wav
  phrases:
    - открой ютуб
    - ютуб
    - ютубчик

```

### 👤 Author

#### Developed by Renamekk

#### Currently supports only Russian.

#### New language support is planned in future versions.

### 📝 License

#### This project is licensed under the MIT License.

#### You are free to:

- Use the code for personal or commercial projects

- Modify it as you see fit

- Distribute your own versions

### However:

- Any modifications or forks are not affiliated with or endorsed by the original author. (Renamekk)

- The original author bears no responsibility for any issues caused by modified versions.
