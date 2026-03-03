# Reflection

## Rationale

### Adapter Pattern

The adapter pattern was chosen for handling the external income transactions. This was necessary because the project's definition of a transaction conflicted with the external transaction definition. The assumption is that the external transaction definition could not be changed. The adapter pattern makes sense here as a way to conform the external definition to our project's definition without having to modify the external code, i.e. transaction. The downside of this is a little more complexity. But, the tradeoff is worth it here so as to form a boundary between our definition and the other definition.

### Singleton Pattern

The singleton was chosen to centralize the tracking of the balance. If the application could instantiate multiple balance objects when needed, there would certainly be race conditions as the app scaled. By centralizing, i.e. global, the balance would not be instantiated across multiple objects, so as to avoid having to have a way to reconcile the fragmented balance tracking. The downside of this is that I am not sure how well the balance class would scale. As written, it would not be able to handle tracking of multiple balances. If there was a desire to do this, additional logic would have to be provided. Even then, there could lead to performance challenges doing the balance tracking in "real-time."

### Observer Pattern


### Decorator Pattern
(Going to do this for the adding information about the account using the balance)
