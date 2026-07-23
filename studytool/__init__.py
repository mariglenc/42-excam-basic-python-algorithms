"""studytool — a small CLI study/drill tool for this exercise repo.

Modules
-------
enparser   parse an .en exercise file -> title, function name, signature, examples
discovery  scan the repo for exercises and resolve filters (all / one / a group)
attempts   find/create try<N>.py attempt files (never overwrites)
grader     import an attempt, run it against the parsed examples, score it
progress   persistent JSON store (.progress.json) + spaced-repetition weighting
cli        argparse command line: list / ask / grade / stats / solution
"""

__all__ = ["enparser", "discovery", "attempts", "grader", "progress", "cli"]
