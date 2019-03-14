# Library Simulation
Discrete Event Simulation of a Library in Python by using SimPy package.

## Setup
```
$ pip install simpy
```
https://simpy.readthedocs.io/en/latest/simpy_intro/installation.html

## Scenerio
In the Library, there are books with limited amount to be requested by students. Students which is registered to library go to the library for requesting to borrow a book. When a student request a book that is available, she/he can borrow immediately. If not, a student needs to wait for demand queue or another student to give the book back. However, there is special membership called gold membership that enables students to borrow without waiting for the queue. The scenario and process are explained clearly in the diagram below.

![Process Diagram](http://www.sebahattinonurozler.com/wp-content/uploads/2019/03/Blank-Diagram.png)

![Example Scenerio](http://www.sebahattinonurozler.com/wp-content/uploads/2019/03/simulationGif.gif)