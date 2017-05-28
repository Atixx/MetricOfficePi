import subprocess
def main():
    # command = ['tshark', '-I', '-i', 'wlxf81a670b81f1', '-f', 'type mgt subtype assoc-resp or type mgt subtype deauth']
    command = ['tshark', '-I', '-i', 'wlxf81a670b81f1', '-f', 'type mgt subtype assoc-resp', '-w', '/home/ahalatian/Desktop/lala.txt', '-a', 'duration:5']
    while True:
        subprocess.call(command)

main()
