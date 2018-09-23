import re
def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return


#re.match or compiled_pattern_regex.match gives a match object. Call start and end on it
#re.findall(pattern, text) or regex.findall(text) gives a list of substrings which match the pattern
#re.fullmatch(pattern,text) or regex.fullmatch(text) returns the match object only if the entire input fits into one pattern
#re.compile(pattern) to save a pattern into a  object
#ab{lower_bound_inc, upper_bound_inc} for bounds on number of bs. ? is shortcut for 0 or 1, + is at least one, * is any
#ab{lower_bound_inc,upper_bound_inc}? means the greediness is turned off. stop once match
#[ab] to group characters
#[^.- ]+ for sequences without ^.-
#. is a wildcard
#Escape codes. \d : digit \D non-digit \s space (incl tab) \S nonspace \w alphanumeric \W non-alphanumeric
# Anchoring. ^ : Start, $: end, \A start of string, \Z endo f string, \b empty string at beginning or end of word,
# Groups of characters. Use match_object.groups() to access and parenthesis to indicate groups.
#Use the flag re.IGNORECASE to ignore case or re.MULTILINE for anchors to work on multiple lines
# Use (?=) for positive lookahead and (?!) for negative look ahead. They are assertions that dont consume characters
# In search, if the first match (ignoring the assertion) does not meet the assertion, it fails completely.
# When assertiong, findall still tries all possible positions
match = re.search("this", "is this in this?")
print("The first match goes from {} to {}".format(match.start(), match.end()))

#What if no match
no_match = re.search("that", "is this in this?")
print("No match looks like {}".format(no_match))

#Precompiling a pattern
print("Precompiling a pattern")
regex = re.compile("this")
print("Matching from a regex object. Result is {} ".format(regex.search("is this in this?")))
print("Finding all from a regex object. Result is {}".format(regex.findall("is this in this?")))

#Repetition in pattern
print("Greedy repetition")
test_patterns("abbaabbba", [("ab+","a then at least one b")])
test_patterns("abbaabbba", [("ab{3}","a then exactly 2 bs")])
test_patterns("abbaabbba", [("ab*","a then any number of bs")])
test_patterns("abbaabbba", [("ab?","a then 0 or 1 b")])
test_patterns("abbaabbba", [("ab{1,3}","a then 1 to 3 b")])

#Nongreedy repetition
print("Non-greedy repetition")
test_patterns("abbaabbba", [("ab+?","a then at least one b")])
test_patterns("abbaabbba", [("ab{3}?","a then exactly 2 bs")])
test_patterns("abbaabbba", [("ab*?","a then any number of bs")])
test_patterns("abbaabbba", [("ab??","a then 0 or 1 b")])
test_patterns("abbaabbba", [("ab{1,3}?","a then 1 to 3 b")])

#character sets
print("testing character sets")
test_patterns(
    'abbaabbba',
    [('[ab]', 'either a or b'),
     ('a[ab]+', 'a followed by 1 or more a or b'),
     ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')],
)

#exclusion testing
#character sets
print("testing character sets")
test_patterns(
    'abbaabbba',
    [('[^a]', 'Match if not a'),
     ('[^a]+', 'Sequences delimited by a')],
)

#testing out escape codes
test_patterns(
    'A prime #1 example!',
    [(r'\d+', 'sequence of digits'),
     (r'\D+', 'sequence of non-digits'),
     (r'\s+', 'sequence of whitespace'),
     (r'\S+', 'sequence of non-whitespace'),
     (r'\w+', 'alphanumeric characters'),
     (r'\W+', 'non-alphanumeric')],
)

#Anchoring

test_patterns(
    'This is some text -- with punctuation.',
    [(r'^\w+', 'word at start of first line'),
     (r'\A\w+', 'word at start of string'),
     (r'\w+\S*$', 'word near end of string'),
     (r'\w+\S*\Z', 'word near end of string'),
     (r'\w*t\w*', 'word containing t'),
     (r'\bt\w+', 't at start of word'),
     (r'\w+t\b', 't at end of word'),
     (r'\Bt\B', 't, not start or end of word')],
)

# fullmatch
print("Full matching here")
full_match_regex = re.compile("everything is here")
print(full_match_regex.fullmatch("everything is here"))

#groups

test_patterns(
    'abbaaabbbbaaaaa',
    [('a(ab)', 'a followed by literal ab'),
     ('a(a*b*)', 'a followed by 0-n a and 0-n b'),
     ('a(ab)*', 'a followed by 0-n ab'),
     ('a(ab)+', 'a followed by 1-n ab')],
)

#accessing groups
print()
print("Accessing groups in a search")
text = 'This is some text -- with punctuation.'
print(re.search(r"(\b\w+)(\W+)(\w+)",text).groups())

#ignoring case
print("Adding IGNORECASE flag to re.compile")
without_case = re.compile('T', re.IGNORECASE)
print(text)
print(without_case.findall(text))

#Multiline
print()
print("Adding MULTILINE flag to re.compile")
single_line = re.compile(r"^this")
multi_line = re.compile(r"^this", re.MULTILINE)
text= """this is cow
that is dog
this is chicken
"""
print('single line version {}'.format(single_line.findall(text)))
print('multiline version {}'.format(multi_line.findall(text)))

# Positive look ahead
print()
print("Trying out positive look ahead. Accept only things fully enclosed in brackets or not at all")
text = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
]
print("Text: {}".format(text))
email_matcher = re.compile(r"\s+(?=(<[\w.]+@[\w.]+>$)|([^<].*[^>]$))"
                           r"<?[\w.]+@[\w.]+>?")
for t in text:
    print(t, ": ", email_matcher.search(t))

#negative lookahead
print()
print("negative lookahead")
address = re.compile(
    '''
    (?!noreply)[\w.]+@[\w.]+
    ''',
    re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'second@example.com noreply@example.com',
]
for t in candidates:
    print(t, ": " , address.findall(t))

