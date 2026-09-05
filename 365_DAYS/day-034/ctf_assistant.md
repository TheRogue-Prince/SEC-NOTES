![](Attachments/Pasted%20image%2020260801135615.png)

![](Attachments/Pasted%20image%2020260801135456.png)

A lightweight, automated reconnaissance analyzer built using Python and the official Google GenAI SDK. This tool feeds raw CTF or HTB scan logs directly into Gemini to extract targeted vulnerabilities, custom enumeration scripts, and precise exploitation paths.

## **1. Step-by-Step Implementation Guide**

### **Step 1: Environment Setup**

Create an isolated workspace and virtual environment to prevent global package conflicts:

Bash

```
mkdir ctf_assistant && cd ctf_assistant
python3 -m venv venv
source venv/bin/activate
```

### **Step 2: Install Dependencies**

Install the official modern Google GenAI library:

Bash

```
pip install google-genai
```

### **Step 3: Create the Script File**

Create a Python script named `ctf_assistant.py` inside your project directory:

Bash

```
touch ctf_assistant.py
```

## **2. Final Code (`ctf_assistant.py`)**

Python testing code.

```
import os
from google import genai
from google.genai import types

def analyze_ctf_recon(recon_data: str):
    # Initialize the Gemini client using the API key
    client = genai.Client(api_key="YOUR_API_KEY_HERE")
    
    # Define expert persona for offensive security context
    system_instruction = (
        "You are an expert offensive security assistant specializing in CTF competitions "
        "and Hack The Box labs. Analyze the provided reconnaissance data, identify potential "
        "vulnerabilities, misconfigurations, or service versions, and recommend specific, "
        "actionable next steps or payloads."
    )

    prompt = f"Here is the reconnaissance data:\n\n{recon_data}\n\nProvide an analysis and next steps."

    try:
        # Utilize the flash model pipeline for rapid inference
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.2, # Low temperature ensures deterministic, technical analysis
            ),
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Sample mock Nmap layout
    sample_recon = """
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5
    80/tcp open  http    Apache httpd 2.4.41
    | http-enum:
    |   /wordpress/: WordPress version 5.8
    """
    
    print("[*] Analyzing recon data with Gemini...")
    analysis = analyze_ctf_recon(sample_recon)
    print("\n[+] Gemini Recommendations:\n")
    print(analysis)
```

## **3. Problems Faced & Troubleshooting Notes**

1. **Virtual Environment Activation Typo:**
    
    - _Problem:_ Accidentally typed `source venve/bin/activate` instead of `venv`.
        
    - _Solution:_ Verified directory contents and corrected the spelling to `source venv/bin/activate`.
        
2. **Environment Variable Scope Mismatch in IDE:**
    
    - _Problem:_ Running the script through VS Code's internal debugger/launcher (`debugpy`) bypassed the terminal session's `export GEMINI_API_KEY="..."` variable, throwing a `ValueError: No API key was provided`.
        
    - _Solution:_ Explicitly passed the `api_key="..."` string directly into the `genai.Client(api_key="...")` constructor for seamless script execution across environments.
        
3. **Deprecated Model Version Error (`404 NOT_FOUND`):**
    
    - _Problem:_ Initial configuration targeted an older testing model version that was no longer available to new users, returning a `404` exception.
        
    - _Solution:_ Shifted the code configuration to utilize stable production-ready identifiers (`gemini-2.5-flash`).
        
4. **Free Tier Rate Limit Quota (`429 RESOURCE_EXHAUSTED`):**
    
    - _Problem:_ Hit minute/daily request restrictions on free-tier usage metrics during initial rapid testing.
        
    - _Solution:_ Accounted for token traffic thresholds and structured sequential requests with backoff times.
![](Attachments/Pasted%20image%2020260801135406.png)

