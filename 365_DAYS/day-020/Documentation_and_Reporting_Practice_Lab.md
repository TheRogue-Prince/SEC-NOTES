You are an assessor for Acme Security, Ltd. Your team has been hired to perform an internal penetration test against one of Inlanefreight's internal networks. The tester assigned to the project had to go out on leave unexpectedly, so you have been tasked by your manager with taking over the assessment. You've had limited communication with the tester, and all of their notes are left on the testing VM configured within the internal network. The scope provided by the client is as follows:

- Network range: `172.16.5.0/24`
- Domain: `INLANEFREIGHT.LOCAL`

Your teammate has already created a directory structure and detailed Obsidian notebook to record their testing activities. They made a list of `13 findings` but only recorded evidence for a few of them. Step in as the penetration tester and complete this mock engagement to the best of your abilities. Experiment with the following to refine your skills:

- Set up Tmux logging and record all of your evidence using Tmux while getting more comfortable with the tool
- Enumerate and exploit all 13 findings listed and gather evidence for the findings that don't have any evidence recorded in the notebook
- Keep a detailed log of all activities you perform
- Update the payload log as needed
- Log all scan and tool output generated while performing enumeration and gathering additional finding evidence
- Practice writing up the findings using either WriteHat or the provided reporting template, or practice with both.
- Finish the penetration test and complete the questions below to conclude this module.

We recommend using the provided version of the Obsidian notebook or recreating the notebook structure and directory structure locally or on the Pwnbox using Obsidian or your own preferred tool. Remember that once the lab resets, you will lose all progress and data saved on the testing VM, so make local copies of any data you would like to use to practice writing your own findings and report if you choose to complete the optional exercise included in this section.

The tasks in this section are mostly optional but highly encouraged. Completing them will give you a feel for how an internal penetration test is conducted and give you a chance to practice the extremely important skill of documentation and reporting. If you complete this entire practice lab, create a sample report, and do the same for the `Attacking Enterprise Networks` module, you will be very well prepared for any Hack The Box Academy exams that require a report to be submitted.

Good luck, and have fun. You'll get out of this module and practice lab as much as you put in.

Keep hacking, and remember to think outside the box!

**Q1. Connect to the testing VM using Xfreerdp and practice testing, documentation, and reporting against the target lab. Once the target spawns, browse to the WriteHat instance on port 443 and authenticate with the provided admin credentials. Play around with the tool and practice adding findings to the database to get a feel for the reporting tools available to us. Remember that all data will be lost once the target resets, so save any practice findings locally! Next, complete the in-progress penetration test. Once you achieve Domain Admin level access, submit the contents of the flag.txt file on the Administrator Desktop on the DC01 host.

we got the info from the notes that we were able to spoof response using responder, we were able to get some 3 users ntlm v2 hashes, using hashcat we cracked and got the password.
```

backupagent::INLANEFREIGHT:6c8613c3033a61f2:11193C889AB1B85D31EB1236B53C1C8C:010100000000000080AB3A23BE15DD01A0B2E81837318E310000000002000800320049005000490001001E00570049004E002D003800390032003900580058004E00450054005200580004003400570049004E002D003800390032003900580058004E0045005400520058002E0032004900500049002E004C004F00430041004C000300140032004900500049002E004C004F00430041004C000500140032004900500049002E004C004F00430041004C000700080080AB3A23BE15DD0106000400020000000800300030000000000000000000000000300000F066614793B03DB455C04F97B0ADB27B235ED2DA947DFE2B3E55E02924967AD90A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000


```

after getting the creds we tried ran bloodhound.py and  found out this user was part of domain admins so we tried logging using evil-winrm after scanning the ip using nmap.

then we used secretsdump.py  to dump the hashes we were able to get  the KRBTGT user hash and also we were able to find the svc_reporting user hash .


I think this was the easiest way we do have many other options attack options available as we have a lot of information about the target in the notes.
