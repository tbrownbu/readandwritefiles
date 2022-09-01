from ast import main


def main():
    
    outfile = open('philosophers.txt','w')
    outfile.write('John Locke\nDavid Hume\nEdmund Burke')
    outfile.close()

main()