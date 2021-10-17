# Message Protocol

## Overview

Messages are how data is passed between publishers and subscribers. Messages are plaintext, comma-delimited strings with the following format:

```plaintext
<MESSAGE-TYPE>,<TIMESTAMP>,<MESSAGE-PAYLOAD>
```

Depending on the type of message, the message payload will have a different format, but in general, like the full message, it is a comma-delimited string.

## Message Types

### Subscribe

Subscribe messages are used by a subscriber to subscribe to data from a publisher. They are the first point of contact between a publisher and subscriber, and function to initialize the connection.

Subscribe messages have the following format:

```plaintext
subscribe,<TIMESTAMP>,<PUBLICATION>[,<PUBLICATION>...]
```

Upon successful processing of a subscribe message, the publisher will echo the subscribe message back to the subscriber (albeit with an altered timestamp) to confirm successful subscription.

### Submit

Submit messages are used by a subscriber to push data to a publisher. A subscriber does not need to be subscribed to any publications to send submit messages to a publisher.

Submit messages have the following format:

```plaintext
submit,<TIMESTAMP>,<PUBLICATION>,<MESSAGE-DATA>
```

The message data will have a different format depending on the publication its data is for, but in general it will be a comma-delimited string whose tokens are data fields.

### Publish

Publish messages are used by a publisher to forward data to subscribers. They have the same format as submit messages, but are used to send data in the opposite direction.

Publish messages have the following format:

```plaintext
publish,<TIMESTAMP>,<PUBLICATION>,<MESSAGE-DATA>
```
