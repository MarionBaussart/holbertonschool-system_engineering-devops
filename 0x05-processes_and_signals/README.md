# 0x05-processes_and_signals

## 0. What is my PID
Write a Bash script that displays its own PID.

## 1. List your processes
Write a Bash script that displays a list of currently running processes.

Requirements:

* Must show all processes, for all users, including those which might not have a TTY
* Display in a user-oriented format
* Show process hierarchy

## 2. Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

* You cannot use pgrep
* The third line of your script must be # shellcheck disable=SC2009 (ignoring shellcheck error)

## 3. Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

* You cannot use ps

## 4. To infinity and beyond
Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

* In between each iteration of the loop, add a sleep 2

## 5. Don't stop me now!
We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:

* You must use kill

## 6. Stop me if you can
Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:

* You cannot use kill or killall