```
import os

import subprocess

from google import genai

from google.genai import types

  

def run_nmap_scan(target_ip: str) -> str:

print(f"[*] Running Nmap scan against {target_ip}...")

try:

# Run a standard service and version detection scan (-sV) quietly (-T4 for speed)

command = ["nmap", "-sV", "-T4", target_ip]

result = subprocess.run(command, capture_output=True, text=True, check=True)

return result.stdout

except subprocess.CalledProcessError as e:

return f"Error running nmap: {e.stderr}"

except FileNotFoundError:

return "Error: nmap is not installed or not found in system path."

  

def analyze_ctf_recon(recon_data: str):

# Initialize the Gemini client with your API key

client = genai.Client(api_key="")

system_instruction = (

"You are an expert offensive security assistant specializing in CTF competitions "

"and Hack The Box labs. Analyze the provided reconnaissance data, identify potential "

"vulnerabilities, misconfigurations, or service versions, and recommend specific, "

"actionable next steps or payloads."

)

  

prompt = f"Here is the reconnaissance data:\n\n{recon_data}\n\nProvide an analysis and next steps."

  

try:

response = client.models.generate_content(

model='gemini-2.0-flash',

contents=prompt,

config=types.GenerateContentConfig(

system_instruction=system_instruction,

temperature=0.2,

),

)

return response.text

except Exception as e:

return f"An error occurred during AI analysis: {e}"

  

if __name__ == "__main__":

# Get the target lab IP address from user input

target = input("Enter the target lab IP address (e.g., 10.10.11.X): ").strip()

if target:

# Step 1: Automated Nmap Execution

scan_output = run_nmap_scan(target)

print("\n--- Nmap Output Captured ---")

print(scan_output)

print("----------------------------\n")

# Step 2: Gemini Analysis

print("[*] Sending scan data to Gemini for analysis...")

analysis = analyze_ctf_recon(scan_output)

print("\n[+] Gemini Recommendations:\n")

print(analysis)

else:

print("[-] No IP address provided. Exiting.")
```


without key in the code .

```
import os

import subprocess

from google import genai

from google.genai import types

  

def run_nmap_scan(target_ip: str) -> str:

print(f"[*] Running Nmap scan against {target_ip}...")

try:

command = ["nmap", "-sV", "-T4", target_ip]

result = subprocess.run(command, capture_output=True, text=True, check=True)

return result.stdout

except subprocess.CalledProcessError as e:

return f"Error running nmap: {e.stderr}"

except FileNotFoundError:

return "Error: nmap is not installed or not found in system path."

  

def analyze_ctf_recon(recon_data: str):

# Initializes using the GEMINI_API_KEY environment variable automatically

client = genai.Client()

system_instruction = (

"You are an expert offensive security assistant specializing in CTF competitions "

"and Hack The Box labs. Analyze the provided reconnaissance data, identify potential "

"vulnerabilities, misconfigurations, or service versions, and recommend specific, "

"actionable next steps or payloads."

)

  

prompt = f"Here is the reconnaissance data:\n\n{recon_data}\n\nProvide an analysis and next steps."

  

try:

response = client.models.generate_content(

model='gemini-3.6-flash',

contents=prompt,

config=types.GenerateContentConfig(

system_instruction=system_instruction,

temperature=0.2,

),

)

return response.text

except Exception as e:

return f"An error occurred during AI analysis: {e}"

  

if __name__ == "__main__":

target = input("Enter the target lab IP address (e.g., 10.10.11.X): ").strip()

if target:

scan_output = run_nmap_scan(target)

print("\n--- Nmap Output Captured ---")

print(scan_output)

print("----------------------------\n")

print("[*] Sending scan data to Gemini for analysis...")

analysis = analyze_ctf_recon(scan_output)

print("\n[+] Gemini Recommendations:\n")

print(analysis)

else:

print("[-] No IP address provided. Exiting.")
```

![](Attachments/Pasted%20image%2020260801150932.png)

one of the best version of code it almost automate everything.

```
import os

import subprocess

from google import genai

from google.genai import types

  

def execute_shell_command(command: str) -> str:

"""Executes a local command line security tool (like nmap, ffuf, gobuster) and returns the output logs.

Args:

command (str): The complete shell command to execute.

"""

print(f"\n[AI TOOL EXECUTION REQUEST] Running: {command}")

allowed_tools = ["nmap", "ffuf", "gobuster", "curl", "dirb", "cat"]

base_cmd = command.strip().split()[0]

if base_cmd not in allowed_tools:

return f"Error: Command '{base_cmd}' is not permitted."

try:

result = subprocess.run(

command,

shell=True,

capture_output=True,

text=True,

timeout=300

)

output = result.stdout if result.stdout else result.stderr

return output if output else "Command executed successfully with no output returned."

except subprocess.TimeoutExpired:

return "Error: Command timed out after 300 seconds."

except Exception as e:

return f"Error executing command: {str(e)}"

  

if __name__ == "__main__":

client = genai.Client()

target = input("Enter the target lab IP address (e.g., 10.10.11.X): ").strip()

if target:

system_instruction = (

"You are an expert autonomous penetration testing and CTF assistant. "

"You have access to a shell execution tool. Conduct comprehensive reconnaissance "

"on the target IP, chain your tool commands based on previous results, "

"and provide a final detailed vulnerability analysis and exploitation path."

)

  

print(f"\n[*] Starting autonomous chat agent loop for target {target}...")

  

try:

# Using chats handles multi-step tool execution loops seamlessly

chat = client.chats.create(

model='gemini-3.6-flash',

config=types.GenerateContentConfig(

system_instruction=system_instruction,

tools=[execute_shell_command],

temperature=0.2,

)

)

response = chat.send_message(f"Target IP: {target}. Begin your automated reconnaissance workflow.")

print("\n[+] Final AI Agent Analysis & Recon Summary:\n")

print(response.text)

  

except Exception as e:

print(f"[-] An error occurred during execution: {e}")

else:

print("[-] No IP address provided. Exiting.")
```

