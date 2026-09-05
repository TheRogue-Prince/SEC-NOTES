
Using the techniques shown in this section, find the cleartext password for the bob_adm user on the target system.


### Step 1: Strip the "Mark-of-the-Web" Security Blocks

PowerShell

```
Get-ChildItem -Path C:\tools\PSSQLite\ -Recurse | Unblock-File
```

- **What it does:** It looks inside the `C:\tools\PSSQLite\` folder, finds every single file (including subfolders via `-Recurse`), and passes them to `Unblock-File`.
    
- **Why it’s necessary:** Windows automatically blocks files downloaded from the internet. This command safely removes that block so Windows won't throw unauthorized access errors or pop up warnings when you try to run them.
    

### Step 2: Navigate and Load the SQLite Module

PowerShell

```
cd .\PSSQLite\
Import-Module .\PSSQLite.psd1
```

- **What it does:** It changes your current directory into the folder containing the module, and then loads the definition file (`.psd1`).
    
- **Why it’s necessary:** Standard PowerShell doesn't natively know how to open or interact with SQLite databases. Importing this module introduces brand new custom commands (like `Invoke-SqliteQuery`) directly into your current terminal session.
    

### Step 3: Define the Path to the Sticky Notes Database

PowerShell

```
$db = 'C:\Users\htb-student\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite'
```

- **What it does:** It creates a shortcut variable named `$db` that points directly to the exact file path where the Windows Modern App version of Sticky Notes saves its data.
    
- **Why it’s necessary:** Modern Windows apps store data in isolated folders inside `AppData\Local\Packages\`. The file `plum.sqlite` is a standard SQLite database that holds all your note history.
    

### Step 4: Query the Database and Format the Text

PowerShell

```
Invoke-SqliteQuery -Database $db -Query "SELECT Text FROM Note" | ft -wrap
```

- **What it does:** This is the execution step. It instructs the database engine to run a specific structured query:
    
    - **`Invoke-SqliteQuery`**: The function you loaded in Step 2.
        
    - **`-Database $db`**: Tells it to open the file path stored in your variable.
        
    - **`-Query "SELECT Text FROM Note"`**: This is an SQL statement telling the file: _"Go into the table called `Note` and grab everything stored under the column called `Text`."_
        
    - **`| ft -wrap`**: Short for `Format-Table -Wrap`. This ensures that long sentences inside the notes don't get cut off at the edge of your terminal window; instead, they gracefully wrap down to the next line so you can read the passwords, flags, or secrets in full plain text.
