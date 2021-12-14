

>Data was never the new oil. It was always the new toxic waste: pluripotent, immortal – and impossible to contain. You don’t want to be making more of it, and you definitely should be getting rid of the supply you’ve so unwisely stockpiled so far.
>
>Data minimization isn’t just good practice; it’s good business. Collect as little data as you can, and keep it as briefly as you can. If your privacy policy fits on the back of a napkin – because you’re collecting almost nothing and processing it only for specific purposes, and then deleting it forever – you’re on the right track!

--- Cory Doctorow (https://www.kaspersky.com/blog/secure-futures-magazine/data-new-toxic-waste/34184/)

---

## What we do

Dataventures is often in a position of trust. We take data security extremely seriously. One of the ways we do this is to make sure we minimise the data we hold for processing.

Where possible, we prefer to minimise the attack area on some pieces of information by never needing to have it in the first place.

Sometimes, we get data which may be useful as a key to enable us to combine datasets from different sources. Typicially this is the known primary key for unit records. In the unlikely event of a data breach, knowing this may enable the leaking of sensitive information.

Obviously, we would rather not hold that. You can't leak in a breach what you never have after all.

---

## How we do this

If we ask our individual data suppliers to normalise and then cryptographically hash the keys at the source, using the same key _which is never revealed to Dataventures_ we can have a key which is useful for joins, but isn't itself identifiable. 

This process is not a complete solution. An attacker may be able re-identify the subject from the rest of the information in that record. That is a different problem, and has other mitigation strategies. But this gives you a starting point.

The steps we take are.

* Give our data suppliers a way to generate a key between them. It is a shared secret. 
* Each supplier normalises the data which is being hashed, so the data on each side refering to the same id will hash to the same value given the same key.
* Each supplier applies the crypto hash to thier records.
* We get the resulting datasets and compute the join.

Without the key Dataventures can't walk the input space and generate a rainbow table to reverse the hash. More importantly, neither can anyone else.
