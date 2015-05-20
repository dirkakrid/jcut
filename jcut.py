import json
import sys

def parse_file(files,fields,fgrep):
    for fn in files:
        with open(fn) as f:
            for line in f:
                parse_line(line,fields,fgrep)

def parse_stdin(fields,fgrep):
    for line in sys.stdin:
        parse_line(line,fields,fgrep)

def parse_line(line,fields,fgrep):
    j = json.loads(line)
    if fgrep is not None:
        all_values = ''.join([str(i) for i in j.values()])
        if fgrep not in all_values:
            return
    if fields is None:
        fields = j.keys()
    formatter = ' '.join(['{}' for _ in range(len(fields))])
    field_text = [j[field] for field in fields]
    print formatter.format(*field_text)
    return

def main():
    import argparse
    parser = argparse.ArgumentParser(description='print fields from JSON input')
    parser.add_argument('--file',\
                        nargs = '+',\
                        help='input from filename(s) instead of stdin')
    parser.add_argument('-fg',\
                        '--fields',\
                        nargs = '+',\
                        help='fields to print')
    parser.add_argument('-g',\
                        '--fgrep',\
                        help='find fixed string in any field (including unselected fields)')
    args = parser.parse_args()
    if args.file:
        files = args.file
        parse_file(files,args.fields,args.fgrep)
    else:
        parse_stdin(args.fields,args.fgrep)

if __name__ == '__main__':
    main()
