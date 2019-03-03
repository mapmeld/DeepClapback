# encoding: utf-8
lines = open('./clapbacks.csv', 'r').read().split("\n")
badmemes = open('./bad_memes.csv', 'r').read().split("\n")
fixed = open('./fixed.csv', 'w')

# Google Cloud storage needs fewer labels

usedphrases = ['NOMEME']

# for bad meme combination
for line in badmemes:
    if (len(line) > 1 and line[:3] != '"",'):
        phrase = line[:line.index(',')]
        if len(line) > len(phrase) + 6:
            line = line.replace(phrase + ',', '', 1) + ',NOMEME'
            fixed.write(line + "\n")

for line in lines:
    if (len(line) > 1 and line[:3] != '"",'):
        phrase = line[:line.index(',')]
        standardphrase = phrase.lower().strip().replace('.', '').replace('&lt;3', 'heart').replace('/', '').replace('ಠ_ಠ', 'lookofdisapproval').replace('(╯lookofdisapproval）╯︵┻━┻', 'throwstable').replace(':-(', 'frownyface').replace(':(', 'smallfrowny').replace(';)', 'smallwink').replace("'", '').replace(' ', '').replace('?', '').replace('!', '').replace('*', '').replace('(͡°͜ʖ͡°)', 'lennyface').replace(':)', 'smallsmiley').replace('-', '').replace('^', '')
        if '┻━┻' in phrase:
            standardphrase = 'throwstable'
        if '_(ツ)_' in phrase:
            standardphrase = 'shrug'

        if not standardphrase.replace('"', '').isalnum():
            print(standardphrase)

        if len(line) > len(phrase) + 6 and standardphrase.isalnum() and len(standardphrase) > 0 and (standardphrase in usedphrases or len(usedphrases) < 99):
            if standardphrase not in usedphrases:
                usedphrases.append(standardphrase)
            line = line.replace(phrase + ',', '', 1) + ',' + standardphrase #.replace('""', '"')
            fixed.write(line + "\n")
