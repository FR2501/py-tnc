import argparse

PROGRAM = 'py-tnc'
VERSION = '1.0.0'

LANGUAGES = ['ger']
CORPUS_VERSIONS = ['2019']

parser = argparse.ArgumentParser(prog=PROGRAM)

parser.add_argument('-v', '--version', help='print version and exit', action='store_true')

parser.add_argument('-l', '--language', help='specify language of base corpus')
parser.add_argument('-c', '--corpus-version', help='specify version of base corpus')
parser.add_argument('-k', '--top-k-filter', metavar='K', help='keep only k most frequent n-grams')
parser.add_argument('-d', '--dictionary-filter', metavar='FILE', help='keep only n-grams in specified dictionary file')
parser.add_argument('-o', '--output-dir', metavar='DIR', help='specify output directory', default='output')
parser.add_argument('-y', '--years', nargs=2, metavar=('MIN', 'MAX'), help='specify min and max years', default=(1800, 2000))

args = parser.parse_args()
print(args)

if args.version:
    print(f'{PROGRAM} version {VERSION}')
    exit(0)

has_error = False
if args.language is None or args.language not in LANGUAGES:
    print('!-- no language specified --!')
    print(f'\t possible values: {", ".join(LANGUAGES)}')
    has_error = True

if args.corpus_version is None:
    print('!-- no corpus version specified --!')
    print(f'\t possible values: {", ".join(CORPUS_VERSIONS)}')
    has_error = True

if has_error:
    parser.print_usage()
    exit(1)

