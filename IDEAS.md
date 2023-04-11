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

What about multiple inputs and outputs?

> Of course, not all sequential chains will be as simple as passing a single string as an argument and getting a single string as output for all steps in the chain. In this next example, we will experiment with more complex chains that involve multiple inputs, and where there also multiple final outputs.
>
> Of particular importance is how we name the input/output variable names. In the above example we didn’t have to think about that because we were just passing the output of one chain directly as input to the next, but here we do have worry about that because we have multiple inputs.

# Ebooks

I will download [A General History of the Pirates](https://standardebooks.org/ebooks/captain-charles-johnson/a-general-history-of-the-pirates) from [Standard Ebooks](https://standardebooks.org/).

I will use the [UnstructuredEPubLoader from LangChain](https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/epub.html).

I will follow the [Question Answering over Docs method](https://python.langchain.com/en/latest/use_cases/question_answering.html).

Needs unstructured Python package.

Needs Pandoc.

## Plan of attack

I will load the documents.

I will split the documents.

I will create embeddings.

I will store it in a vectorstore.

I will do a retrieval.

I will then pass documents, along with the original question, to the language model and have it generate a response

That is my current understanding of the process.
