# Advanced Python Calculator for IS218, Building Web Applications.

## App Demonstration: https://youtu.be/jWWxObkXaCA ##

## Introduction ## 
This project serves to teach us how to develop an advanced calculator application utilizing python's native functionality. 

A big point of emphasis has been developing professional software development practices. 

## Core Functionalities ## 

This application comes with the ability to perform one of the four basic arithmetic operations on any pair of numbers, which are input by the user. These operations can be accessed via the inputting of commands.

### Command Line Interface (REPL) ###

Within the init file for the app module (see the folder labelled app), there is a read-eval-print loop that allows us to access the application via the command line. **The start method defined in line 58** is primarily how this is achieved. Once an entry file is executed (in this case, the Main.py file), the start method is called. This method begins a while loop that only ends once the exit command is entered into the terminal. During this while loop, the command line will accept inputs from the keyboard. There is a try catch block that utilizes a command handler (defined in init file in the commands folder), to read the input from the keyboard. If the input matches a known plug in, the command is executed. Otherwise, the user is alerted that no such command exists. 

### Plugin System ###

The **load_plugins method defined on line 38** of the init file of the app folder, is how the plugin system is acheived. This method executes a loop that cycles through the plugins subdirectory of the app folder. Any futher subdirectories that are discovered through this loop are then imported into the application as commands to be executed.

As previosuly mentioned, these are all integrated into the program using a command handler, defined in line 8 of the command folder's module file. This class comes with the register_command method, which allows given inputs to be registered as commands in our application, without having to change the structure of the application. At all. This is useful as commaands can be added or removed on a whim. 

### Logging ###
 
Logging has been implemented in my project, with the system logging each and every process within the application, from the starting of the application, to the loading of the environment variables and plugins, and finally to the moment the application is closed. Each command entered is logged as well. 