Output
```
[*] Starting autonomous chat agent loop for target 10.0.2.15...

[AI TOOL EXECUTION REQUEST] Running: nmap -sV -sC -p- --min-rate 1000 10.0.2.15

[AI TOOL EXECUTION REQUEST] Running: curl -s http://10.0.2.15:8000/

[AI TOOL EXECUTION REQUEST] Running: curl -s http://10.0.2.15:8000/backupagent
echo "--- sapservice ---"
curl -s http://10.0.2.15:8000/sapservice
echo "--- svc_qualys ---"
curl -s http://10.0.2.15:8000/svc_qualys
echo "--- svcvm ---"
curl -s http://10.0.2.15:8000/svcvm
echo "--- wley ---"
curl -s http://10.0.2.15:8000/wley

[AI TOOL EXECUTION REQUEST] Running: curl -s http://10.0.2.15:8000/kerbrute/

[AI TOOL EXECUTION REQUEST] Running: python3 -c '
import json, urllib.request

for fname in ["20260729101924_domains.json", "20260729101924_computers.json", "20260729101924_groups.json", "20260729101924_users.json"]:
    url = f"http://10.0.2.15:8000/{fname}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        meta = data.get("meta", {})
        count = len(data.get("data", []))
        print(f"File: {fname}, Count: {count}, Meta: {meta}")
'

[AI TOOL EXECUTION REQUEST] Running: jq '.' <<< '$(curl -s http://10.0.2.15:8000/20260729101924_domains.json)' | head -n 30

[AI TOOL EXECUTION REQUEST] Running: curl -s http://10.0.2.15:8000/20260729101924_domains.json | head -n 30

```

Delay based code to overcome the 5 req per second.

```
import os

import time

import subprocess

from google import genai

from google.genai import types

from google.genai.errors import APIError

  

def execute_shell_command(command: str) -> str:

"""Executes a local command line security tool (like nmap, ffuf, gobuster) and returns the output logs.

Args:

command (str): The complete shell command to execute.

"""

print(f"\n[AI TOOL EXECUTION REQUEST] Running: {command}\n" + "-"*40)

allowed_tools = ["nmap", "ffuf", "gobuster", "curl", "dirb", "cat", "python3", "jq"]

base_cmd = command.strip().split()[0]

if base_cmd not in allowed_tools:

return f"Error: Command '{base_cmd}' is not permitted."

output_lines = []

try:

process = subprocess.Popen(

command,

shell=True,

stdout=subprocess.PIPE,

stderr=subprocess.STDOUT,

text=True

)

for line in process.stdout:

print(line, end="")

output_lines.append(line)

process.wait(timeout=300)

full_output = "".join(output_lines)

return full_output if full_output else "Command executed successfully with no output returned."

except subprocess.TimeoutExpired:

process.kill()

return "Error: Command timed out after 300 seconds."

except Exception as e:

return f"Error executing command: {str(e)}"

  

if __name__ == "__main__":

client = genai.Client()

target = input("Enter the target lab IP address (e.g., 10.10.11.X): ").strip()

if target:

system_instruction = (

"You are an expert autonomous penetration testing and CTF assistant. "

"You have access to a shell execution tool. Conduct comprehensive reconnaissance "

"on the target IP, chain your tool commands based on previous results, "

"and provide a final detailed vulnerability analysis and exploitation path."

)

  

print(f"\n[*] Starting resilient autonomous chat agent loop for target {target}...")

  

try:

chat = client.chats.create(

model='gemini-3.6-flash',

config=types.GenerateContentConfig(

system_instruction=system_instruction,

tools=[execute_shell_command],

temperature=0.2,

)

)

message = f"Target IP: {target}. Begin your automated reconnaissance workflow."

# Rate-limit resilient execution loop

while True:

try:

response = chat.send_message(message)

break

except APIError as e:

if e.code == 429:

print(f"\n[!] Rate limit reached (429). Sleeping for 20 seconds before retrying...")

time.sleep(20)

continue

else:

raise e

  

print("\n[+] Final AI Agent Analysis & Recon Summary:\n")

print(response.text)

  

except Exception as e:

print(f"[-] An error occurred during execution: {e}")

else:

print("[-] No IP address provided. Exiting.")
```


