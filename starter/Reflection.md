# Reflection

## Rationale

### Adapter Pattern

The adapter pattern was chosen for handling the external income transactions. This was necessary because the project's definition of a transaction conflicted with the external transaction definition. The assumption is that the external transaction definition could not be changed. The adapter pattern makes sense here as a way to conform the external definition to our project's definition without having to modify the external code, i.e. transaction. The downside of this is a little more complexity. But, the tradeoff is worth it here so as to form a boundary between our definition and the other definition.

### Singleton Pattern

The singleton was chosen to centralize the tracking of the balance. If the application could instantiate multiple balance objects when needed, there would certainly be race conditions as the app scaled. By centralizing, i.e. global, the balance would not be instantiated across multiple objects, so as to avoid having to have a way to reconcile the fragmented balance tracking. The downside of this is that I am not sure how well the balance class would scale. As written, it would not be able to handle tracking of multiple balances. If there was a desire to do this, additional logic would have to be provided. Even then, there could lead to performance challenges doing the balance tracking in "real-time."

### Observer Pattern

The observer pattern was used by the Balance class to perform various actions in other classes, such as alerting and printing updates. The advantage of the pattern is that the behaviors to be performed when the balance is updated are implemented outside of the balance code. This adheres to open/closed principle at the expense of having to manage more classes. But again results in a solution that is more cohesive and separates concerns better than one giant class. One thing that I did do in order to separate the notification logic from the balance logic was to create a BalanceNotifier singleton used inside the balance class in order to handle the notification logic. In this way, the notification logic is implemented separately, though tightly coupled to, the balance logic.

### Decorator Pattern

For the fourth pattern I am using the decorator pattern in order to add additional information about the account the balance is tracking. In this pattern, I can add additional functionality without modifying the balance class itself which is already doing a bunch of heavy lifting tracking the balance updates. This favors composition over inheritance. The down side is more classes to manage and potentially debug. Part of my motivation for doing this was that this was the hardest design pattern for me to visualize and implement, so I want to work on it.
