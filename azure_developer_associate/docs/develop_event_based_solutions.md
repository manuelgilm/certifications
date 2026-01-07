# Develop event-based solutions

## Explore Azure Event Grid

### Concepts in Azure Event Grid

**Publishers**

A publisher is the application that sends events to Event Grid. It can be the same application where the events originated, the event source. Organizations that host services outside of Azure can publish events through Event.

A *partner* is a kind of publisher that sends events from its system to make them available to Azure Customers. Partners not only can publish events to Azure Event Grid. but they can also receive events from it.

**Events and cloud events**

An event is the smallest amount of information that fully describes something that happened in a system. Every event has common information like source of the event, the time the 
event took place, and a unique identifier. Every event also has specific information that is only relevant to the specific type of event.

**Event Sources**

An event source is where the event happens. Each event source is related to one or more event types. For example, Azure Storage is the event source for blob created events. IoT is the event source for device created events. Your application is the event source for custom events that you define. Event sources are responsible for sending events to Event Grid.

**Topics**
 A topic holds events that have been published to Event Grid. You typically use a topic resource for a collection of related events. To respond to certain types of events, subscribers (an Azure service or other applications) decide which topics to subscribe to. There are several kinds of topics: custom topics, system topics, and partner topics.

**Event Subscriptions**

A subscription tells the Event Grid which events on a topic we are interesting in receiving. 

**Event Handlers**

From an Event Grid perspective, an event handler is the place where the event is sent. The handler takes some further action to process the event. Event Grid supports several handler types. You can use a supported Azure service or your own webhook as the handler. Depending on the type of handler, Event Grid follows different mechanisms to guarantee the delivery of the event. For HTTP webhook event handlers, the event is retried until the handler returns a status code of 200 – OK. 

## Discover Event Schemas

Azure Event Grid supports two types of event schemas: Event Grid event schema and Cloud event schema. Events consist of a set of four required string properties. The properties are common to all events from any publisher.

## Examples 

* **Triggering simple azure function app using blob event.**

In this example an Azure function is triggered based on a blob event. For more details, click [here](/examples/eventgrid/README.md)