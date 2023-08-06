---
**<font  color='0000ff' size=7>P</font><font  color='ffbb00' size=8>y</font><font size=7>LogLib</font>**

---

**A python logging library designed to be quick and easy to use
with a large amount of customization options
while still remaining simple**

## Log <font  color='00aa00' size=4>class</font>

### Syntax

**`Log(prefix, surfix, splitter, time, clock, saveprefix, printprefix, savesurfix, printsurfix, savetime, printtime, print, file)`**

### Description

Use Log() to create a Log object, this is essential for logging since it contains all the methods
in the library.

### Arguments

- prefix `string` --- the default prefix for all logged messages
- surfix `string` --- the default surfix for all logged messages
- splitter `string` --- text to split the start of the message from the message content
- time `boolen` --- if the time when logged should be displayed in the message
- clock `clock` --- if the time should contain the current clock
- saveprefix `boolen` --- if the prefix should be included in the message saved to file
- printprefix `boolen` --- if the prefix should be included in the printed message
- savesurfix `boolen` --- if the surfix should be included in the message saved to file
- printsurfix `boolen` --- if the surfix should be included in the printed message
- savetime `boolen` --- if the time should be included in the message saved to file
- printtime `boolen` --- if the time should be included in the printed message
- print `boolen` --- if the logged messages should be printed to the console
- file `string` --- file to log messages to (if left blank the messages will not be logged to a file)

## log <font  color='9955ff' size=4>method</font>

### Syntax

**`log(content, prefix, surfix, time)`**

### Description

log() is a method of Log(), it is the standard way to log a message via the parameters of the object it is used on.
you can change these parameters with the arguments: `prefix, surfix, time`.

### Arguments

- content `string` --- the content that the message contains
- prefix `string` --- what prefix the message should have, if left blank it will used the default value defined in Log()
- surfix `string` --- what surfix the message should have, if left blank it will used the default value defined in Log()
- time `boolen` --- if the time when logged should be displayed in the message, if left blank it will used the default value defined in Log()

## logtitle <font  color='9955ff' size=4>method</font>

### Syntax

**`logtitle(content)`**

### Description

logtitle() is a method of Log() and is used to display some content in a very visible format, it is typically
used for marking the start and end of tasks.

### Arguments

-  `content` --- the content of the title

## lograw <font  color='9955ff' size=4>method</font>

### Syntax

**`lograw(content)`**

### Description

logtitle() is a method of Log() and is used to log a raw message without prefixes, surfixes or time.

### Arguments

-  `content` --- the content of the message

## clear <font  color='9955ff' size=4>method</font>

### Syntax

**`clear()`**

### Description

clear() is a method of Log() and is used to wipe a log of all of it's previous messages.

### Arguments

- This method does not have any arguments

## remove <font  color='9955ff' size=4>method</font>

### Syntax

**`remove(number)`**

### Description

remove() is a method of Log() and is used to remove a certain amount of messages from a log.

### Arguments

- number `integer` --- the number of messages to remove

---
**<font size=7>PyLogLib v1.0.0 - Change Log</font>**

---

- **First Release**

---