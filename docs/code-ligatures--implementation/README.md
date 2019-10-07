# Implementing Code Ligatures

There are three primary possible ways I see to implement code ligatures:

1. Emulate Fira Code: use `calt` to make code ligatures default, and let people disable them if they want to.
2. Use a `CODE` axis with alternates & GSUB set up in the designspace. This could be layered on top of the calt approach – it would have "invisible" composed ligatures by default, but more-connected, "code ligaturey" ligatures available when CODE gets turned up to 1.
3. Use `dlig`, checking that contextual control is still possible (I think it is, but need to verify). 

## Fira Code, using DLIG instead of CALT

I asked @tonsky why Fira Code uses `calt`, when `dlig` may be more "by the book" for this type of feature (https://github.com/tonsky/FiraCode/issues/854). His initial reply was:

> I don’t remember exactly but one reason why I put them into calt instead of liga/dlig is because lookups or subs I use didn’t work in liga/dlig. Are they working ok for you?

With a quick test in a forked Fira Code file, these *do* seem to work if the feature code is moved from CALT to DLIG. Here is an image in Sketch:

![](assets/2019-10-06-22-26-34.png)

(This font is stored at `docs/code-ligatures--implementation/assets/FiraCodeDLIG-Bold.otf`, and is made from the `dlig-test` branch of @thundernixon/firacode).


## Testing in Recursive

I'm starting in `src/masters/mono/Recursive Mono-Linear B.ufo/features.fea`.

**Questions to answer:**

- How can I write this code in a central location then import it in?
- Why does the Fira Code feature use `LIG` in the lookups? What is that?
- (Make separate issue): What other features need to be written to make this font work well?