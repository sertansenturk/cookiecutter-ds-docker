__Definition of ready__ (DOR) indicates what a ticket needs to cover to be considered as complete for someone to start working on. 

The definition of ready facilitates the communication and understanding about the ticket such as its scope, solution method, and deliverables. DOR should be built over the agreement between team members to disallow ambiguities. The DOR may change as time passes, due to a better understanding of the work requirements or changing needs. 

The types of tickets we decided are: [Feature](#feature), [Task](#task), [Bug Fix](#bug-fix), [Spike](#spike), [Epic](#epic). Below are the brief description and requirements for DOR for each type of ticket.

### General

These should be fulfilled in all types of tickets:

* Pointed (except Epics, see below)
* One of the types below added as a label
* Priority (except Epics) assigned as a label
* Assigned to a person
* Added to a Sprint
* Dependencies linked (if applicable)
* Team understands and agrees upon the content & context
* Labeled as Ready

All tickets have to adhere to the structure below:

* One-line summary (optional)
* Reason
* Design
* Acceptance Criteria
* Outcome

Now we will explain each ticket type, as well as the additions and special cases to DOR for each type.

### Feature
Features are tickets, where we develop a new functionality or extend a functionality. A feature ticket could be about improving an experimental pipeline, standardizing data preprocessing, creating an online demo, or automating the evaluation etc. Typically, these would involve finalizing a repeatable/re-runnable deliverable, for example, written code.

In addition to the general criteria, in a feature ticket:

* The acceptance criteria should clarify __unit tests__ and __integration tests__ even if there are none.
* The outcome should clarify the __deliverables__ (code, process etc.) and __documentation__, where applicable.

### Task
Tasks are ad-hoc or one time jobs. Exploring data/results, re-running experiments, preparing a presentation, creating visualizations, or writing a blog post may be considered as tasks.

* Outcome should clarify __deliverables__ (scripts, process etc.) and __documentation__, if applicable.

### Bug fix
A bug fix is a correction to an error, flaw, failure or fault.

* Bug fixes have a _Steps to Reproduce_ and _Expected Behavior_ instead of _Reason_

### Spike
Spikes are research tickets, where we try to define a problem, identify possible solutions, or try out a new tool/method. Spikes typically answer how we should progress on an issue, e.g. how to complete a task or which feature to implement, before we proceed to implement the solution.

* _Design_ ought to include a summary as a list of questions to be answered, for the sake of clarity.

### Epic
Epics are tickets which group other tickets with relevant aims. Epics have to align with Sprint goals, or a recurring type of work (e.g. "Management tickets"). Each ticket should have a single epic.

* Epics only have a description.
* The epics should not be pointed. Its overall point is the summation of all points of related tickets.
