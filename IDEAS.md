Read https://medium.com/@neonforge/how-to-automate-midjourney-image-generation-with-python-and-gui-automation-ac9ca5f747ae

Make a Discord bot.

Usage is at https://platform.openai.com/account/usage - coding tonight was 2 cents, including aicommits.

Billing is at https://platform.openai.com/account/billing/overview

## Scripts

## Chat message history

## Output parsers

## Chains

What is in `chains.py`?

Each individual chain has a single input and a single output, and the output of one step is used as input to the next.

```python
overall_chain = SimpleSequentialChain(chains=[location_chain, meal_chain], verbose=True)

review = overall_chain.run("Oslo")
```

The `chains.py` file has a `SimpleSequentialChain` class that takes a list of chains and runs them in sequence. The output of one chain is used as input to the next. The first chain gets Oslo as input, and the second chain gets the output of the first chain as input.

When the input is Oslo:

```markdown
> Entering new SimpleSequentialChain chain...

A classic dish from the Oslo region is lapskaus. It is a stew made with potatoes, carrots, beef and other vegetables cooked in beef broth. It is often served with mustard, bread, and pickles.
```