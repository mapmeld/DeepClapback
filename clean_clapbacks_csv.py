# encoding: utf-8
lines = open('./clapbacks.csv', 'r').read().split("\n")
badmemes = open('./bad_memes.csv', 'r').read().split("\n")
fixed = open('./fixed.csv', 'w')

# Google Cloud storage needs fewer labels

usedphrases = ['NOMEME']

# for bad meme combination
for line in badmemes:
    if (len(line) > 3 and (',' in line) and line[:3] != '"",'):
        phrase = line[:line.index(',')]
        if len(line) > len(phrase) + 6:
            line = line.replace(phrase + ',', '', 1) + ',NOMEME'
            fixed.write(line + "\n")

for line in lines:
    if (len(line) > 1 and (',' in line) and line[:3] != '"",'):
        phrase = line[:line.index(',')]
        standardphrase = phrase.lower().strip().replace('.', '').replace("'", '').replace(' ', '').replace('?', '').replace('!', '').replace('*', '').replace('/', '').replace('-', '').replace('^', '').replace('&lt;3', 'heart').replace('ಠ_ಠ', 'lookofdisapproval').replace('(╯lookofdisapproval）╯︵┻━┻', 'throwstable').replace(':(', 'frownface').replace(';)', 'wink').replace('(͡°͜ʖ͡°)', 'lennyface').replace(':)', 'smallsmiley')
        if 'If you would also like to protect yourself, add the Chrome extension' in phrase:
            continue
        if '┻━┻' in phrase:
            standardphrase = 'throwstable'
        if '_(ツ)_' in phrase:
            standardphrase = 'shrug'
        if 'datboi' in standardphrase:
            standardphrase = 'datboi'
        if 'thatsthejoke' in standardphrase:
            standardphrase = 'thatsthejoke'
        if 'checksout' in standardphrase:
            standardphrase = 'xchecksout'
        if 'shitwaddup' in standardphrase:
            standardphrase = 'ohshitwaddup'
        if standardphrase == 'woosh' or standardphrase == 'whoosh':
            standardphrase = 'woosh'
        if standardphrase == 'thanks' or standardphrase == 'thankyou':
            standardphrase = 'thanks'
        if standardphrase == 'haha':
            standardphrase = 'lol'

        if not standardphrase.replace('"', '').isalnum():
            #print(standardphrase)
            x = 1

        if len(line) > len(phrase) + 6 and standardphrase.isalnum() and len(standardphrase) > 0 and (standardphrase in usedphrases or len(usedphrases) < 99) and standardphrase != 'yes' and standardphrase != 'no' and standardphrase != 'shrug':
            if standardphrase not in usedphrases:
                usedphrases.append(standardphrase)
            line = line.replace(phrase + ',', '', 1) + ',' + standardphrase #.replace('""', '"')
            fixed.write(line + "\n")
