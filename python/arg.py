import argparse
parser = argparse.ArgumentParser(description="doesn't matter")
parser.add_argument('w', help='run hi function')

def hi():
    print('how you doin')

args = parser.parse_args()
if(args.w):
    hi()

