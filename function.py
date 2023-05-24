def nice_print(doc):
    print('{:<14} {:<10} {:<12}'.format('text', 'pos_', 'dep_'))
    print('_'* 55)
    for token in doc:
        print('{:<14} {:<10} {:<12}'.format(token.text, token.pos_, token.dep_))
    print('_'* 55)
    