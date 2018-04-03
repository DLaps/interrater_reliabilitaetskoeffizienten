# Danlaps Inter-Rater Agreement Program
A simulation program for inter-rater reliability coefficients.

The .NET Framework (Version 4.5.2) or Mono must be installed to run the program.
## Content
```
-- createBoxplots.py :: python script to create boxplots visualizing the
|                       simulation results
|
-- simulationDefinitions :: contains simulation definitions  of all executed
|                           simulations
|
-- simulationResults :: contains the results of the simulations and boxplots of
|                       the results
|
-- specs :: contains XML Schema files, which specifies the format of files,
|            which can be loaded and/or saved by the program
|
-- src
|  |
|  |-- InterRaterAgreementLibrary :: contains the source code of the simulation
|                                    framework
|  |-- InterRaterAgreementProgram :: contains the source code of the program
|  
```

## Build the program
Load the two solutions in your IDE (Visual Studio or MonoDevelop) and build the
solutions in the IDE.

## Run the program
On Windows: Just double click on iragreement.exe.
On Linux execute: ```mono iragreement.exe```

When you start the programm you enter the path, where the simulation results are
stored. After that you can execute one of the following commands:

|Command|Description|
|---|---|
|```add <path to simulation definition file>```|Adds the specified simulation to the simulator|
|```clear``` | Deletes all simulations of the simulator.|
|```list``` | Lists the names of the simulations, which was added to the simulator.
|```exit```| Closes the program.|
|```precision <number>```| Defines the precision of the displayed results after a simulation run.|
|```run all``` | Runs all added simulations.|
|```run <name>``` | Runs the specified simulation.|
