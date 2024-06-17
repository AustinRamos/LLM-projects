This project showcases a Python-based culinary assistant leveraging OpenAI's GPT-3.5-turbo model and API.
it first emulates an assistant tasked to categorize a request for one of the following:
1) a recipe suggestion
2) a dish suggestion 
3) a critique of a recipe


# ChefGPT Project Demonstration Report

**Prepared by**: Austin Ramos  
**Date**: [Insert Date]

## Project Overview

The `ChefGPT` project is a Python-based interactive culinary assistant that uses OpenAI's GPT-3.5-turbo model. The assistant is designed to provide suggestions for dishes based on ingredients, detailed recipes, and critiques of provided recipes, all while emulating the persona of Anthony Bourdain.

### Key Features

- **Ingredient-based Dish Suggestions**
- **Detailed Recipe Provision**
- **Constructive Recipe Critiques**

## Demonstration

### Interaction 1: Recipe Critique

**User Input**:
```plaintext
ok i have a recipe where I first take a raw fish, i shred it in a meat shredder mixed with pork. then i soak it in water and fry it up in a deep fryer.
```

Response Type: CRITIQUE

Assistant's Critique:

```plaintext
Oh boy, where do I even start with this one? Mixing raw fish with pork and shredding it in a meat shredder is a culinary crime in itself. Fish and pork have vastly different textures and flavors that just don't play well together—it's like trying to make a symphony out of two very off-key instruments.
Soaking this strange concoction in water before deep frying only adds insult to injury. Waterlogged, mushy fish-pork mishmash is not something that will win you any culinary awards, trust me.
```


Interaction 2: Ingredient Suggestion
User Input:

```plaintext
i have a recipe that is toast, with lard sprinkled on top, and 100 pickles
```

Response Type: SUGGESTION

Assistant's Response:

```plaintext
Well, that's certainly a unique combination! Let's see what we can do with toast, lard, and 100 pickles. How about a play on a classic Cuban sandwich?
We'll start by making a sandwich with layers of thinly sliced ham, roasted pork, Swiss cheese, and mustard between two slices of toasted bread with a generous amount of lard spread on the outside for a crispy finish. Then, we'll top it off with a mountain of pickles for that tangy kick.
```



Interaction 3: Ingredient Suggestion
User Input:

```plaintext
i have the following ingredients, 1 egg, an orange, soda, and walnuts
```

Response Type: SUGGESTION

Assistant's Response:

```plaintext
Well, with that interesting mix of ingredients, how about making an orange walnut cake? You can use the egg for binding, the orange for flavor and zest, soda for leavening, and walnuts for texture and crunch. It might sound unconventional, but sometimes the most delicious creations come from unexpected combinations. Give it a try and let your taste buds take a wild ride! Just remember, cooking is an adventure, so embrace the unexpected.
```