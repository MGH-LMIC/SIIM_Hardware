from predict import Hardware_detection
import sys
if __name__ == '__main__':
    HW = Hardware_detection()
    file_url = sys.argv[1]
    print(HW.predict(file_url))