## Evolution of the CTF Assistant Script

This document summarizes the chronological updates, core problems encountered, and structural improvements made to the autonomous CTF reconnaissance script.

### 1. Version Progression & Code Changes

- **v1.0 (Manual Analysis):**
    
    - **What it did:** Ran a single `nmap` scan via `subprocess`, captured the output text, and sent it once to Gemini to get recommendations.
        
    - **Limitation:** Completely static; the AI could not run further tools or inspect services dynamically.
        
- **v2.0 (Autonomous Agent Loop):**
    
    - **What it did:** Integrated native tool-use/function calling using `client.chats.create`. The script declared an `execute_shell_command` function that let the AI execute multiple security tools (`nmap`, `ffuf`, `curl`, `python3`, etc.) iteratively, chaining commands based on previous results.
        
    - **Limitation:** Fired requests back-to-back without pacing, which triggered severe free-tier API rate limits (`429 Too Many Requests`).
        
- **v3.0 (Rate-Limit Resilient Version):**
    
    - **What it did:** Added a retry block checking for `APIError` with code `429`, designed to catch throttling exceptions, sleep for a set duration, and resume automatically.
        
    - **Limitation:** Did not account for the absolute daily request limit (`20 requests per day` on the free tier), leading to persistent throttling once daily caps were exhausted.
        

### 2. Core Problems Faced & Resolutions

|**Problem Encountered**|**Root Cause**|**Resolution**|
|---|---|---|
|**API Key Exposure**|Hardcoding sensitive tokens directly into script source files.|Removed hardcoded values and migrated to automatic environment detection (`GEMINI_API_KEY`).|
|**Model Version 404 Errors**|Targeting outdated or deprecated model identifiers.|Switched configurations to current production identifiers (`gemini-3.6-flash`).|
|**Free Tier Quota Exhaustion (429)**|Rapid automated multi-step tool loops making too many requests per minute/day.|Implemented turn-pacing logic, sleep delays, and optional manual human-in-the-loop validation controls.|

### 3. Final Outcome & Capabilities

The final architecture transforms Gemini from a static text analyzer into an **interactive autonomous agent**:

1. **Dynamic Execution:** The model evaluates open ports and services in real-time.
    
2. **Tool Chaining:** If a web server or file listing is discovered, the AI automatically constructs and triggers deep-dive commands (`curl`, `ffuf`, custom Python extraction scripts) through local shell execution.
    
3. **Resilience & Control:** Scripts can be run either fully autonomously (with rate-limit management) or interactively with human oversight (`[y/N]` prompts) to prevent accidental quota blocks or unintended command executions.

### 1. `ctf_assistant_v1.py` (The Baseline)

- **What changed from your notes:** This is the standard, static script. It runs **only `nmap`** locally, passes the text to Gemini one single time, and prints the recommendation. It has **no tool-use loop**, meaning the AI cannot run secondary tools on its own.
    

### 2. `ctf_assistant_v2.py` (The Autonomous Agent)

- **What changed from v1:** Added the `execute_shell_command` function and configured `tools=[execute_shell_command]` inside `client.chats.create`.
    
- **The Difference:** Instead of just reading an Nmap scan, Gemini can now look at the results and **autonomously decide** to run `ffuf`, `gobuster`, `curl`, or python scripts on your machine loop-by-loop.
    

### 3. `ctf_assistant_v3.py` (The Rate-Limit Resilient Version)

- **What changed from v2:** Added `try...except APIError` logic wrapping `chat.send_message()` to catch code `429` (Too Many Requests) and force a `time.sleep(20)` cooldown before attempting to resume.
    
- **The Difference:** This version stops the script from crashing instantly when the free-tier per-minute limit is hit, allowing it to pause and recover automatically.