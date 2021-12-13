## The motivation

Data was never the new oil. It was always the new toxic waste: pluripotent, immortal – and impossible to contain. You don’t want to be making more of it, and you definitely should be getting rid of the supply you’ve so unwisely stockpiled so far.

Data minimization isn’t just good practice; it’s good business. Collect as little data as you can, and keep it as briefly as you can. If your privacy policy fits on the back of a napkin – because you’re collecting almost nothing and processing it only for specific purposes, and then deleting it forever – you’re on the right track!

--- Cory Doctorow (https://www.kaspersky.com/blog/secure-futures-magazine/data-new-toxic-waste/34184/)

---

## What we do

Dataventures is often in a position of trust, and as such needs to take security extremely seriously. One of the ways we do this is to make sure we minimise the data we hold for processing.

If we can minimise the attack area on some data by never needing to have it in the first place, that is what we do.

Sometimes, we get data which is useful as a key to combine datasets from different sources, typicially this is known primary key for unit records. Obviously, we would rather not have that, if we are going to combine datasets, and aggregate up the results for consumption. You can't leak in a breach what you never have after all.

---

## How we do this

If we normalise and then cryptographically hash the keys at the source, using the same key, _which we never know what it is_ we can have a key which is useful for joins, but isn't itself identifyable. 

This does not mean that you may not be able to work it out from the rest of the data for that record, that is a different problem, and has other mitigation strategies. But this gives you a starting point.

The steps we take are.

* Give the data sources a way to generate a key between them, it is a shared secret between them. 
* Normalise the data which is being hashed, so the data on each side refering to the same id will hash to the same value given the same key.
* Apply the crypto hash.
* We get the resulting dataset.

Without the key, we can't walk the input space, and effectively generate a rainbow table, to reverse it. More importantly, neither can anyone else.
