
📬 Mail Merge Automation

A simple yet powerful Python automation project that generates personalized invitation letters using text templates and dynamic placeholders such as [name], [date], and [event].

This project was built as part of my Day 24 Python milestone to strengthen file handling, path management, and automation logic using modern Python tools like pathlib.

⸻

✨ Features
	•	📁 Reads recipient names from a text file
	•	🧠 Supports multiple placeholders: [name], [date], [event]
	•	🪶 Automatically generates personalized letters for each name
	•	💾 Saves outputs safely into a clean Output/ReadyToSend folder
	•	⚙️ Uses pathlib for OS-independent paths
	•	🚀 Can be extended to send letters as emails or export PDFs

⸻

🧠 Skills Practiced
	•	File I/O (open, read, write)
	•	String replacement and formatting
	•	Path handling using pathlib
	•	Code modularization (functions + constants)
	•	Automation mindset for repetitive tasks

⸻

🧩 Project Structure

mail-merge-automation/
 ├── main.py
 ├── Input/
 │   ├── Names/
 │   │   └── invited_names.txt
 │   └── Letters/
 │       └── starting_letter.txt
 ├── Output/
 │   └── ReadyToSend/
 ├── sample_output/
 │   └── letter_for_Sam.txt
 └── README.md


⸻

⚙️ How It Works

1️⃣ The script reads names from Input/Names/invited_names.txt
2️⃣ It loads a template from Input/Letters/starting_letter.txt
3️⃣ It replaces placeholders ([name], [date], [event])
4️⃣ It writes personalized letters in Output/ReadyToSend/

⸻

🧾 Example

Template (starting_letter.txt)

Dear [name],

You are invited to our [event] happening on [date]!
See you soon.

Names (invited_names.txt)

Angela
Rishi
Sam

Output (letter_to_Sam.txt)

Dear Sam,

You are invited to our Python Study Group Meetup happening on 2025-10-16!
See you soon.


⸻

▶️ How to Run

In your terminal:

python main.py

✅ The personalized letters will appear inside:

Output/ReadyToSend/


⸻

🚀 Future Improvements
	•	🧾 Add email-sending functionality via SMTP
	•	🪄 Export generated letters as PDFs
	•	💬 Add a GUI interface (Tkinter)
	•	⚙️ Add command-line arguments for templates and names file paths

⸻




